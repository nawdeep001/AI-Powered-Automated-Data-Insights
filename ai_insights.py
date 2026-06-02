from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(

    api_key=os.getenv(
        "OPENAI_API_KEY"
    ),

    base_url=os.getenv(
        "OPENAI_BASE_URL"
    )

)


def generate_ai_insights(insights):

    prompt = f"""

Dataset Shape:

{insights['shape']}

Numeric Columns:

{insights['numeric_columns']}

Missing Values:

{insights['missing_values']}

Descriptive Stats:

{str(insights['descriptive_stats'])[:2500]}

Generate:

1. Key findings

2. Business insights

3. Risks

4. Recommendations

"""

    response = client.chat.completions.create(

        model="gpt-4o-mini",

        messages=[

            {

                "role":"user",

                "content":prompt

            }

        ]

    )

    return response.choices[
        0
    ].message.content