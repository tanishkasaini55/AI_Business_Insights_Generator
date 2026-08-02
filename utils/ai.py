import os
from dotenv import load_dotenv
from groq import Groq

# Load environment variables
load_dotenv()

# Create Groq client
client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


def generate_ai_insights(df):

    prompt = f"""
    You are a senior business analyst.

    Analyze the following business dataset and provide:

    1. Top 5 Business Insights
    2. Best Performing Region
    3. Best Selling Item Type
    4. Sales Trend Analysis
    5. Business Recommendations

    Dataset:

    {df.head(20).to_string()}
    """

    completion = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.5,
        max_tokens=700
    )

    return completion.choices[0].message.content

