# Module 5: OpenAI Responses API & Agents SDK (Groq Adaptation)

This directory contains practical implementations demonstrating core concepts from **Module 5: OpenAI Responses API and Agents SDK Basics**. 

Because these lessons were originally designed for OpenAI's ecosystem, we adapted them to run seamlessly using **Groq API** and the **Meta Llama 3.3 (70B)** open model.

---

## 📚 What You Learned

1. **Direct Model Completions (`responses_api.py`)**:
   * How to prompt an LLM directly without complex message arrays.
   * How to pass `system` level instructions to guide the personality, depth, and tone of responses.
2. **Agent Abstraction & Personas (`agent_sdk.py`)**:
   * How to build an `Agent` structure with dedicated names, system instructions, and models.
   * How system prompts enforce structural rules (e.g., ensuring a history tutor always provides a fun fact).
   * How a `Runner` class executes agent requests asynchronously or synchronously.

---

## 🤖 Core Concepts: Chatbot vs. AI Agent

Based on the execution outputs from `responses_api.py`:

| Feature | Chatbot | AI Agent |
| :--- | :--- | :--- |
| **Primary Goal** | Conversational interaction and Q&A. | Autonomous goal achievement and task execution. |
| **Logic Type** | Rule-based or single-turn response generation. | Context-aware decision-making and planning. |
| **Capabilities** | Answers questions based on training data. | Executes actions, uses external tools, and calls APIs. |
| **Example** | Answering flight schedules and prices. | Booking a flight, applying loyalty discounts, and reserving a hotel automatically. |

---

## 🔄 Technical Differences: OpenAI Native vs. Groq Adaptation

Because OpenAI's `client.responses.create` API and `openai-agents` SDK are tied to OpenAI's infrastructure, we engineered a custom adaptation for Groq.

| Aspect | OpenAI Course Specification | Groq Adaptation (Our Implementation) |
| :--- | :--- | :--- |
| **Underlying Model** | `gpt-4o` / `gpt-5.5` | `llama-3.3-70b-versatile` |
| **API Endpoint** | `client.responses.create()` | `client.chat.completions.create()` |
| **Agents SDK Support** | Native `openai-agents` library | Custom `Agent` & `Runner` wrapper classes built over `groq` |
| **Inference Speed** | Standard API latency | Ultra-fast LPU inference speeds |
| **Cost** | Paid API credits | Free tier access via Groq API |

---

## 📁 Files in This Directory

* **`responses_api.py`**: Demonstrates simple LLM calls and system-instructed guidance using Groq's Chat Completions API.
* **`agent_sdk.py`**: Implements an `Agent` and `Runner` class architecture to run a "History Tutor" persona using Llama 3.3.

---

## 🚀 How to Run

Ensure your virtual environment is activated and `GROQ_API_KEY` is present in your root `.env` file.

```powershell
# Run the Responses API demonstration
python 05_openai_responses_api_and_agents_sdk/responses_api.py

# Run the Agents SDK demonstration
python 05_openai_responses_api_and_agents_sdk/agent_sdk.py