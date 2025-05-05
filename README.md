<p align="center">
  <img src="./banner.png" alt="Network Intrusion Detection Visualizer Banner" width="100%">
</p>

# Network Intrusion Detection Visualizer

A Streamlit-based machine learning app for visualizing and detecting network intrusions using offline data and models.

## Features
- Upload and preview CSV network logs
- Run predictions using a local ML model
- Visualize attack type distribution with interactive charts
- Offline and API-free setup

## Installation

```bash
git clone https://github.com/yourusername/network-intrusion-visualizer.git
cd network-intrusion-visualizer
pip install -r requirements.txt
streamlit run app.py
```

## Model
Place your trained ML model (`ids_model.pkl`) in the `model/` directory. The model should be trained on preprocessed NSL-KDD or similar datasets.

## Dataset
Use offline datasets such as [NSL-KDD](https://www.unb.ca/cic/datasets/nsl.html). Place a test `.csv` file in the `data/` directory.

## Folder Structure
```
nids-streamlit/
├── app.py
├── requirements.txt
├── README.md
├── model/
│   └── ids_model.pkl  # Add your model here
└── data/
    └── NSL-KDD-test.csv  # Add your test data here
```

## Future Improvements
- Add SHAP explainability for model transparency
- Support real-time or batch packet simulation
- Improve multi-class classification for diverse attacks

## License
MIT

## Acknowledgements
- NSL-KDD dataset by Canadian Institute for Cybersecurity
- Built with Streamlit, scikit-learn, and pandas
