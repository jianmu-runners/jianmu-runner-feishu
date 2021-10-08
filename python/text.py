# coding:utf-8

import json
import os
import requests

def send():
    print('进入text')
    JIANMU_BOT_WEBHOOK_URL = os.getenv('JIANMU_BOT_WEBHOOK_URL')
    JIANMU_MSG_TEXT = os.getenv('JIANMU_MSG_TEXT')

    data = {
        "msg_type": "text",
        "content": {
            "text": JIANMU_MSG_TEXT
        }
    }

    data1 = json.dumps(data)
    response = requests.post(url=JIANMU_BOT_WEBHOOK_URL, data=data1)
    print(response.text)
