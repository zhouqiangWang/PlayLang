from dotenv import find_dotenv, load_dotenv
import os
import requests
import io
from PIL import Image
import json

load_dotenv(find_dotenv())

HF_API_TOKEN = os.getenv("HF_API_TOKEN")
HG_HEADERS = {"Authorization": f"Bearer {HF_API_TOKEN}"}

# text-to-image
def draw(description):
    API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-2-1"
    payload = {
        "inputs": description,
        "wait_for_model": "true",
    }
    response = requests.post(API_URL, headers=HG_HEADERS, json=payload)
    print(response.status_code)
    # print(response.json())

    image_bytes = response.content

    with open("Astronaut.JPEG", 'wb') as file:
        file.write(image_bytes)

    # image = Image.open(io.BytesIO(image_bytes))


draw("Astronaut riding a horse")
