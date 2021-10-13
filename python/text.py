# coding:utf-8

import json
import os
import requests

def send(url):
    print('进入text')
    JIANMU_MSG_TEXT = os.getenv('JIANMU_MSG_TEXT')

    data = {
        "msg_type": "text",
        "content": {
            "text": JIANMU_MSG_TEXT
        }
    }

    data1 = json.dumps(data)
    response = requests.post(url=url, data=data1)
    content = response.json()
    if content.get("StatusCode") != 0:
        raise Exception(content)
    print(content)
