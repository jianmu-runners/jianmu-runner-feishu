import json
import os
import requests

import util


url = os.getenv('JIANMU_BOT_WEBHOOK_URL')
msg_title = os.getenv('JIANMU_MSG_TITLE')
msg_text = os.getenv('JIANMU_MSG_TEXT')
msg_markdown = os.getenv('JIANMU_MSG_MARKDOWN')
msg_at_phone_list = json.loads(os.getenv("JIANMU_MSG_AT_PHONE_LIST"))

data = {
    "msg_type": "interactive",
    "card": {
        "elements": []
    }
}
if (msg_title):
    data['card']['header'] = {
        "title": {
            "content": msg_title,
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

if (msg_text):
    data['card']['elements'].append(
        {
            "tag": "div",
            "text": {
                "tag": "plain_text",
                "content": msg_text
            }
        }
    )

if (msg_markdown):
    data['card']['elements'].append(
        {
            "tag": "markdown",
            "content": msg_markdown
        }
    )

if (msg_at_phone_list):
    open_ids = util.getOpenId(msg_at_phone_list, 'open_id')
    if len(open_ids) != 0:
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
