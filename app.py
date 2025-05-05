import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt

st.set_page_config(page_title="Network Intrusion Detection Visualizer", layout="wide")
st.title("Network Intrusion Detection Visualizer")

uploaded_file = st.file_uploader("Upload your network log file (.csv)", type=["csv"])

if uploaded_file:
    data = pd.read_csv(uploaded_file)
    st.write("Uploaded Data Preview:", data.head())

    model = joblib.load("model/ids_model.pkl")

    # Assume preprocessing is already done in model training
    predictions = model.predict(data)
    data["Prediction"] = predictions

    st.write("Prediction Results", data)

    attack_counts = data["Prediction"].value_counts()
    st.subheader("Attack Type Distribution")
    st.bar_chart(attack_counts)
