import streamlit as st
import google.generativeai as palm

# API Key
API_KEY = "AIzaSyDUh4QRN36e67k5_dVXgxdAuzpWPOdBPKU"

st.set_page_config(
    page_title="AI Chatbot",
    page_icon="👽",
    layout="centered",
)

# --- Enhanced Styling ---
st.markdown(
    """
    <style>
    body {
        font-family: 'Roboto', sans-serif;
        background: linear-gradient(to right, #eef2f3, #8e9eab);
        color: #2c3e50;
    }
    .main-header {
        text-align: center;
        font-size: 3.5rem;
        font-weight: 700;
        color: #2c3e50;
        margin-bottom: 15px;
    }
    .input-area, .response-box {
        padding: 20px;
        background: #ffffff;
        border-radius: 12px;
        border: 2px solid #3498db;
        box-shadow: 0 6px 12px rgba(0,0,0,0.1);
        transition: transform 0.2s;
    }
    .input-area:hover, .response-box:hover {
        transform: translateY(-4px);
    }
    .btn-generate {
        background-color: #4CAF50;
        color: white;
        padding: 12px 20px;
        border-radius: 10px;
        transition: 0.3s;
    }
    .btn-generate:hover {
        background-color: #2e7d32;
        transform: scale(1.05);
    }
    .response-box pre {
        font-family: 'Courier New', monospace;
        background-color: #f4f4f4;
        padding: 12px;
        border-radius: 8px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# --- Header ---
st.markdown('<h1 class="main-header">👾 AI Chatbot To Analyze Code</h1>', unsafe_allow_html=True)
st.markdown('<p style="text-align:center;">Analyze code and receive AI-powered insights!</p>', unsafe_allow_html=True)

# --- Input Area ---
user_input = st.text_area(
    "Paste your code or describe the issue:",
    placeholder="Describe the error or paste your code...",
    height=180
)

# --- Generate Response ---
if st.button("🚀 Generate Response", use_container_width=True):
    if user_input.strip():
        try:
            palm.configure(api_key=API_KEY)
            model = palm.GenerativeModel(
                model_name="gemini-2.0-flash-thinking-exp",
                system_instruction="You are a code analyzer. Provide solutions and explanations."
            )
            response = model.generate_content(user_input)
            
            if response and hasattr(response, "text"):
                st.markdown('<div class="response-box">', unsafe_allow_html=True)
                st.markdown("### ✨ AI Response:")
                st.code(response.text, language="python")
                st.markdown('</div>', unsafe_allow_html=True)
            else:
                st.error("Failed to get a response. Please retry.")
        except Exception as e:
            st.error(f"Error: {e}")
    else:
        st.warning("Please enter a prompt!")
