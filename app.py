import gradio as gr
from fastapi import FastAPI
from fastapi.middleware.wsgi import WSGIMiddleware
import joblib
import pandas as pd
from predict import predict

# Initialize FastAPI
app = FastAPI()

# 1. Load the model for the UI
model = joblib.load("model.pkl")

# 2. Define the UI Logic
def ui_predict(ph, Hardness, Solids, Chloramines, Sulfate, Conductivity, Organic_carbon, Trihalomethanes, Turbidity):
    input_dict = {
        "ph": ph, "Hardness": Hardness, "Solids": Solids, 
        "Chloramines": Chloramines, "Sulfate": Sulfate, 
        "Conductivity": Conductivity, "Organic_carbon": Organic_carbon, 
        "Trihalomethanes": Trihalomethanes, "Turbidity": Turbidity
    }
    result = predict(input_dict)
    
    label = "✅ SAFE (Potable)" if result["potability_prediction"] == 1 else "❌ UNSAFE (Non-Potable)"
    score = result["potability_probability"]
    return label, score

# 3. Create Gradio Interface
demo = gr.Interface(
    fn=ui_predict,
    inputs=[
        gr.Slider(0, 14, value=7, label="pH Level"),
        gr.Number(value=200, label="Hardness"),
        gr.Number(value=20000, label="Solids"),
        gr.Number(value=7, label="Chloramines"),
        gr.Number(value=300, label="Sulfate"),
        gr.Number(value=400, label="Conductivity"),
        gr.Number(value=10, label="Organic Carbon"),
        gr.Number(value=60, label="Trihalomethanes"),
        gr.Number(value=4, label="Turbidity"),
    ],
    outputs=[
        gr.Label(label="Result"),
        gr.Number(label="Model Confidence Score")
    ],
    title="Water Potability Predictor",
    description="Adjust the chemical parameters to check if the water is safe for human consumption."
)

# 4. Mount Gradio into FastAPI
app = gr.mount_gradio_app(app, demo, path="/")

# 5. Keep your existing API endpoint
@app.post("/predict")
def predict_api(data: dict): # Simplified for brevity, use your Pydantic model here
    return predict(data)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=7860)