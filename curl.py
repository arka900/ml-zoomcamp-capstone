import requests
import json

# UPDATE: Changed port from 8000 to 7860 to match Docker/Hugging Face
url = "http://127.0.0.1:7860/predict"

sample_input = {
    "ph": 7.5,
    "Hardness": 210.2,
    "Solids": 22000.5,
    "Chloramines": 7.1,
    "Sulfate": 350.0,
    "Conductivity": 450.0,
    "Organic_carbon": 15.2,
    "Trihalomethanes": 70.3,
    "Turbidity": 4.1
}

try:
    response = requests.post(url, json=sample_input)

    if response.status_code == 200:
        print("✅ Success!")
        print(json.dumps(response.json(), indent=4))
    else:
        print(f"❌ Failed with status code: {response.status_code}")
        print("Error Details:", response.text)

except requests.exceptions.ConnectionError:
    print(f"❌ Connection Error: Is your Docker container running on {url}?")