"""
Lesson: Your First API Call (Groq Equivalent)
==============================================
Adapted from OpenAI Responses API to work with Groq & Llama 3.3.

Before running:
    python -m pip install groq
"""

import os
from dotenv import load_dotenv
from groq import Groq

# 1. Load your GROQ_API_KEY from the .env file
load_dotenv()

# 2. Create the Groq client (reads GROQ_API_KEY automatically)
client = Groq()

# --------------------------------------------------
# Part 1: Simple API Call
# --------------------------------------------------

response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[{
        "role": "user",
        "content": "Explain what an AI agent is in one paragraph.",
    }],
)

print("=" * 60)
print("RESPONSE:")
print("=" * 60)
print(response.choices[0].message.content)
print()

# --------------------------------------------------
# Part 2: Call with System Instructions
# --------------------------------------------------

response2 = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {
            "role": "system",
            "content": "You are a helpful teacher who explains things simply.",
        },
        {
            "role": "user",
            "content": "What is the difference between an agent and a chatbot?",
        },
    ],
)

print("=" * 60)
print("RESPONSE WITH INSTRUCTIONS:")
print("=" * 60)
print(response2.choices[0].message.content)