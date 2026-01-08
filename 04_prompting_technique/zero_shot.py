"""
Zero-shot prompting me model ko koi example nahi diya jata.
Bas task likho → model apni training ke basis par answer deta hai.
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
        {   "role": "system",
            "content": "You are a sentiment analysis assistant."
        },
        {
            "role": "user",
            "content":(
                "Classify the sentiment of the following text "
                "as Positive, Negative, or Neutral:\n\n"
                f"Text: {text}"
            )
        }
        
    ],
    temperature=0
)

print(response.choices[0].message.content)



"""
Example 1 — Simple Explanation
Explain Python generators in simple terms.
Model answers reasonably well → zero-shot success

Example 2— Sentiment Analysis
Classify the sentiment of this text as Positive or Negative:
"I love this product"
No example given → still works.

Example 3 — Customer Support (Zero-Shot)
User: My order hasn’t arrived yet.
Without examples, the model still responds politely (thanks to training + system prompt).
"""