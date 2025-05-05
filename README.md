# Network Intrusion Detection Visualizer

A Streamlit app that detects network intrusions from uploaded `.csv` logs using a machine learning model.

## Features
- Generate or upload network traffic logs
- Run predictions using a trained Random Forest model
- Visualize attack vs normal classifications
- Mobile-friendly layout and CSV output
- Hosted via Streamlit Cloud

## Demo
[Try it on Streamlit Cloud](https://streamlit.io/cloud)

## Getting Started

### Clone the Repo
```bash
git clone https://github.com/your-username/network-intrusion-visualizer.git
cd network-intrusion-visualizer
```

### Requirements
Install dependencies:
```bash
pip install -r requirements.txt
```

### Run Locally
```bash
streamlit run app.py
```

### Deploy on Streamlit Cloud
1. Push this folder to a public GitHub repo
2. Go to [streamlit.io/cloud](https://streamlit.io/cloud)
3. Click **New app**, select your repo
4. Set `app.py` as the entry point
5. Deploy

## File Structure
```
network-intrusion-visualizer/
├── app.py
├── model/
│   └── ids_model.pkl
├── sample_logs.csv
├── requirements.txt
└── README.md
```

## Notes
- `ids_model.pkl` must exist in the `model/` folder for predictions to work.
- For test logs, use the included `sample_logs.csv`.

## License
MIT
