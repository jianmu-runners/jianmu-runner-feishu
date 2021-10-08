# coding: utf-8

import json
import os
import requests

def send():
    print('进入fulltext')
    JIANMU_BOT_WEBHOOK_URL = os.getenv("JIANMU_BOT_WEBHOOK_URL")
    JIANMU_MSG_TITLE = os.getenv("JIANMU_MSG_TITLE")
    JIANMU_MSG_TEXT = os.getenv("JIANMU_MSG_TEXT")
    JIANMU_MSG_LINK_TEXT = os.getenv("JIANMU_MSG_LINK_TEXT")
    JIANMU_MSG_LINK_HREF = os.getenv("JIANMU_MSG_LINK_HREF")
    JIANMU_MSG_AT_LIST = json.loads(os.getenv("JIANMU_MSG_AT_LIST"))

    data = {
        "msg_type": "post",
        "content": {
            "post": {
                "zh_cn": {
                    "title": JIANMU_MSG_TITLE,
                    "content": [
                        [
                            {
                                "tag": "text",
                                "text": JIANMU_MSG_TEXT
                            }, {
                            "tag": "a",
                            "text": JIANMU_MSG_LINK_TEXT,
                            "href": JIANMU_MSG_LINK_HREF
                        }
                        ]
                    ]
                }
            }
        }
    }

    # add at user
    for user_id in JIANMU_MSG_AT_LIST:
        at = {
            "tag": "at"
        }
        at["user_id"] = user_id
        data['content']['post']['zh_cn']['content'][0].append(at)

    data1 = json.dumps(data)
    response = requests.post(url=JIANMU_BOT_WEBHOOK_URL, data=data1)
    print(response.text)
