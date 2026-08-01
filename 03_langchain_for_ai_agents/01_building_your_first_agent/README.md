# Practical 01: Building Your First Agent using LangChain

## Overview
Demonstrates creating an AI agent with custom python tools (`multiply`, `divide`) powered by Groq's `llama-3.3-70b-versatile` model.

---

## How to Run

From the root directory of the project:

```powershell
python 03_langchain_for_ai_agents/01_building_your_first_agent/main.py
```

---

## Troubleshooting & Issue Log

During this practical, three major issues were encountered and resolved with Gemini AI assistance:

### 1. PowerShell Environment Activation Error
* **Error Log:**
  ```text
  source : The term 'source' is not recognized as the name of a cmdlet, function, script file, or operable program.
  ```
* **Cause:** The course slide showed Linux/Mac syntax (`source .../bin/activate`), whereas the execution environment is Windows PowerShell.
* **Fix:** Activated using PowerShell syntax:
  ```powershell
  .\langchain-env\Scripts\Activate.ps1
  ```

---

### 2. Windows Application Control Blocking `pip.exe`
* **Error Log:**
  ```text
  Program 'pip.exe' failed to run: An Application Control policy has blocked this file
  ```
* **Cause:** Windows Security blocked direct execution of newly created `.exe` binaries inside local user directories.
* **Fix:** Invoked pip directly through the trusted Python executable:
  ```powershell
  python -m pip install langchain langchain-groq python-dotenv
  ```

---

### 3. Agent Key Typo (`groq.BadRequestError: 400`)
* **Error Log:**
  ```text
  groq.BadRequestError: Error code: 400 - {'error': {'message': "'messages' : minimum number of items is 1", 'type': 'invalid_request_error'}}
  ```
* **Cause:** Called `agent.invoke({"message": [...]})` with singular `"message"`. LangChain agent state requires plural `"messages"`.
* **Fix:** Updated the invoke payload key:
  ```python
  result = agent.invoke({
      "messages": [("user", "What is 15 multiplied by 8, then divided by 3?")]
  })
  ```

---

## Successful Execution Output

```text
The result of 15 multiplied by 8 is 120. Then, dividing 120 by 3 results in 40.
```