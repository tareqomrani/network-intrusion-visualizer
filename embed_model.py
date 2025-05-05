import joblib
import base64
from io import BytesIO

# Base64-encoded model
model_base64 = """<PASTE THE FULL BASE64 STRING HERE>"""

model_bytes = base64.b64decode(model_base64)
model = joblib.load(BytesIO(model_bytes))
