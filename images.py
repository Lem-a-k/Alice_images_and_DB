import requests
import json

from config import OAuth_TOKEN, DIALOG_ID


def get_size():
    url = "https://dialogs.yandex.net/api/v1/status"
    headers = {
        'Authorization': f"OAuth {OAuth_TOKEN}"
    }
    response = requests.get(url, headers=headers)
    return response.json()


def upload_image(image_url):
    url = f"https://dialogs.yandex.net/api/v1/skills/{DIALOG_ID}/images"
    headers = {
        'Authorization': f"OAuth {OAuth_TOKEN}",
        'Content-Type': 'application/json'
    }
    data = {"url": image_url}
    response = requests.post(url, headers=headers, data=json.dumps(data))
    return response.json()