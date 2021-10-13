import os
import requests
import json

def getToken():
    JIANMU_APP_ID = os.getenv('JIANMU_APP_ID')
    JIANMU_APP_SECRET = os.getenv('JIANMU_APP_SECRET')
    postUrl = "https://open.feishu.cn/open-apis/auth/v3/tenant_access_token/internal/"
    payload_message = {
        "app_id": JIANMU_APP_ID,
        "app_secret": JIANMU_APP_SECRET
    }
    response = requests.post(url=postUrl, data=json.dumps(payload_message))
    content = response.json()
    if content.get("code") != 0:
        print("get token failed, errorCode is %s，please check AppID or App Secret" % content['code'])
    return content.get("tenant_access_token")


def getOpenId(phones):
    token = getToken()
    if(not token):
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
    if(content['data']['mobiles_not_exist']):
        print("mobiles_not_exist:", content['data']['mobiles_not_exist'])

    mobile_users = content.get('data').get('mobile_users')

    for phone in phones:
        user = mobile_users.get(phone)
        if (user):
            userIds.append(user[0].get('open_id'))
    return userIds

def upload_image():
    JIANMU_IMAGE_URL = os.getenv('JIANMU_IMAGE_URL')
    if(not JIANMU_IMAGE_URL):
        return ""
    response = requests.get(JIANMU_IMAGE_URL)
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
