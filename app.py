# # app.py
# import streamlit as st
# import requests
# from helper import extract_text
# from dotenv import load_dotenv
# import os
# from helper import export_to_docx


# load_dotenv()
# OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
# model="mistralai/mistral-7b-instruct"




# # Function to send prompt to OpenRouter
# # def ask_openrouter(prompt, model="mistral/mistral-7b-instruct"):
# #     headers = {
# #         "Authorization": f"Bearer {OPENROUTER_API_KEY}",
# #         "Content-Type": "application/json",
# #         "HTTP-Referer": "https://yourdomain.com",  # Replace with your site or GitHub
# #         "X-Title": "Legal Document Analyzer"
# #     }
# #     data = {
# #         "model": model,
# #         "messages": [
# #             {"role": "user", "content": prompt}
# #         ]
# #     }
# #     response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=data)
# #     response.raise_for_status()
# #     return response.json()["choices"][0]["message"]["content"]

# def ask_openrouter(prompt, model="mistralai/mistral-7b-instruct"):
#     headers = {
#         "Authorization": f"Bearer {OPENROUTER_API_KEY}",
#         "Content-Type": "application/json",
#         "HTTP-Referer": "https://github.com/aadityajxcodes/legal-doc-analyzer",  # ✅ Required
#         "X-Title": "Legal Document Analyzer"
#     }
#     data = {
#         "model": model,
#         "messages": [
#             {"role": "user", "content": prompt}
#         ]
#     }
#     response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=data)
    
#     # Check response content if error
#     if response.status_code != 200:
#         st.error(f"⚠️ OpenRouter Error: {response.status_code} - {response.text}")
#         return "Request failed"

#     return response.json()["choices"][0]["message"]["content"]

# # --- Streamlit UI ---
# st.set_page_config(page_title="🧾 Legal Document Analyzer", layout="wide")
# st.title("🧾 AI-Powered Legal Document Analyzer")

# uploaded_file = st.file_uploader("📂 Upload a legal document (PDF, DOCX, or TXT)", type=["pdf", "docx", "txt"])

# if uploaded_file:
#     with st.spinner("Extracting text..."):
#         text = extract_text(uploaded_file)
#     st.subheader("📜 Extracted Text (Preview)")
#     st.text_area("Text", text[:3000], height=250)  # Preview only

#     # Summarization
#     if st.button("🧠 Summarize Document"):
#         with st.spinner("Summarizing via OpenRouter..."):
#             prompt = f"Summarize the following legal document in simple terms:\n\n{text}"
#             summary = ask_openrouter(prompt)
#             st.subheader("📝 Summary")
#             st.write(summary)

#     # Q&A
#     user_question = st.text_input("❓ Ask a question about this document")
#     if user_question:
#         with st.spinner("Thinking..."):
#             prompt = f"Given this legal document:\n\n{text}\n\nAnswer the question: {user_question}"
#             answer = ask_openrouter(prompt)
#             st.subheader("🗣️ Answer")
#             st.write(answer)



# # app.py
# import streamlit as st
# import requests
# import os
# from dotenv import load_dotenv
# from helper import extract_text, export_to_docx

# # Load API key
# load_dotenv()
# OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
# model = "mistralai/mistral-7b-instruct"

# # Function to query OpenRouter
# def ask_openrouter(prompt, model="mistralai/mistral-7b-instruct"):
#     headers = {
#         "Authorization": f"Bearer {OPENROUTER_API_KEY}",
#         "Content-Type": "application/json",
#         "HTTP-Referer": "https://github.com/aadityajxcodes/legal-doc-analyzer",  # required
#         "X-Title": "Legal Document Analyzer"
#     }
#     data = {
#         "model": model,
#         "messages": [
#             {"role": "user", "content": prompt}
#         ]
#     }
#     response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=data)

#     if response.status_code != 200:
#         st.error(f"⚠️ OpenRouter Error: {response.status_code} - {response.text}")
#         return "Request failed"

#     return response.json()["choices"][0]["message"]["content"]

