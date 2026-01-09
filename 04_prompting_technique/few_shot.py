"""
Few-shot prompting me hum model ko 2–5 examples dete hain
taaki model pattern samajh le aur same format me answer de.
"""
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.getenv("GOOGLE_API_KEY"),
    base_url=os.getenv("BASE_URL")
)


response = client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[
        {
            "role": "system",
            "content": "You are a sentiment analysis assistant."
        },
        {
            "role": "user",
            "content": (
                "Text: I love this product\n"
                "Sentiment: Positive\n\n"
                "Text: This app is terrible and slow\n"
                "Sentiment: Negative\n\n"
                "Text: The UI is okay but nothing special\n"
                "Sentiment:"
            )
        }
        
    ],
    temperature=0
)

print(response.choices[0].message.content)


"""
Example 1 — Sentiment Classification (Few-Shot)
Text: I love this app
Sentiment: Positive

Text: The app crashes frequently
Sentiment: Negative

Text: It works fine
Sentiment:


Model almost always returns:
Neutral

✔ Pattern learned
✔ High accuracy

Example 2 — Customer Support Tone Control
User: I was charged twice
Response: I'm sorry for the inconvenience. Let me help you with that.

User: My order is late
Response: I apologize for the delay. I'll check the status for you.

User: My refund is missing
Response:


Model continues in same tone & style.
"""