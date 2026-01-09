"""
Chain-of-thought prompting mein, model ko apne reasoning steps dikhane hote hain
taaki wo complex problems ko solve kar sake.
"""
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.getenv("GOOGLE_API_KEY"),
    base_url=os.getenv("BASE_URL")
)

text = "The app is slow and keeps crashing."

response = client.chat.completions.create(
    model="gemini-2.5-flash",
     messages=[
        {
            "role": "system",
            "content": "Solve problems step by step and explain reasoning."
        },
        {
            "role": "user",
            "content": "A shop sells a pen for $2. If you buy 7 pens, how much do you pay?"
        }
    ],
    temperature=0.3
)

print(response.choices[0].message.content)



