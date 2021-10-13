# coding: utf-8

import json
import os
import requests

import util


def send(url):
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
                            "text": JIANMU_MSG_LINK_TEXT if JIANMU_MSG_LINK_TEXT else "",
                            "href": JIANMU_MSG_LINK_HREF if JIANMU_MSG_LINK_HREF else ""
                        }
                        ]
                    ]
                }
            }
        }
    }

    # add at user
    if (JIANMU_MSG_AT_PHONE_LIST):
        open_ids = util.getOpenId(JIANMU_MSG_AT_PHONE_LIST)
        for open_id in open_ids:
            at = {
                "tag": "at"
            }
        at["open_id"] = open_id
        data['content']['post']['zh_cn']['content'][0].append(at)
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
