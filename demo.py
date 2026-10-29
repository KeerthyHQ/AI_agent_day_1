import os
# pip install python-dotenv
from dotenv import load_dotenv
# pip install openai
from openai import OpenAI
load_dotenv()                 # loads everything from .env

#client = OpenAI()   # reads your API key from the environment

# point the SAME client at Groq instead of OpenAI 
client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1",
)

response = client.chat.completions.create(
    model="openai/gpt-oss-120b",
    messages=[
        {"role": "system", "content": "You are a witty travel guide.provide answer in markdown"},
        {"role": "user",   "content": "Suggest one thing to do in kanchipuram."},
    ],
)
print(response.choices[0].message.content)


# now OpenAI() finds the key automatically — no key in your code 🎉