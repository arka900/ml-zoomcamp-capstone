
---

# Water Potability – ML Zoomcamp Capstone Project

This project predicts whether a water sample is **potable** (safe for human consumption) based on environmental and chemical sensor readings such as **pH, Sulfate levels, Hardness, and Chloramines**.

The dataset is automatically fetched from **Kaggle** and processed through a **robust Random Forest machine learning pipeline**.

---

## Project Features

- End-to-end **Machine Learning Pipeline**
  - Data fetching
  - Missing value imputation
  - Feature scaling
- **Random Forest** model with hyperparameter tuning
- **FastAPI** backend with **Gradio UI** integration
- Fully **Dockerized API** for easy reproduction and deployment
- Clean, modular code structure:
  - `train.py`
  - `predict.py`
  - `app.py`

- **Exploratory Data Analysis (EDA)** in `notebook.ipynb`

---

## Exploratory Data Analysis

The Jupyter notebook includes:

- Data cleaning and missing value imputation
- Model selection and hyperparameter tuning
- Feature importance analysis

---

## Setup & Usage

### 1. Clone the Repository

```bash
git clone git@github.com:arka900/ml-zoomcamp-capstone.git
cd ml-zoomcamp-capstone
```

## 2. Create the virtual environment using conda along with the necessary libraries (if done locally)

```bash
conda env create -f environment.yaml
conda activate capstone
```
```bash
pip install -r requirements.txt
```

## 3. Train the Model (Locally)

```bash
python train.py
```

This will generate:

`model.pkl`

## 4. Run the Prediction Service Locally

```bash
python app.py
```

Open the browser:

API root & UI: http://127.0.0.1:7860

Docs UI: http://127.0.0.1:7860/docs

Use the POST `/predict`  endpoint or the Gradio interface at the root URL.

## 5. Interact with the service: 

Run the curl.py script in a separate terminal to send a POST request to the prediction service

```bash
python curl.py
```

## 6. Build & Run the Docker Image

### **Build the image**

```bash
docker build -t water-api .
```
###  **Run the container**

```bash
docker run -p 7860:7860 water-api
```

API will be available at:

```
http://127.0.0.1:7860
http://127.0.0.1:7860/docs

```

### 7. Cloud Deployment

I have used Hugging Face Spaces (http://huggingface.co) to host the Docker container. 

It lives on at: https://huggingface.co/spaces/arka900/water-potability-api
