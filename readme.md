# 🤖 AI System Architect Advisor

**Fault-Tolerant • Multi-LLM • Production-Focused**

A production-ready system design assistant that generates **scalable, secure, and realistic software architecture recommendations** based on real user requirements.

This project is built to demonstrate **real-world backend and system design thinking**, not just AI integration.

---

## 🧠 What This Project Demonstrates

This repository showcases engineering decisions commonly expected in production systems:

* Multi-LLM provider abstraction (no vendor lock-in)
* Graceful handling of API failures and exhausted credits
* Secure backend-only API key management
* Automatic system type detection before AI invocation
* Clean, chat-based UX with predictable behavior

> This is not a chatbot demo. It is a **resilient AI-backed architecture advisory system**.

---

## 🏗️ High-Level Architecture

```
┌─────────────┐
│   User UI   │
│ (Streamlit) │
└──────┬──────┘
       ↓
┌────────────────────┐
│ Requirement Parser │
│ + Architecture     │
│ Type Detection     │
└──────┬─────────────┘
       ↓
┌────────────────────┐
│ Prompt Enhancer    │
│ (Context Injection)│
└──────┬─────────────┘
       ↓
┌─────────────────────────────────────┐
│ AI Provider Router                  │
│                                     │
│ OpenAI → Anthropic → DeepSeek → HF │
│                                     │
│ Automatic fallback on failure       │
└──────┬──────────────────────────────┘
       ↓
┌────────────────────┐
│ Smart Auto Fallback│
│ (Rule-Based Engine)│
└──────┬─────────────┘
       ↓
┌────────────────────┐
│ Final Architecture │
│ Recommendation     │
└────────────────────┘
```

---

## 🔁 AI Provider Fallback Chain

```
OpenAI
   ↓ (credit exhausted / error)
Anthropic
   ↓
DeepSeek
   ↓
Hugging Face
   ↓
Rule-Based Architecture Generator
```

✔ No single point of failure
✔ Predictable behavior
✔ Application remains usable even without AI access

---

## ✨ Key Features

### 🔐 Secure by Design

* API keys are **never exposed** to the frontend
* Credentials managed only via environment variables
* Safe for public deployment

### 🔁 Multi-LLM Provider Support

* Vendor-agnostic AI routing layer
* Easy to extend with new providers
* Prevents dependency on a single AI platform

### 🧠 Architecture Type Auto-Detection

The system analyzes user input to identify patterns such as:

* Real-time systems
* SaaS platforms
* Fintech applications
* AI/ML pipelines
* E-commerce systems
* IoT platforms

This context is injected into prompts **before** calling any AI model, improving output quality.

### ⚠️ Intelligent Credit Failure Handling

When AI credits are unavailable:

* User is informed transparently
* A best-practice architecture response is generated automatically
* The application continues functioning normally

This mirrors real-world fail-safe system behavior.

### 💬 Clean Developer-Focused UX

* Chat-based interface
* Streaming-style responses for better perceived performance
* Provider indicator for transparency
* Conversation history using session state

---

## 🧩 Technology Stack

| Layer           | Technology                                |
| --------------- | ----------------------------------------- |
| UI              | Streamlit                                 |
| Backend Logic   | Python                                    |
| AI Providers    | OpenAI, Anthropic, DeepSeek, Hugging Face |
| Security        | Environment variables                     |
| Design Approach | Modular, fail-safe, provider-agnostic     |

---

## 🔐 Configuration

Set **at least one** AI provider key as an environment variable:

```bash
OPENAI_API_KEY=your_key_here
ANTHROPIC_API_KEY=your_key_here
DEEPSEEK_API_KEY=your_key_here
HF_API_KEY=your_key_here
```

The application automatically detects which providers are available at runtime.

---

## ▶️ Run Locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

---

## 📌 Use Cases

* Early-stage system architecture planning
* System design interview preparation
* MVP to scalable system transitions
* Internal technical reviews
* Architecture consulting demos

---

## 🧠 Engineering Philosophy

* Reliability over novelty
* Fail-safe over fail-fast
* Architecture clarity over AI hype
* Production realism over demos

Every design choice reflects **real backend and system engineering practices**.

---

## 🛣️ Future Enhancements

* Retrieval-Augmented Generation (RAG)

  * PDF-based knowledge ingestion
  * Database schema awareness
  * Internal documentation support
* FastAPI backend separation
* Cost monitoring per AI provider
* Team-based architecture workspaces

---

## 👤 Author

**Shubham R. Chhatre**
Software Engineer | Backend & AI Systems

Focused on building **resilient, production-grade systems**, not just integrations.

---

## ⭐ Why This Project Matters

This project highlights:

* System design thinking
* AI abstraction patterns
* Secure backend practices
* Graceful degradation strategies

If you are reviewing this repository, pay special attention to:

* Provider routing logic
* Fallback mechanisms
* Architecture detection
* Security decisions

That is where the core engineering value lies.
