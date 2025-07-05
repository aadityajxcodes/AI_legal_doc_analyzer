# app.py
import streamlit as st
import requests
from helper import extract_text
from dotenv import load_dotenv
import os

load_dotenv()
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
model="mistralai/mistral-7b-instruct"




# Function to send prompt to OpenRouter
# def ask_openrouter(prompt, model="mistral/mistral-7b-instruct"):
#     headers = {
#         "Authorization": f"Bearer {OPENROUTER_API_KEY}",
#         "Content-Type": "application/json",
#         "HTTP-Referer": "https://yourdomain.com",  # Replace with your site or GitHub
#         "X-Title": "Legal Document Analyzer"
#     }
#     data = {
#         "model": model,
#         "messages": [
#             {"role": "user", "content": prompt}
#         ]
#     }
#     response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=data)
#     response.raise_for_status()
#     return response.json()["choices"][0]["message"]["content"]

def ask_openrouter(prompt, model="mistralai/mistral-7b-instruct"):
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json",
        "HTTP-Referer": "https://github.com/aadityajxcodes/legal-doc-analyzer",  # ✅ Required
        "X-Title": "Legal Document Analyzer"
    }
    data = {
        "model": model,
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }
    response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=data)
    
    # Check response content if error
    if response.status_code != 200:
        st.error(f"⚠️ OpenRouter Error: {response.status_code} - {response.text}")
        return "Request failed"

    return response.json()["choices"][0]["message"]["content"]

# --- Streamlit UI ---
st.set_page_config(page_title="🧾 Legal Document Analyzer", layout="wide")
st.title("🧾 AI-Powered Legal Document Analyzer")

uploaded_file = st.file_uploader("📂 Upload a legal document (PDF, DOCX, or TXT)", type=["pdf", "docx", "txt"])

if uploaded_file:
    with st.spinner("Extracting text..."):
        text = extract_text(uploaded_file)
    st.subheader("📜 Extracted Text (Preview)")
    st.text_area("Text", text[:3000], height=250)  # Preview only

    # Summarization
    if st.button("🧠 Summarize Document"):
        with st.spinner("Summarizing via OpenRouter..."):
            prompt = f"Summarize the following legal document in simple terms:\n\n{text}"
            summary = ask_openrouter(prompt)
            st.subheader("📝 Summary")
            st.write(summary)

    # Q&A
    user_question = st.text_input("❓ Ask a question about this document")
    if user_question:
        with st.spinner("Thinking..."):
            prompt = f"Given this legal document:\n\n{text}\n\nAnswer the question: {user_question}"
            answer = ask_openrouter(prompt)
            st.subheader("🗣️ Answer")
            st.write(answer)
