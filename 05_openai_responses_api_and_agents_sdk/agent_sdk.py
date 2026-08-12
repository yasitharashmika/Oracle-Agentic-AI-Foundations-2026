"""
Lesson: Your First Agent (Groq Equivalent)
===========================================
The Agents SDK concept adapted to run with Groq & Llama 3.3.
Just define an Agent with a model, name, and instructions, then run it.

Before running:
    python -m pip install groq python-dotenv
"""

import os
from dotenv import load_dotenv
from groq import Groq

# Load environment variables (reads GROQ_API_KEY from .env)
load_dotenv()
client = Groq()


# --------------------------------------------------
# Agents SDK Abstraction Wrapper for Groq
# --------------------------------------------------
class Agent:

  def __init__(self, name: str, instructions: str, model: str):
    self.name = name
    self.instructions = instructions
    self.model = model


class RunResult:

  def __init__(self, output: str):
    self.final_output = output


class Runner:

  @staticmethod
  def run_sync(agent: Agent, prompt: str) -> RunResult:
    """Executes the agent request synchronously using the Groq API."""
    response = client.chat.completions.create(
        model=agent.model,
        messages=[
            {"role": "system", "content": agent.instructions},
            {"role": "user", "content": prompt},
        ],
    )
    return RunResult(response.choices[0].message.content)


# --------------------------------------------------
# Step 1: Define an Agent
# --------------------------------------------------
# An Agent needs:
#   - name: a label for identification and tracing
#   - instructions: the system prompt that defines behavior
#   - model: LLM name
agent = Agent(
    name="History Tutor",
    instructions="""You are a friendly history tutor.
You answer history questions clearly and concisely.
Always include an interesting fun fact in your answers.""",
    model="llama-3.3-70b-versatile",
)


# --------------------------------------------------
# Step 2: Run the Agent
# --------------------------------------------------
print("--- Question 1 ---")
result = Runner.run_sync(
    agent, "Who was the first president of the United States?"
)
print(result.final_output)
print()

# Run it again with a different question
print("--- Question 2 ---")
result2 = Runner.run_sync(agent, "What caused World War I?")
print(result2.final_output)
print()

print("✅ You just built and ran your first agent with Groq!")