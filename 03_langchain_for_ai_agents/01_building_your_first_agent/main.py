from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.chat_models import init_chat_model
from langchain_core.tools import tool

# Load your GROQ_API_KEY from the .env file
load_dotenv()

# Initialize the model
model = init_chat_model("llama-3.3-70b-versatile", model_provider="groq")


# Define the tools with clean docstrings
@tool
def multiply(a: float, b: float) -> float:
  """Multiply two numbers together. Use this tool for multiplication operations."""
  return a * b


@tool
def divide(a: float, b: float) -> float:
  """Divide the first number by the second number. Returns an error string if dividing by zero."""
  if b == 0:
    return "Error: Cannot divide by zero."
  return a / b


# Create the LangChain Agent
agent = create_agent(model, [multiply, divide])

# Run the agent with a prompt testing division by zero
result = agent.invoke({
    "messages": [("user", "What is 10 multiplied by 10, then divided by 100000?")]
})

# 1. Print the full raw dictionary
print("=== FULL AGENT STATE RESULT ===")
print(result)

# 2. Print only the final AI message content
print("\n=== FINAL AI RESPONSE ===")
print(result["messages"][-1].content)