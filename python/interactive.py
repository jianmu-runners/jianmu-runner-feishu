import json
import os
import requests

import util


def send(url):
    JIANMU_MSG_TITLE = os.getenv('JIANMU_MSG_TITLE')
    JIANMU_MSG_TEXT = os.getenv('JIANMU_MSG_TEXT')
    JIANMU_MSG_MARKDOWN = os.getenv('JIANMU_MSG_MARKDOWN')
    JIANMU_MSG_AT_PHONE_LIST = json.loads(os.getenv("JIANMU_MSG_AT_PHONE_LIST"))

    data = {
        "msg_type": "interactive",
        "card": {
            "elements": []
        }
    }
    if (JIANMU_MSG_TITLE):
        data['card']['header'] = {
            "title": {
                "content": JIANMU_MSG_TITLE,
                "tag": "plain_text"
            },
        }

    image = util.upload_image()
    if (image):
        data['card']['elements'].insert(
            0,
            {
                "tag": "img",
                "img_key": image,
                "alt": {
                    "tag": "plain_text",
                    "content": ""
                }
            }
        )

    if (JIANMU_MSG_TEXT):
        data['card']['elements'].append(
            {
                "tag": "div",
                "text": {
                    "tag": "plain_text",
                    "content": JIANMU_MSG_TEXT
                }
            }
        )

    if (JIANMU_MSG_MARKDOWN):
        data['card']['elements'].append(
            {
                "tag": "markdown",
                "content": JIANMU_MSG_MARKDOWN
            }
        )

    if (JIANMU_MSG_AT_PHONE_LIST):
        open_ids = util.getOpenId(JIANMU_MSG_AT_PHONE_LIST)
        div = {
            "tag": "div",
            "fields": []
        }
        for open_id in open_ids:
            div['fields'].append({
                "text": {
                    "tag": "lark_md",
                    "content": "<at id=" + open_id + "><at>"
                }
            })
        data['card']['elements'].append(div)

    response = requests.post(
        url=url,
        data=json.dumps(data)
    )
    content = response.json()
    if content.get("StatusCode") != 0:
        raise Exception(content)
    print(content)
