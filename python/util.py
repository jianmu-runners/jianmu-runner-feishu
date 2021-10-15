import json
import os
import requests


def getToken():
    app_id = os.getenv('JIANMU_APP_ID')
    app_secret = os.getenv('JIANMU_APP_SECRET')
    post_url = "https://open.feishu.cn/open-apis/auth/v3/tenant_access_token/internal/"
    payload_message = {
        "app_id": app_id,
        "app_secret": app_secret
    }
    response = requests.post(url=post_url, data=json.dumps(payload_message))
    content = response.json()
    if content.get("code") != 0:
        print("get token failed, errorCode is %s，please check AppID or App Secret" % content['code'])
    return content.get("tenant_access_token")


def getOpenId(phones, str):
    token = getToken()
    if (not token):
        token = ""
    mobiles = "&mobiles=".join(phones)
    response = requests.get(
        url="https://open.feishu.cn/open-apis/user/v1/batch_get_id?mobiles=" + mobiles,
        headers={'Authorization': "Bearer " + token}
    )
    content = response.json()
    userIds = []

    if content.get('code') != 0:
        print("get userId failed, errorCode is %s" % content['code'])
        return userIds
    if (content['data']['mobiles_not_exist']):
        print("mobiles_not_exist:", content['data']['mobiles_not_exist'])

    mobile_users = content.get('data').get('mobile_users')

    for phone in phones:
        user = mobile_users.get(phone)
        if (user):
            userIds.append(user[0].get(str))
    return userIds


def upload_image():
    image_url = os.getenv('JIANMU_IMAGE_URL')
    if (not image_url):
        return ""
    response = requests.get(image_url)
    token = getToken()
    response = requests.post(
        url='https://open.feishu.cn/open-apis/image/v4/put/',
        headers={'Authorization': "Bearer " + token},
        files={
            "image": response.content
        },
        data={
            "image_type": "message"
        },
        stream=True)
    content = response.json()
    if content.get("code") == 0:
        return content.get("data").get("image_key")
    else:
        print('upload image failed:', content)
        return ""
