# coding:utf-8
import json
import os
import requests

import util

url = os.getenv('JIANMU_BOT_WEBHOOK_URL')
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
