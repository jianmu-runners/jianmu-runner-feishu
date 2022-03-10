# coding: utf-8

import json
import os
import requests

import util

url = os.getenv('JIANMU_BOT_WEBHOOK_URL')
title = os.getenv("JIANMU_MSG_TITLE")
text = os.getenv("JIANMU_MSG_TEXT")
link_text = os.getenv("JIANMU_MSG_LINK_TEXT")
link_href = os.getenv("JIANMU_MSG_LINK_HREF")
msg_at_list = json.loads(os.getenv("JIANMU_MSG_AT_LIST"))
msg_at_phone_list = json.loads(os.getenv("JIANMU_MSG_AT_PHONE_LIST"))

data = {
    "msg_type": "post",
    "content": {
        "post": {
            "zh_cn": {
                "title": title,
                "content": [
                    [
                        {
                            "tag": "text",
                            "text": text
                        }, {
                        "tag": "a",
                        "text": link_text,
                        "href": link_href
                    }
                    ]
                ]
            }
        }
    }
}

# add at user
if (msg_at_phone_list):
    msg_at_list.extend(util.getOpenId(msg_at_phone_list, 'user_id'))
if len(msg_at_list) != 0:
    for user_id in msg_at_list:
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
