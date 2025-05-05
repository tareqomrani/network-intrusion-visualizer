import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
import joblib
import os

# Create model directory if it doesn't exist
os.makedirs("model", exist_ok=True)

# Generate synthetic training data
protocols = ['tcp', 'udp', 'icmp']
services = ['http', 'ftp', 'smtp', 'dns']
flags = ['SF', 'S0', 'REJ', 'RSTO']

def generate_logs(num_rows=1000):
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

df = generate_logs(1000)
X = pd.get_dummies(df.drop(columns=["label"]))
y = df["label"].map({'normal': 0, 'attack': 1})

# Train model
model = RandomForestClassifier(n_estimators=50, random_state=42)
model.fit(X, y)

# Save model
joblib.dump(model, "model/ids_model.pkl")
print("Model trained and saved to model/ids_model.pkl")