# # Streamlit UI
# st.set_page_config(page_title="🧾 Legal Document Analyzer", layout="wide")
# st.title("🧾 AI-Powered Legal Document Analyzer")

# uploaded_file = st.file_uploader("📂 Upload a legal document (PDF, DOCX, or TXT)", type=["pdf", "docx", "txt"])

# if uploaded_file:
#     with st.spinner("Extracting text..."):
#         text = extract_text(uploaded_file)

#     st.subheader("📜 Extracted Text (Preview)")
#     st.text_area("Text", text[:3000], height=250)

#     summary = ""
#     qa_list = []

#     if st.button("🧠 Summarize Document"):
#         with st.spinner("Summarizing via OpenRouter..."):
#             prompt = f"Summarize the following legal document in simple terms:\n\n{text}"
#             summary = ask_openrouter(prompt)
#             st.subheader("📝 Summary")
#             st.write(summary)

#     user_question = st.text_input("❓ Ask a question about this document")
#     if user_question:
#         with st.spinner("Thinking..."):
#             prompt = f"Given this legal document:\n\n{text}\n\nAnswer the question: {user_question}"
#             answer = ask_openrouter(prompt)
#             st.subheader("🗣️ Answer")
#             st.write(answer)
#             qa_list.append(answer)  # Append to QA list

#     # Export to DOCX
#     if st.button("📄 Export Summary & Q&A to Word (.docx)"):
#         if not summary:
#             st.warning("Please generate a summary before exporting.")
#         else:
#             export_path = export_to_docx(summary, qa_list)
#             with open(export_path, "rb") as file:
#                 st.download_button(
#                     label="📥 Download File",
#                     data=file,
#                     file_name="legal_summary.docx",
#                     mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
#                 )



# import streamlit as st
# import requests
# from helper import extract_text, export_to_docx
# from dotenv import load_dotenv
# import os

# import spacy
# nlp = spacy.load("en_core_web_sm")


# load_dotenv()
# OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
# model = "mistralai/mistral-7b-instruct"

# # Function to send prompt to OpenRouter
# def ask_openrouter(prompt, model="mistralai/mistral-7b-instruct"):
#     headers = {
#         "Authorization": f"Bearer {OPENROUTER_API_KEY}",
#         "Content-Type": "application/json",
#         "HTTP-Referer": "https://github.com/aadityajxcodes/legal-doc-analyzer",  # ✅ Required
#         "X-Title": "Legal Document Analyzer"
#     }
#     data = {
#         "model": model,
#         "messages": [
#             {"role": "user", "content": prompt}
#         ]
#     }
#     response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=data)
    
#     if response.status_code != 200:
#         st.error(f"⚠️ OpenRouter Error: {response.status_code} - {response.text}")
#         return "Request failed"

#     return response.json()["choices"][0]["message"]["content"]

# # --- Streamlit UI ---
# st.set_page_config(page_title="🧾 Legal Document Analyzer", layout="wide")
# st.title("🧾 AI-Powered Legal Document Analyzer")

# uploaded_file = st.file_uploader("📂 Upload a legal document (PDF, DOCX, or TXT)", type=["pdf", "docx", "txt"])

# if uploaded_file:
#     with st.spinner("Extracting text..."):
#         text = extract_text(uploaded_file)
#     st.subheader("📜 Extracted Text (Preview)")
#     st.text_area("Text", text[:3000], height=250)  # Preview only

#     # Summarization
#     if st.button("🧠 Summarize Document"):
#         with st.spinner("Summarizing via OpenRouter..."):
#             prompt = f"Summarize the following legal document in simple terms:\n\n{text}"
#             summary = ask_openrouter(prompt)
#             st.session_state.summary = summary  # ✅ Store in session
#             st.subheader("📝 Summary")
#             st.write(summary)

