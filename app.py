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

# Generate synthetic logs
if 'synthetic_data' not in st.session_state:
    st.session_state.synthetic_data = None

if st.button("Generate Synthetic Test Logs"):
    st.session_state.synthetic_data = generate_synthetic_logs(200)

# Display data and cloud-safe CSV block
if st.session_state.synthetic_data is not None:
    data = st.session_state.synthetic_data
    st.markdown("### Generated Synthetic Data")
    st.dataframe(data.head())

    csv = data.to_csv(index=False)
    st.markdown("### Copyable CSV Output")
    st.text_area("Long press to copy on mobile", csv, height=200)

# Upload file for prediction
uploaded_file = st.file_uploader("Upload your network log file (.csv)", type=["csv"])

if uploaded_file:
    data = pd.read_csv(uploaded_file)
    st.markdown("### Uploaded Data Preview")
    st.dataframe(data.head())

    model = joblib.load("model/ids_model.pkl")
    predictions = model.predict(data)
    data["Prediction"] = predictions

    st.markdown("### Prediction Results")
    st.dataframe(data)

    st.subheader("Attack Type Distribution")
    attack_counts = data["Prediction"].value_counts()
    st.bar_chart(attack_counts)
