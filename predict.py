import joblib
import pandas as pd

# Load the model once when the script is imported to keep the API fast
MODEL_PATH = "model.pkl"
try:
    model = joblib.load(MODEL_PATH)
except:
    model = None

def predict(input_dict: dict):
    if model is None:
        return {"error": "Model file not found"}

    # Convert the dictionary into a DataFrame (1 row)
    # The columns must match the order expected by the pipeline
    df_input = pd.DataFrame([input_dict])

    # Get prediction and probability
    prediction = int(model.predict(df_input)[0])
    probabilities = model.predict_proba(df_input)[0]
    probability = float(probabilities[prediction])

    return {
        "potability_prediction": prediction,
        "potability_probability": probability
    }