#     # Q&A
#     user_question = st.text_input("❓ Ask a question about this document")
#     if user_question:
#         with st.spinner("Thinking..."):
#             prompt = f"Given this legal document:\n\n{text}\n\nAnswer the question: {user_question}"
#             answer = ask_openrouter(prompt)
#             if "qa_list" not in st.session_state:
#                 st.session_state.qa_list = []
#             st.session_state.qa_list.append(f"Q: {user_question}\nA: {answer}")
#             st.subheader("🗣️ Answer")
#             st.write(answer)

#     # Export to Word
#     if st.button("📄 Export Summary & Q&A to Word (.docx)"):
#         if "summary" not in st.session_state or not st.session_state.summary:
#             st.warning("Please generate a summary before exporting.")
#         else:
#             filename = export_to_docx(
#                 st.session_state.summary,
#                 st.session_state.get("qa_list", []),
#                 "Legal_Summary.docx"
#             )
#             with open(filename, "rb") as f:
#                 st.download_button(
#                     label="⬇️ Download Word File",
#                     data=f,
#                     file_name=filename,
#                     mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
#                 )


# import streamlit as st
# import requests
# from dotenv import load_dotenv
# from helper import extract_text, export_to_docx
# import os
# import spacy

# # Load environment variables
# load_dotenv()
# OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

# # Load spaCy model for NER
# nlp = spacy.load("en_core_web_sm")

# # Streamlit config
# st.set_page_config(page_title="🧾 Legal Document Analyzer", layout="wide")
# st.title("🧾 AI-Powered Legal Document Analyzer")

# # OpenRouter LLM function
# def ask_openrouter(prompt, model="mistralai/mistral-7b-instruct"):
#     headers = {
#         "Authorization": f"Bearer {OPENROUTER_API_KEY}",
#         "Content-Type": "application/json",
#         "HTTP-Referer": "https://github.com/aadityajxcodes/legal-doc-analyzer",
#         "X-Title": "Legal Document Analyzer"
#     }
#     data = {
#         "model": model,
#         "messages": [{"role": "user", "content": prompt}]
#     }
#     response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=data)
#     if response.status_code != 200:
#         st.error(f"⚠️ OpenRouter Error: {response.status_code} - {response.text}")
#         return "Request failed"
#     return response.json()["choices"][0]["message"]["content"]

# # Named Entity Recognition
# def extract_named_entities(text):
#     doc = nlp(text)
#     return [(ent.text, ent.label_) for ent in doc.ents]

# # File uploader
# uploaded_file = st.file_uploader("📂 Upload a legal document (PDF, DOCX, or TXT)", type=["pdf", "docx", "txt"])

# if uploaded_file:
#     with st.spinner("🔍 Extracting text..."):
#         text = extract_text(uploaded_file)

#     st.subheader("📜 Extracted Text (Preview)")
#     st.text_area("Text", text[:3000], height=250)

#     summary = ""
#     qa_list = []

#     if st.button("🧠 Summarize Document"):
#         with st.spinner("Summarizing via OpenRouter..."):
#             prompt = f"Summarize the following legal document in simple terms:\n\n{text}"
#             summary = ask_openrouter(prompt)
#             st.subheader("📝 Summary")
#             st.write(summary)

#     user_question = st.text_input("❓ Ask a question about this document")
#     if user_question:
#         with st.spinner("Thinking..."):
#             prompt = f"Given this legal document:\n\n{text}\n\nAnswer the question: {user_question}"
#             answer = ask_openrouter(prompt)
#             qa_list.append((user_question, answer))
#             st.subheader("🗣️ Answer")
#             st.write(answer)

#     if st.button("🔍 Extract Named Entities"):
#         with st.spinner("Extracting entities..."):
#             entities = extract_named_entities(text)
#             st.subheader("📌 Named Entities Found")
#             if entities:
#                 for ent_text, ent_label in entities:
#                     st.markdown(f"- **{ent_text}** *(type: {ent_label})*")
#             else:
#                 st.info("No named entities found.")

#     # Export to docx
#     if st.button("📄 Export Summary & Q&A to Word (.docx)"):
#         if summary:
#             export_to_docx(summary, qa_list)
#             st.success("📄 Exported successfully! Check the generated .docx file.")
#         else:
#             st.warning("Please generate a summary before exporting.")





