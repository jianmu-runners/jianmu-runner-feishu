# coding:utf-8

import json
import requests

import util


def send_image(url):
    image = util.upload_image()
    data = {
        "msg_type": "image",
        "content": {
            "image_key": image
        }
    }
    response = requests.post(
        url=url,
        data=json.dumps(data)
    )
    content = response.json()
    if content.get("StatusCode") != 0:
        raise Exception(content)
    print(content)
