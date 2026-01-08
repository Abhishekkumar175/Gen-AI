"""
System prompt to guide the behavior of a customer support 
agent using Gemini via OpenAI compatibility
"""
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.getenv("GOOGLE_API_KEY"),
    base_url=os.getenv("BASE_URL")
)

# User query (angry customer)
user_message = (
    "Your app charged me twice and nobody is replying to my emails. "
    "This is terrible service!"
)

""""
Build an AI customer support agent that:

Is polite & professional
Apologizes first
Never argues
Gives clear solutions
Stays calm even if user is angry
"""

system_prompt = """You are a professional customer support agent.
Rules:
- Always be polite and empathetic
- Apologize first if the user reports a problem
- Never argue with the user
- Provide clear and actionable solutions
- If you don't know the answer, say so honestly
- Keep responses concise and friendly"""

response = client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[
        {   "role": "system",
            "content": system_prompt
        },
        {
            "role": "user",
            "content": user_message
        }
        
    ],
    temperature=0.3
)

print(response.choices[0].message.content)


"""
example 2 :
Backend API Bot System:_
You are a backend service.
Return responses ONLY in valid JSON.
Never add extra text.
If data is missing, return an error object.

Example 3– Tutor Bot (Education) System:
You are a strict Python tutor.
Explain concepts step by step.
If the student is wrong, correct them.
Never hallucinate.


Result:
Clear explanations
No made-up answers
Teaching style stays consistent
"""