# import streamlit as st
# import requests
# from helper import extract_text, export_to_docx, extract_named_entities
# from dotenv import load_dotenv
# import os
# from helper import check_document_authenticity

# load_dotenv()
# OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
# model = "mistralai/mistral-7b-instruct"

# # Send prompt to OpenRouter API
# def ask_openrouter(prompt, model="mistralai/mistral-7b-instruct"):
#     headers = {
#         "Authorization": f"Bearer {OPENROUTER_API_KEY}",
#         "Content-Type": "application/json",
#         "HTTP-Referer": "https://github.com/aadityajxcodes/legal-doc-analyzer",
#         "X-Title": "Legal Document Analyzer"
#     }
#     data = {
#         "model": model,
#         "messages": [
#             {"role": "user", "content": prompt}
#         ]
#     }
#     response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=data)
#     if response.status_code != 200:
#         st.error(f"⚠️ OpenRouter Error: {response.status_code} - {response.text}")
#         return "Request failed"
#     return response.json()["choices"][0]["message"]["content"]


# def detect_fake_clauses(text, max_clauses=5):
#     clauses = [p.strip() for p in text.split("\n") if len(p.strip()) > 50]
#     flagged_clauses = []

#     for clause in clauses[:max_clauses]:  # Limit for performance
#         prompt = f"""You are a legal assistant.
# Analyze the following legal clause and tell if it's fake, suspicious, vague, or unrealistic. 
# Also explain briefly why, if it is:
# Clause: \"\"\"{clause}\"\"\"
# """
#         response = ask_openrouter(prompt)
#         if "suspicious" in response.lower() or "fake" in response.lower() or "vague" in response.lower():
#             flagged_clauses.append((clause, response.strip()))

#     return flagged_clauses

# # --- Streamlit UI ---
# # st.set_page_config(page_title="🧾 Legal Document Analyzer", layout="wide")
# st.set_page_config(page_title="⚖️ LawLens | AI Legal Analyzer", layout="wide")

# st.title("⚖️ LawLens — AI Legal Document Analyzer")
# st.caption("🔍 Understand complex legal documents with the power of AI.")


# # Session states
# if "summary" not in st.session_state:
#     st.session_state.summary = ""
# if "qa_list" not in st.session_state:
#     st.session_state.qa_list = []

# uploaded_file = st.file_uploader("📂 Upload a legal document (PDF, DOCX, or TXT)", type=["pdf", "docx", "txt"])

# if uploaded_file:
#     with st.spinner("Extracting text..."):
#         text = extract_text(uploaded_file)

#     st.subheader("📜 Extracted Text (Preview)")
#     st.text_area("Text", text[:3000], height=250)

#     # --- Summarize ---
#     if st.button("🧠 Summarize Document"):
#         with st.spinner("Summarizing via OpenRouter..."):
#             prompt = f"Summarize the following legal document in simple terms:\n\n{text}"
#             summary = ask_openrouter(prompt)
#             st.session_state.summary = summary
#             st.subheader("📝 Summary")
#             st.write(summary)

#     # --- Question Answering ---
#     user_question = st.text_input("❓ Ask a question about this document")
#     if user_question:
#         with st.spinner("Thinking..."):
#             prompt = f"Given this legal document:\n\n{text}\n\nAnswer the question: {user_question}"
#             answer = ask_openrouter(prompt)
#             st.session_state.qa_list.append((user_question, answer))
#             st.subheader("🗣️ Answer")
#             st.write(answer)

#     # --- Named Entities ---
#     if st.button("🔍 Extract Named Entities"):
#         with st.spinner("Extracting entities..."):
#             entities = extract_named_entities(text)
#             st.subheader("📌 Named Entities Found")
#             if entities:
#                 for ent_text, ent_label in entities:
#                     st.markdown(f"- **{ent_text}** *(type: {ent_label})*")
#             else:
#                 st.info("No named entities found.")

