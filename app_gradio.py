import gradio as gr

from data_insights import (
    load_and_clean_csv,
    generate_insights,
    create_visualizations
)

from ai_insights import (
    generate_ai_insights
)


def analyze_csv(file):

    if file is None:

        return (
            "Please upload a CSV file",
            None,
            None,
            None,
            None,
            None,
            None
        )

    try:

        #################################
        # Load Data
        #################################

        df = load_and_clean_csv(
            file.name
        )

        #################################
        # Generate Insights
        #################################

        insights = generate_insights(
            df
        )

        #################################
        # Generate AI Insights
        #################################

        ai_summary = generate_ai_insights(
            insights
        )

        #################################
        # Create Charts
        #################################

        plots = create_visualizations(
            df
        )

        #################################
        # Summary Text
        #################################

        summary = f"""

## ✅ Analysis Complete

**Rows:** {insights['shape'][0]:,}

**Columns:** {insights['shape'][1]}

**Numeric Columns:** {len(insights['numeric_columns'])}

**Categorical Columns:** {len(insights['categorical_columns'])}

"""

        return (

            summary,

            df.head(
                15
            ).to_html(
                classes='table'
            ),

            insights[
                'descriptive_stats'
            ],

            ai_summary,

            plots.get(
                'histogram'
            ),

            plots.get(
                'correlation'
            ),

            plots.get(
                'top_category'
            )

        )

    except Exception as e:

        return (

            f"❌ Error: {str(e)}",

            None,

            None,

            None,

            None,

            None,

            None

        )


###################################################
# Build UI
###################################################

with gr.Blocks(

    title="Auto Data Insights Dashboard"

) as demo:

    gr.Markdown(

"""
# 📊 AI Powered Automated Data Insights Dashboard

Upload a CSV file and automatically generate:

- Dataset profiling
- Statistics
- Visualizations
- AI Generated Insights

"""
    )

    #################################
    # Upload Section
    #################################

    with gr.Row():

        file_input = gr.File(

            label="Upload CSV",

            file_types=[".csv"]

        )

    analyze_btn = gr.Button(

        "🚀 Analyze Data",

        variant="primary"

    )

    #################################
    # Tabs
    #################################

    with gr.Tabs():

        #################################

        with gr.Tab("Summary"):

            summary_output = gr.Markdown()

            preview_table = gr.HTML()

        #################################

        with gr.Tab("Statistics"):

            stats_output = gr.JSON()

        #################################

        with gr.Tab("AI Insights"):

            ai_output = gr.Markdown()

        #################################

        with gr.Tab("Visualizations"):

            plot1 = gr.Plot(
                label="Distribution"
            )

            plot2 = gr.Plot(
                label="Correlation"
            )

            plot3 = gr.Plot(
                label="Categories"
            )

    #################################
    # Button Click
    #################################

    analyze_btn.click(

        fn=analyze_csv,

        inputs=file_input,

        outputs=[

            summary_output,

            preview_table,

            stats_output,

            ai_output,

            plot1,

            plot2,

            plot3

        ]

    )


###################################################
# Launch
###################################################

if __name__ == "__main__":

    demo.launch(

        share=False,

        server_name="127.0.0.1",

        server_port=7860,

        theme=gr.themes.Soft()

    )