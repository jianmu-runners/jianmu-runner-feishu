# coding:utf-8

import json
import os
import requests

url = os.getenv('JIANMU_BOT_WEBHOOK_URL')
text = os.getenv('JIANMU_MSG_TEXT')

data = {
    "msg_type": "text",
    "content": {
        "text": text
    }
}

data1 = json.dumps(data)
response = requests.post(url=url, data=data1)
content = response.json()
if content.get("StatusCode") != 0:
    raise Exception(content)
print(content)