#     # --- Export to Word ---
#     st.markdown("---")
#     if st.button("📄 Export Summary & Q&A to Word (.docx)"):
#         if st.session_state.summary:
#             export_to_docx(st.session_state.summary, st.session_state.qa_list)
#             with open("Legal_Summary.docx", "rb") as f:
#                 st.download_button(
#                     label="⬇️ Download Legal_Summary.docx",
#                     data=f,
#                     file_name="Legal_Summary.docx",
#                     mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
#                 )
#         else:
#             st.warning("⚠️ Please generate a summary before exporting.")

#     # --- Document Authenticity Check ---
#     if st.button("🛡️ Check Document Authenticity"):
#         with st.spinner("Analyzing metadata..."):
#             metadata = check_document_authenticity(uploaded_file)
#             if metadata:
#                 st.subheader("📄 Document Metadata")
#                 for k, v in metadata.items():
#                     st.write(f"**{k.capitalize()}**: {v}")
#             else:
#                 st.warning("No metadata found or unsupported format.")



#     # --- Fake Clause Detection ---
#     if st.button("🚨 Run Fake Clause Detector"):
#         with st.spinner("Analyzing clauses with LLM..."):
#             flagged = detect_fake_clauses(text)
#             st.subheader("🚩 Flagged Clauses")
#             if flagged:
#                 for clause, reason in flagged:
#                     st.markdown(f"**Clause:** {clause}")
#                     st.markdown(f"🧠 **LLM Feedback:** {reason}")
#                     st.markdown("---")
#             else:
#                 st.success("✅ No suspicious clauses detected.")

# # --- End of Streamlit UI ---


import streamlit as st
import requests
from helper import extract_text, export_to_docx, extract_named_entities
from dotenv import load_dotenv
import os
from PIL import Image


import base64
from io import BytesIO

def logo_to_base64(img):
    buf = BytesIO()
    img.save(buf, format="PNG")
    byte_im = buf.getvalue()
    return base64.b64encode(byte_im).decode()



load_dotenv()
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
model = "mistralai/mistral-7b-instruct"

# --- LLM Request ---
def ask_openrouter(prompt, model="mistralai/mistral-7b-instruct"):
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json",
        "HTTP-Referer": "https://github.com/aadityajxcodes/legal-doc-analyzer",
        "X-Title": "LawLens"
    }
    data = {
        "model": model,
        "messages": [{"role": "user", "content": prompt}]
    }
    response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=data)
    if response.status_code != 200:
        st.error(f"⚠️ OpenRouter Error: {response.status_code} - {response.text}")
        return "Request failed"
    return response.json()["choices"][0]["message"]["content"]

# --- Fake Clause Detection ---
def detect_fake_clauses(text, max_clauses=5):
    clauses = [p.strip() for p in text.split("\n") if len(p.strip()) > 50]
    flagged_clauses = []

    for clause in clauses[:max_clauses]:
        prompt = f"""You are a legal assistant.
Analyze the following legal clause and tell if it's fake, suspicious, vague, or unrealistic. 
Also explain briefly why, if it is:
Clause: \"\"\"{clause}\"\"\"
"""
        response = ask_openrouter(prompt)
        if "suspicious" in response.lower() or "fake" in response.lower() or "vague" in response.lower():
            flagged_clauses.append((clause, response.strip()))

    return flagged_clauses

# --- Streamlit UI ---
st.set_page_config(page_title=" ⚖️ LawLens | AI Legal Analyzer", layout="wide")
# st.title("⚖️ LawLens — AI Legal Document Analyzer")
# st.caption("🔍 Understand complex legal documents with the power of AI.")


from PIL import Image
import base64
from io import BytesIO

def logo_to_base64(img):
    buffer = BytesIO()
    img.save(buffer, format="PNG")
    byte_data = buffer.getvalue()
    base64_str = base64.b64encode(byte_data).decode()
    return base64_str

