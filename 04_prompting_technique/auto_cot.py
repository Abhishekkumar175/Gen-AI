"""
Auto-CoT me hum manually reasoning examples nahi likhte
Model khud hi good Chain-of-Thought examples generate karta hai
aur unhi ko use karke problems solve karta hai.
"""
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.getenv("GOOGLE_API_KEY"),
    base_url=os.getenv("BASE_URL")
)

# Step 1: Generate CoT examples
examples = client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[
        {
            "role": "user",
            "content": "Solve these problems step by step:\n1) 6 + 4 * 3\n2) (8 - 2) * 5"
        }
    ],
    temperature=0.2
)

cot_examples = examples.choices[0].message.content

# Step 2: Use generated CoT for new problem
final = client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[
        {"role": "system", "content": "Use the following examples to solve the next problem."},
        {"role": "user", "content": cot_examples},
        {"role": "user", "content": "Solve: 10 + 6 * 2"}
    ],
    temperature=0
    
)

print(final.choices[0].message.content)



