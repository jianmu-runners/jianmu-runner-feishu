# coding:utf-8

import full_text
import os
import text
import sys

print('进入send')
JIANMU_BOT_WEBHOOK_URL = os.getenv('JIANMU_BOT_WEBHOOK_URL')
JIANMU_MSGTYPE = os.getenv('JIANMU_MSGTYPE')

if JIANMU_BOT_WEBHOOK_URL == '((xxx))':
    print('Error: JIANMU_BOT_WEBHOOK_URL is empty!')
    sys.exit(1)

if JIANMU_MSGTYPE == 'text':
    text.send()
elif JIANMU_MSGTYPE == 'fulltext':
    full_text.send()
elif JIANMU_MSGTYPE == 'chat':
    print('暂不支持chat')
elif JIANMU_MSGTYPE == 'image':
    print('暂不支持image')
elif JIANMU_MSGTYPE == 'interactive':
    print('暂不支持interactive')
else:
    print('Error: The value of JIANMU_MSGTYPE must be in (text|fulltext|chat|image|interactive)!')
    sys.exit(1)