# Load your logo
logo_img = Image.open("lawlens_logo.png")
logo_base64 = logo_to_base64(logo_img)

# Display logo + heading inline
st.markdown(f"""
    <div style='display: flex; align-items: center; gap: 10px;'>
        <img src="data:image/png;base64,{logo_base64}" width="45">
        <h1 style='margin: 0; color: #FFF;'>LawLens — <span style="font-weight: 400;">AI Legal Document Analyzer</span></h1>
    </div>
""", unsafe_allow_html=True)
st.caption("🔍 Understand complex legal documents with the power of AI.")
# st.markdown("""
# <div style="background-color: #f8f9fa; padding: 15px 25px; border-radius: 8px; margin-top: 10px;">

# 🎯 <strong>Simplify Legal Jargon:</strong> Instantly get simplified summaries of complex legal documents.<br><br>
# 🔍 <strong>Smart Q&A:</strong> Ask any question about the document and get precise AI-powered answers.<br><br>
# 🚨 <strong>Fake Clause Detection:</strong> Identify suspicious or vague clauses using an LLM.<br><br>
# 📄 <strong>Export & Save:</strong> Download the AI summary and answers as a professional `.docx` file.<br><br>
# 🧠 <strong>Named Entity Recognition:</strong> Highlight names, places, laws, organizations and more automatically.

# </div>
# """, unsafe_allow_html=True)



# Session state
if "summary" not in st.session_state:
    st.session_state.summary = ""
if "qa_list" not in st.session_state:
    st.session_state.qa_list = []

uploaded_file = st.file_uploader("📂 Upload a legal document (PDF, DOCX, or TXT)", type=["pdf", "docx", "txt"])

if uploaded_file:
    with st.spinner("Extracting text..."):
        text = extract_text(uploaded_file)

    st.subheader("📜 Extracted Text (Preview)")
    st.text_area("Text", text[:3000], height=250)

    # --- Horizontal Buttons ---
    st.markdown("### ⚙️ Features")
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        if st.button("🧠 Summarize"):
            with st.spinner("Summarizing via OpenRouter..."):
                prompt = f"Summarize the following legal document in simple terms:\n\n{text}"
                summary = ask_openrouter(prompt)
                st.session_state.summary = summary
                st.subheader("📝 Summary")
                st.write(summary)

    with col2:
        if st.button("🚨 Detect Fake Clauses"):
            with st.spinner("Analyzing for suspicious clauses..."):
                flagged = detect_fake_clauses(text)
                st.subheader("🚩 Flagged Clauses")
                if flagged:
                    for clause, reason in flagged:
                        st.markdown(f"**Clause:** {clause}")
                        st.markdown(f"🧠 **LLM Feedback:** {reason}")
                        st.markdown("---")
                else:
                    st.success("✅ No suspicious clauses detected.")

    with col3:
        if st.button("🔍 Named Entities"):
            with st.spinner("Extracting entities..."):
                entities = extract_named_entities(text)
                st.subheader("📌 Named Entities")
                if entities:
                    for ent_text, ent_label in entities:
                        st.markdown(f"- **{ent_text}** *(type: {ent_label})*")
                else:
                    st.info("No named entities found.")

    with col4:
        if st.button("📄 Export Summary"):
            if st.session_state.summary:
                export_to_docx(st.session_state.summary, st.session_state.qa_list)
                with open("Legal_Summary.docx", "rb") as f:
                    st.download_button(
                        label="⬇️ Download .docx",
                        data=f,
                        file_name="Legal_Summary.docx",
                        mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
                    )
            else:
                st.warning("⚠️ Please generate a summary first.")

    # --- Question Answering ---
    st.markdown("---")
    user_question = st.text_input("❓ Ask a question about the document:")
    if user_question:
        with st.spinner("Thinking..."):
            prompt = f"Given this legal document:\n\n{text}\n\nAnswer the question: {user_question}"
            answer = ask_openrouter(prompt)
            st.session_state.qa_list.append((user_question, answer))
            st.subheader("🗣️ Answer")
            st.write(answer)
