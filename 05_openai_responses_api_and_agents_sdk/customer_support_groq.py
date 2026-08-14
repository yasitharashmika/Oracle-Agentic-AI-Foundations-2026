"""
Complete Project: Customer Support System (Groq Adaptation)
===========================================================
This script mimics the multi-agent architecture using standard LangChain and Groq.
Architecture:
  1. Guardrail Check (Blocks non-support questions)
  2. Triage/Tool Calling (LLM decides which tool to route to)
  3. Execution (Runs the Python function and returns the final answer)
"""

import os
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain_core.tools import tool
from langchain_core.messages import SystemMessage, HumanMessage

# Load environment variables
load_dotenv()

# Initialize the Groq model
model = init_chat_model("llama-3.3-70b-versatile", model_provider="groq")

# --------------------------------------------------
# PART 1: Define Custom Tools (Specialists)
# --------------------------------------------------

ORDERS_DB = {
    "ORD-001": {"item": "Wireless Headphones", "status": "Shipped", "eta": "March 22"},
    "ORD-002": {"item": "Python Programming Book", "status": "Delivered", "eta": "March 18"},
}

@tool
def lookup_order(order_id: str) -> str:
    """Look up the status of a customer order by order ID (e.g., ORD-001)."""
    order = ORDERS_DB.get(order_id.upper())
    if order:
        return f"Order {order_id.upper()}: Item: {order['item']}, Status: {order['status']}, ETA: {order['eta']}"
    return f"Order {order_id} not found."

@tool
def process_refund(order_id: str, reason: str) -> str:
    """Process a refund request for a given order ID with a reason."""
    order = ORDERS_DB.get(order_id.upper())
    if not order:
        return f"Cannot process refund: Order {order_id} not found."
    return f"Refund initiated for Order {order_id.upper()}. Reason: {reason}. Money will return in 5-7 days."

# Bind tools to the model so it knows they exist
model_with_tools = model.bind_tools([lookup_order, process_refund])


# --------------------------------------------------
# PART 2: Define the Guardrail
# --------------------------------------------------

def guardrail_check(user_message: str) -> bool:
    """A tiny LLM call that acts as a security guard to block off-topic questions."""
    prompt = (
        "You are a strict security guardrail. Is the following user message about "
        "customer support (e.g., orders, refunds, shipping, FAQs)? "
        "Reply ONLY with the word 'YES' or 'NO'.\n\n"
        f"Message: '{user_message}'"
    )
    response = model.invoke(prompt)
    return "YES" in response.content.upper()


# --------------------------------------------------
# PART 3: The Main Triage System
# --------------------------------------------------

def handle_customer(message: str):
    print(f"👱 Customer: {message}")
    
    # 1. Run Guardrail
    if not guardrail_check(message):
        print("🚫 Guardrail Blocked: This doesn't appear to be a support question.\n" + "="*70)
        return
        
    # 2. Triage / Routing
    system_prompt = SystemMessage(content="You are a helpful customer support triage agent. Use tools to check orders or process refunds. If no tool is needed, just answer politely.")
    messages = [system_prompt, HumanMessage(content=message)]
    
    # Let the model think and decide what to do
    response = model_with_tools.invoke(messages)
    
    # 3. Tool Execution (Specialist Handoff)
    if response.tool_calls:
        for tool_call in response.tool_calls:
            print(f"⚙️  Triage routing to specialist tool: {tool_call['name']}...")
            
            # Execute the correct Python function based on LLM choice
            if tool_call['name'] == 'lookup_order':
                tool_msg = lookup_order.invoke(tool_call)
            elif tool_call['name'] == 'process_refund':
                tool_msg = process_refund.invoke(tool_call)
                
            # Feed the tool's answer back to the LLM
            messages.append(response)
            messages.append(tool_msg)
            
        # Get the final natural language answer
        final_response = model_with_tools.invoke(messages)
        print(f"🤖 Support Agent: {final_response.content}")
    else:
        # No tools needed (General FAQ)
        print(f"🤖 FAQ Agent: {response.content}")
        
    print("=" * 70)


# --------------------------------------------------
# PART 4: Run the Demo
# --------------------------------------------------
if __name__ == "__main__":
    print("=" * 70)
    print(" CUSTOMER SUPPORT AGENT SYSTEM - GROQ ADAPTATION DEMO")
    print("=" * 70)

    # Test 1: Order status
    handle_customer("Where is my order ORD-001?")

    # Test 2: Refund request
    handle_customer("I want a refund for order ORD-002. The book arrived damaged.")

    # Test 3: Off-topic (Should be blocked)
    handle_customer("Can you write a Python script for me?")