import pandas as pd
import numpy as np
import plotly.express as px


########################################################
# LOAD + CLEAN DATA
########################################################

def load_and_clean_csv(file_path):

    try:

        #########################################
        # Load CSV
        #########################################

        df = pd.read_csv(file_path)

        #########################################
        # Clean column names
        #########################################

        df.columns = [

            col.strip()

            .lower()

            .replace(" ","_")

            .replace("/","_")

            for col in df.columns

        ]

        #########################################
        # Replace missing values
        #########################################

        df = df.replace(

            [

                '',

                ' ',

                'NA',

                'N/A',

                'null',

                'None'

            ],

            np.nan

        )

        #########################################
        # Detect probable date columns
        #########################################

        object_cols = df.select_dtypes(

            include=['object']

        ).columns

        for col in object_cols:

            sample = (

                df[col]

                .dropna()

                .astype(str)

                .head(20)

            )

            if len(sample)==0:

                continue

            looks_like_dates = sample.str.contains(

                r'[-/:]|jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec',

                regex=True,

                case=False

            )

            if looks_like_dates.mean() < 0.5:

                continue

            converted = pd.to_datetime(

                df[col],

                errors='coerce'

            )

            if converted.notna().mean() > 0.7:

                df[col]=converted

        return df

    except Exception as e:

        raise Exception(

            f"Error loading CSV: {str(e)}"

        )


########################################################
# INSIGHTS
########################################################

def generate_insights(df):

    numeric_cols = df.select_dtypes(

        include=np.number

    ).columns.tolist()

    categorical_cols = df.select_dtypes(

        include=[

            'object',

            'category',

            'bool'

        ]

    ).columns.tolist()

    insights = {

        "shape":

            df.shape,

        "columns":

            list(df.columns),

        "numeric_columns":

            numeric_cols,

        "categorical_columns":

            categorical_cols,

        "missing_values":

            df.isnull()

            .sum()

            .to_dict(),

        "descriptive_stats":

            df.describe(

                include='all'

            )

            .fillna("")

            .round(3)

            .to_dict(),

        "correlation":

            (

                df[numeric_cols]

                .corr()

                .round(3)

                .to_dict()

            )

            if len(numeric_cols)>1

            else {}

    }

    return insights


########################################################
# VISUALIZATIONS
########################################################

def create_visualizations(df):

    plots={}

    numeric_cols = df.select_dtypes(

        include=np.number

    ).columns.tolist()

    categorical_cols = df.select_dtypes(

        include=[

            'object',

            'category'

        ]

    ).columns.tolist()

    #########################################
    # Histogram
    #########################################

    if len(numeric_cols)>0:

        col = numeric_cols[0]

        plots['histogram'] = px.histogram(

            df,

            x=col,

            title=f"Distribution of {col}"

        )

    #########################################
    # Correlation Heatmap
    #########################################

    if len(numeric_cols)>1:

        numeric_df = df[

            numeric_cols

        ].copy()

        # Remove constant columns

        numeric_df = numeric_df.loc[

            :,

            numeric_df.nunique()>1

        ]

        # limit columns

        if numeric_df.shape[1] > 10:

            numeric_df = numeric_df.iloc[

                :,

                :10

            ]

        if numeric_df.shape[1] > 1:

            corr = numeric_df.corr()

            fig = px.imshow(

                corr,

                text_auto=".2f",

                color_continuous_scale="RdBu",

                zmin=-1,

                zmax=1,

                aspect="equal",

                title="Correlation Heatmap"

            )

            fig.update_layout(

                height=650,

                width=650

            )

            plots['correlation']=fig

    #########################################
    # Top Categories
    #########################################

    if len(categorical_cols)>0:

        col = categorical_cols[0]

        top_values = (

            df[col]

            .astype(str)

            .value_counts()

            .head(10)

        )

        plots['top_category']=px.bar(

            x=top_values.index,

            y=top_values.values,

            title=f"Top Categories: {col}",

            labels={

                "x":col,

                "y":"Count"

            }

        )

    return plots