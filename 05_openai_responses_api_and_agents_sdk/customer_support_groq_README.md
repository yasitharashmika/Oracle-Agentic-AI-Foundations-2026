# 🚀 Complete Project: Customer Support System (Groq & LangChain)

This script is a functional adaptation of the course's final multi-agent project. Because the course utilized an experimental OpenAI-specific SDK (`agents`), we re-engineered the architecture to work with open-source tools: **LangChain**, **Groq API**, and **Llama 3.3 (70B)**.

## 🧠 Core Architecture Learned & Adapted

### 1. The Guardrail (Security Check)
Before the main AI ever sees the prompt, we pass the user's message through a `guardrail_check()`. This is a strict, isolated LLM call that returns a boolean (`True/False`). 
* **Benefit:** If a user asks for coding advice or tells a joke, the script stops instantly. This prevents prompt injection, saves API tokens, and ensures the agent stays on-topic.

### 2. The Triage Logic (`bind_tools`)
Instead of a rigid handoff list, we utilize LangChain's `bind_tools()` method. The LLM acts as the **Triage Agent**. It reads the user prompt, looks at the available tools (`lookup_order`, `process_refund`), and intelligently decides which tool is required.

### 3. Specialist Execution (Tool Invocation)
When the Triage LLM selects a tool, the script executes the local Python function (acting as our "Specialist Agents"). The raw data returned by the database is fed back to the LLM so it can formulate a polite, natural-language response for the customer.

## 🛠️ Key Takeaway
We successfully proved that the *conceptual architecture* taught in the course (Guardrails $\rightarrow$ Triage $\rightarrow$ Execution) is universal. By understanding the logic, we were able to rebuild it entirely outside of the OpenAI ecosystem using LangChain!
