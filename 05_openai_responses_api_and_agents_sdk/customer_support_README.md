# 🚀 Complete Project: Multi-Agent Customer Support System

This project demonstrates a production-grade AI architecture using a multi-agent system. Instead of relying on a single Large Language Model (LLM) to handle everything, the workload is distributed across specialized agents.

## 🧠 Core Architecture Learned

### 1. The Triage Agent (The Router)
The **Triage Agent** serves as the front door. It doesn't answer questions directly. Instead, its only job is to understand the user's intent and trigger a **handoff** to the correct Specialist Agent.

### 2. Specialist Agents (The Workers)
Each specialist has a narrow focus and specific tools, reducing the chance of AI hallucinations:
* **Order Status Agent:** Given access to a local Python function tool (`lookup_order`) to query a simulated database.
* **Refund Agent:** Given access to a transactional tool (`process_refund`) that can modify data.
* **FAQ Agent:** Given access to an external `WebSearchTool()` to pull real-time policy data.

### 3. Input Guardrails (The Bouncer)
We implemented an `@input_guardrail` that runs *before* the Triage Agent even sees the message. 
* It uses a secondary, smaller LLM agent to analyze the text.
* It uses **Pydantic Structured Output** (`SupportCheck`) to force the LLM to reply with a strict `True` or `False` JSON response.
* If the user asks for a joke or coding help, the guardrail triggers a tripwire and blocks the request instantly, saving processing time and API costs.

## 🛠️ Key Takeaway
Building robust AI systems requires **orchestration**. By combining routing (Triage), safety (Guardrails), and execution (Specialists with Tools), we create an AI system that is safe, predictable, and highly capable!