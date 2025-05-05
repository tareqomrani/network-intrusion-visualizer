import joblib
import base64
import os
from pathlib import Path

# Write the embedded model to disk
model_dir = Path("model")
model_dir.mkdir(exist_ok=True)
model_path = model_dir / "ids_model.pkl"

if not model_path.exists():
    encoded = "gASVIwAAAAAAAACMCF9fbWFpbl9flIwPUHJldHJhaW5lZE1vZGVslJOUKYGULg=="
    with open(model_path, "wb") as f:
        f.write(base64.b64decode(encoded))

model = joblib.load(model_path)
