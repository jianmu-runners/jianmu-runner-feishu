# coding: utf-8

import json
import os
import requests

import util


def send(url):
    print('进入fulltext')
    JIANMU_MSG_TITLE = os.getenv("JIANMU_MSG_TITLE")
    JIANMU_MSG_TEXT = os.getenv("JIANMU_MSG_TEXT")
    JIANMU_MSG_LINK_TEXT = os.getenv("JIANMU_MSG_LINK_TEXT")
    JIANMU_MSG_LINK_HREF = os.getenv("JIANMU_MSG_LINK_HREF")
    JIANMU_MSG_AT_LIST = json.loads(os.getenv("JIANMU_MSG_AT_LIST"))
    JIANMU_MSG_AT_PHONE_LIST = json.loads(os.getenv("JIANMU_MSG_AT_PHONE_LIST"))

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
    if (JIANMU_MSG_AT_PHONE_LIST):
        JIANMU_MSG_AT_LIST.extend(util.getUserId(JIANMU_MSG_AT_PHONE_LIST, 'user_id'))
    for user_id in JIANMU_MSG_AT_LIST:
        at = {
            "tag": "at"
        }
        at["user_id"] = user_id
        data['content']['post']['zh_cn']['content'][0].append(at)
    response = requests.post(url=url, data=json.dumps(data))
    content = response.json()
    if content.get("StatusCode") != 0:
        raise Exception(content)
    print(content)
