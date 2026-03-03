# 🎟️ Future ML – Ticket Classification App

A lightweight Streamlit project for classifying customer support tickets using a simple machine‑learning pipeline.  
The app lets users upload a CSV of text tickets and returns predicted categories based on a trained model.

---

## 🗂️ Project Structure

```
.
├── requirements.txt               # Python dependencies
├── app/
│   └── streamlit_app.py          # Main Streamlit interface
├── data/
│   └── customer_support_tickets.csv  # Example dataset
├── models/                       # Saved model artifacts
└── notebooks/
    └── ticket_classification.ipynb  # Exploration & training notebook
```

---

## 🚀 Getting Started

1. **Clone the repo**
   ```bash
   git clone https://github.com/KaluriVamshi16/FUTURE_ML_02.git
   cd FUTURE_ML_02
   ```

2. **Create & activate a virtual environment**
   ```bash
   python -m venv venv
   .\venv\Scripts\Activate.ps1   # Windows PowerShell
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Streamlit app**
   ```bash
   streamlit run app/streamlit_app.py
   ```

5. **Open your browser** at `http://localhost:8501` and start classifying tickets!

---

## 🛠️ What’s Inside

- **streamlit_app.py** – Streamlit UI for uploading data, processing text, and displaying predictions.
- **ticket_classification.ipynb** – Data exploration, preprocessing, model training and evaluation steps.
- **customer_support_tickets.csv** – Sample dataset with text and labels.
- **models** – Directory reserved for serialized model(s) produced during development.
- **requirements.txt** – Lists packages such as `streamlit`, `pandas`, `scikit-learn` etc.

---

## 🧠 Machine Learning Workflow

1. **Load and clean** the CSV data.
2. **Preprocess** text (tokenization, vectorization, etc.).
3. **Train** a classifier (e.g. `LogisticRegression`, `RandomForest`).
4. **Save** the model to models for inference.
5. **Use** the model in Streamlit to predict ticket categories.

Refer to the notebook for detailed code and performance metrics.

---

## 📄 Usage Notes

- The app expects a CSV with a column of ticket text.
- You can adapt preprocessing or swap in a different model by editing the notebook and redeploying.
- Feel free to expand the UI for visualization, logging, or batch processing.

---

## ✅ Future Improvements

- Add model versioning & automatic retraining.
- Deploy to a cloud platform (e.g. Streamlit Cloud, Azure Web App).
- Integrate with a real-time support system via API.

---

## 📜 License

This repository is released under the MIT License.  
Feel free to use, modify, and redistribute!

---
