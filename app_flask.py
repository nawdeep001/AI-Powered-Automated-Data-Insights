from flask import Flask, render_template, request
import os
from werkzeug.utils import secure_filename

from data_insights import (
    load_and_clean_csv,
    generate_insights,
    create_visualizations
)

from ai_insights import generate_ai_insights


app = Flask(__name__)

UPLOAD_FOLDER="uploads"

app.config["UPLOAD_FOLDER"]=UPLOAD_FOLDER

os.makedirs(
    UPLOAD_FOLDER,
    exist_ok=True
)


@app.route("/")
def index():

    return render_template(
        "index.html"
    )


@app.route(
    "/analyze",
    methods=["POST"]
)

def analyze():

    try:

        ##################################
        # FILE CHECK
        ##################################

        if "file" not in request.files:

            return "No file uploaded"

        file=request.files["file"]

        if file.filename=="":

            return "No file selected"

        ##################################
        # SAVE FILE
        ##################################

        filename=secure_filename(
            file.filename
        )

        filepath=os.path.join(
            app.config["UPLOAD_FOLDER"],
            filename
        )

        file.save(
            filepath
        )

        ##################################
        # LOAD DATA
        ##################################

        df=load_and_clean_csv(
            filepath
        )

        ##################################
        # GENERATE INSIGHTS
        ##################################

        insights=generate_insights(
            df
        )

        ##################################
        # AI INSIGHTS
        ##################################

        try:

            ai_text=generate_ai_insights(
                insights
            )

        except Exception as e:

            ai_text=f"AI Failed: {str(e)}"

        ##################################
        # VISUALIZATIONS
        ##################################

        plots=create_visualizations(
            df
        )

        plot_json={

            k:v.to_json()

            for k,v in plots.items()

        }

        ##################################
        # TABLE PREVIEW
        ##################################

        preview=df.head(
            10
        ).to_html(
            classes="table table-striped",
            index=False
        )

        ##################################
        # SEND TO HTML
        ##################################

        return render_template(

            "results.html",

            summary={

                "rows":df.shape[0],

                "columns":df.shape[1],

                "numeric_cols":
                    insights[
                        "numeric_columns"
                    ],

                "cat_cols":
                    insights[
                        "categorical_columns"
                    ]
            },

            stats=
                insights[
                    "descriptive_stats"
                ],

            ai_insights=
                ai_text,

            head=
                preview,

            plots=
                plot_json
        )

    except Exception as e:

        return f"ERROR: {str(e)}"



if __name__=="__main__":

    app.run(

        debug=True,

        port=5000

    )