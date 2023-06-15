import cv2

image = cv2.imread('IDE/1.jpg')

import io

_, compressed_image = cv2.imencode('.jpg', image, [1, 90])
file_bytes = io.BytesIO(compressed_image)

import requests

url_api = 'https://contractfit-intelligent-automation-ocr-ai.p.rapidapi.com/inboxes'
headers = {
    'X-RapidAPI-Key': 'ddb1379273mshfd92ba41d0beaadp1d8569jsn6af60b78cf09',
    'Content-Type': 'application/octet-stream',
    "X-RapidAPI-Host": "intelligent-automation-ocr-ai.p.rapidapi.com"
}

response = requests.post(url_api, headers=headers, data=file_bytes.getvalue())

print(response)