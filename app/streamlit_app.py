import streamlit as st
import joblib
import os
import re

# -----------------------------
# PATH SETTINGS (IMPORTANT)
# -----------------------------
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

model_path = os.path.join(BASE_DIR, "models", "ticket_model.pkl")
vectorizer_path = os.path.join(BASE_DIR, "models", "vectorizer.pkl")

model = joblib.load(model_path)
vectorizer = joblib.load(vectorizer_path)

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(
    page_title="Support Ticket Classifier",
    page_icon="🎧",
    layout="wide"
)

# -----------------------------
# TITLE
# -----------------------------
st.title("🎧 AI Support Ticket Classification System")
st.write(
"""
Automatically classify customer tickets and assign priority levels  
to help support teams respond faster and smarter.
"""
)

st.divider()

# -----------------------------
# TEXT CLEANING FUNCTION
# -----------------------------
def clean_text(text):
    text = re.sub(r'[^a-zA-Z]', ' ', text)
    text = text.lower()
    return text

# -----------------------------
# PRIORITY LOGIC
# -----------------------------
def assign_priority(text):
    urgent_words = ['urgent','immediately','asap','refund','cancel','not working','error','failed']

    for word in urgent_words:
        if word in text:
            return "🔴 High"

    if len(text.split()) > 20:
        return "🟠 Medium"

    return "🟢 Low"

# -----------------------------
# INPUT AREA
# -----------------------------
st.subheader("Enter Customer Support Ticket")

ticket_text = st.text_area(
    "Ticket Message",
    placeholder="Example: My payment failed but money was deducted. Please resolve immediately.",
    height=150
)

# -----------------------------
# PREDICTION BUTTON
# -----------------------------
if st.button("Classify Ticket", use_container_width=True):

    if ticket_text.strip() == "":
        st.warning("Please enter a ticket message.")
    else:

        cleaned = clean_text(ticket_text)

        vectorized = vectorizer.transform([cleaned])

        category = model.predict(vectorized)[0]

        priority = assign_priority(cleaned)

        st.divider()

        # KPI STYLE OUTPUT
        col1, col2 = st.columns(2)

        col1.metric("Predicted Category", category)
        col2.metric("Priority Level", priority)

        st.success("Ticket classified successfully!")

# -----------------------------
# SIDEBAR (Makes app look premium)
# -----------------------------
st.sidebar.header("About This Model")

st.sidebar.write("""
**Model Used:** Logistic Regression  
**Vectorization:** TF-IDF  

This AI system helps businesses:

✅ Reduce manual ticket sorting  
✅ Improve response time  
✅ Detect urgent issues faster  
✅ Increase customer satisfaction  
""")

st.sidebar.info("Built with Scikit-learn & Streamlit")
