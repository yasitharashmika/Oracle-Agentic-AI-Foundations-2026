from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain.agents import create_agent
from langchain_core.tools import Tool, tool


# Load your GROQ_API_KEY from the .env file
load_dotenv()


# Initialize the model
model = init_chat_model("llama-3.3-70b-versatile", model_provider="groq")


# Define the tools
@tool
def multiply (a: float, b: float) -> float:
    """Multiply two numbers together.Use for multiplication operations."""
    return a*b

@tool
def divide (a: float, b: float) -> float:
    """Divide the first number by the second number.Returns error if deviding by zero."""
    if b==0:
        return "Error: Can not divide by zero."
    return a/b


#Create the langchain Agent
agent = create_agent(model, [multiply,divide])

#Run the agent with a prompt
result=agent.invoke({"messages": [("user","What is 15 multiplied by 8, then divided by 3?")]})


# 5. Print the output in terminal
print(result)
# ✅ Prints only the final AI message content
print(result["messages"][-1].content)