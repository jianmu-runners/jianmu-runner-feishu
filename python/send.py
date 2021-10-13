# coding:utf-8

import full_text
import os
import text
import sys
import image
import interactive

print('进入send')
JIANMU_BOT_WEBHOOK_URL = os.getenv('JIANMU_BOT_WEBHOOK_URL')
JIANMU_MSGTYPE = os.getenv('JIANMU_MSGTYPE')

if JIANMU_MSGTYPE == 'text':
    text.send(JIANMU_BOT_WEBHOOK_URL)
elif JIANMU_MSGTYPE == 'fulltext':
    full_text.send(JIANMU_BOT_WEBHOOK_URL)
elif JIANMU_MSGTYPE == 'chat':
    print('暂不支持chat')
    sys.exit(1)
elif JIANMU_MSGTYPE == 'image':
    image.send_image(JIANMU_BOT_WEBHOOK_URL)
elif JIANMU_MSGTYPE == 'interactive':
    interactive.send(JIANMU_BOT_WEBHOOK_URL)
else:
    print('Error: The value of JIANMU_MSGTYPE must be in (text|fulltext|chat|image|interactive)!')
    sys.exit(1)
