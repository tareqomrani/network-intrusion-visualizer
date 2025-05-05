import streamlit as st
import pandas as pd
import numpy as np
import joblib
import matplotlib.pyplot as plt

st.set_page_config(page_title="Network Intrusion Detection Visualizer", layout="wide")
st.title("Network Intrusion Detection Visualizer")

def generate_synthetic_logs(num_rows=100):
    protocols = ['tcp', 'udp', 'icmp']
    services = ['http', 'ftp', 'smtp', 'dns']
    flags = ['SF', 'S0', 'REJ', 'RSTO']

    data = {
        'duration': np.random.randint(0, 1000, size=num_rows),
        'protocol_type': np.random.choice(protocols, size=num_rows),
        'service': np.random.choice(services, size=num_rows),
        'flag': np.random.choice(flags, size=num_rows),
        'src_bytes': np.random.randint(0, 100000, size=num_rows),
        'dst_bytes': np.random.randint(0, 100000, size=num_rows),
        'label': np.random.choice(['normal', 'attack'], size=num_rows, p=[0.7, 0.3])
    }
    return pd.DataFrame(data)

# Button to generate synthetic logs
if st.button("Generate Synthetic Test Logs"):
    st.session_state.synthetic_data = generate_synthetic_logs(200)

# Display synthetic data and download button if available
if 'synthetic_data' in st.session_state:
    data = st.session_state.synthetic_data
    st.write("Generated Synthetic Data:", data.head())

    st.markdown("### Download Synthetic Logs")
    csv = data.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="Download as CSV",
        data=csv,
        file_name='synthetic_logs.csv',
        mime='text/csv'
    )

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
