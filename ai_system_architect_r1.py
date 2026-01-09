import os
import time
import requests
import streamlit as st

# =========================
# CONFIG
# =========================
HF_API_URL = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.2"

OPENAI_KEY = os.getenv("OPENAI_API_KEY")
HF_KEY = os.getenv("HF_API_KEY")
ANTHROPIC_KEY = os.getenv("ANTHROPIC_API_KEY")
DEEPSEEK_KEY = os.getenv("DEEPSEEK_API_KEY")

# =========================
# ARCHITECTURE AUTO-DETECT
# =========================
def detect_architecture(user_input: str) -> str:
    text = user_input.lower()

    if "real-time" in text or "chat" in text:
        return "Real-time event-driven architecture with WebSockets"
    if "ecommerce" in text or "payment" in text:
        return "Scalable e-commerce architecture with transactional DB"
    if "ai" in text or "ml" in text:
        return "ML-enabled system with async inference pipelines"
    if "fintech" in text:
        return "Secure fintech architecture with compliance & auditing"
    if "iot" in text:
        return "IoT architecture with message brokers and stream processing"

    return "Modular monolithic architecture suitable for MVP"

# =========================
# SMART MOCK (BACKUP)
# =========================
def smart_mock_response(user_input: str) -> str:
    architecture = detect_architecture(user_input)

    return f"""
## 🧠 Auto-Generated Architecture (Fallback Mode)

**Detected Architecture Type:**  
{architecture}

### Recommended Design
- Modular monolith (MVP friendly)
- Clear domain boundaries
- REST + async background jobs

### Database
- PostgreSQL (ACID, scalable)
- Redis for caching & queues

### Security
- JWT authentication
- Role-Based Access Control
- HTTPS everywhere

### Scalability
- Horizontal scaling
- Stateless services
- Load balancer + CDN

### Risks
- Cost spikes
- Scaling bottlenecks
- Security misconfigurations

---

⚠️ **Credits not enough buddy 😅**  
This response was auto-generated using best-practice rules.

**Your Input:**  
{user_input}
"""

# =========================
# HUGGING FACE CALL
# =========================
def call_huggingface(prompt: str) -> str:
    headers = {
        "Authorization": f"Bearer {HF_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "inputs": prompt,
        "parameters": {"max_new_tokens": 600, "temperature": 0.4}
    }

    response = requests.post(HF_API_URL, headers=headers, json=payload, timeout=60)
    if response.status_code != 200:
        raise Exception("HF failed")

    result = response.json()
    text = result[0]["generated_text"] if isinstance(result, list) else result["generated_text"]
    return text.replace(prompt, "").strip()

# =========================
# PROVIDER ROUTER
# =========================
def generate_response(user_input: str):
    architecture_hint = detect_architecture(user_input)

    prompt = f"""
You are a senior software architect.

System Type:
{architecture_hint}

Analyze:
- Architecture
- Database
- Security
- Scalability
- Risks

System Description:
{user_input}

Respond in clean markdown.
"""

    providers = []

    if OPENAI_KEY:
        providers.append("openai")
    if ANTHROPIC_KEY:
        providers.append("anthropic")
    if DEEPSEEK_KEY:
        providers.append("deepseek")
    if HF_KEY:
        providers.append("huggingface")

    for provider in providers:
        try:
            if provider == "huggingface":
                return call_huggingface(prompt), "Hugging Face"
            # Other providers intentionally skipped (token-safe demo)
        except Exception:
            continue

    return smart_mock_response(user_input), "Auto-Fallback"

# =========================
# STREAMLIT UI (MAX UX)
# =========================
st.set_page_config(
    page_title="AI System Architect Advisor",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 AI System Architect Advisor")
st.caption("Multi-Model • Fail-Safe • Production-Ready")

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

if user_input := st.chat_input("Describe your system requirements..."):
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    with st.chat_message("assistant"):
        with st.spinner("Designing architecture..."):
            response, provider = generate_response(user_input)

            placeholder = st.empty()
            streamed = ""
            for word in response.split():
                streamed += word + " "
                placeholder.markdown(streamed)
                time.sleep(0.015)

            st.caption(f"⚙️ Provider: {provider}")
            st.session_state.messages.append(
                {"role": "assistant", "content": response}
            )
