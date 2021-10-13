# jianmu-runner-feishu

#### 介绍
用于对接飞书机器人

#### 参数说明
可参考[飞书-群机器人参数说明](https://www.feishu.cn/hc/zh-CN/articles/360024984973)

##### 全局参数
```
# 机器人webhook地址
JIANMU_BOT_WEBHOOK_URL

# 消息类型(text/fulltext/image/interactive)
JIANMU_MSGTYPE
```

##### 根据msgtype不同设置不同的参数

text
```
# 文本内容，必填
JIANMU_MSG_TEXT
```

fulltext
```
# 文本标题，非必填
JIANMU_MSG_TITLE

# 文本内容，必填
JIANMU_MSG_TEXT

# 超链接文本内容，非必填
JIANMU_MSG_LINK_TEXT

# 超链接地址，非必填
JIANMU_MSG_LINK_HREF

# userid的列表，提醒群中的指定成员(@某个成员)，@all表示提醒所有人，非必填
JIANMU_MSG_AT_LIST

# 手机号列表，提醒群中的指定成员(@某个成员)，@all表示提醒所有人，非必填。需要App ID和App Secret，并且还要开启通过手机号或邮箱获取用户ID的权限
JIANMU_MSG_AT_PHONE_LIST
```
```
# 通过手机号@成员，需要App ID和App Secret，并且还要开启通过手机号或邮箱获取用户ID的权限

# 飞书应用App ID
JIANMU_APP_ID

# 飞书应用App Secret
JIANMU_APP_SECRET
```
[如何查看userid](https://open.feishu.cn/document/home/user-identity-introduction/how-to-get)

[如何获取AppId和AppSecret](https://open.feishu.cn/document/home/develop-a-bot-in-5-minutes/create-an-app)

[如何开启应用权限](https://open.feishu.cn/document/ukTMukTMukTM/uQjN3QjL0YzN04CN2cDN)

image
```
# 飞书应用App ID,必填
JIANMU_APP_ID

# 飞书应用App Secret，必填
JIANMU_APP_SECRET

# 图片url，必填，图片大小不能超过10MB
JIANMU_IMAGE_URL
```
[如何获取AppId和AppSecret](https://open.feishu.cn/document/home/develop-a-bot-in-5-minutes/create-an-app)

interactive
```
# 文本标题，非必填
JIANMU_MSG_TITLE

# 图片url，非必填，图片大小不能超过10MB
JIANMU_IMAGE_URL

# 文本内容，必填
JIANMU_MSG_TEXT

# markdown文本，非必填
JIANMU_MSG_MARKDOWN

# userid的列表，提醒群中的指定成员(@某个成员)，@all表示提醒所有人，非必填
JIANMU_MSG_AT_LIST

# 手机号列表，提醒群中的指定成员(@某个成员)，@all表示提醒所有人，非必填。需要App ID和App Secret，并且还要开启通过手机号或邮箱获取用户ID的权限
JIANMU_MSG_AT_PHONE_LIST
```
[markdown支持语法](https://open.feishu.cn/document/ukTMukTMukTM/uADOwUjLwgDM14CM4ATN)
```
# 发送图片，需要App ID和App Secret
# 通过手机号@成员，需要App ID和App Secret，并且还要开启通过手机号或邮箱获取用户ID的权限

# 飞书应用App ID
JIANMU_APP_ID

# 飞书应用App Secret
JIANMU_APP_SECRET
```

#### 构建docker镜像
```
# 创建docker镜像
docker build -t jianmudev/jianmu-runner-feishu:${version} -f dockerfile/Dockerfile .

# 上传docker镜像
docker push jianmudev/jianmu-runner-feishu:${version}
```

#### 用法
飞书发送文本通知:
```
docker run --rm \
  -e JIANMU_BOT_WEBHOOK_URL=xxx \
  -e JIANMU_MSGTYPE=text \
  -e JIANMU_MSG_TEXT=xxx \
  jianmudev/jianmu-runner-feishu:${version}
```

飞书发送富文本通知:
```
docker run --rm \
  -e JIANMU_BOT_WEBHOOK_URL=xxx \
  -e JIANMU_MSGTYPE=fulltext \
  -e JIANMU_MSG_TITLE=xxx \
  -e JIANMU_MSG_TEXT=xxx \
  -e JIANMU_MSG_AT_LIST='["xxx"]' \
  jianmudev/jianmu-runner-feishu:${version}
```

飞书发送图片:
```
docker run --rm \
    -e JIANMU_BOT_WEBHOOK_URL=xxx \
    -e JIANMU_MSGTYPE=image \
    -e JIANMU_APP_ID=xxx \
    -e JIANMU_APP_SECRET=xxx \
    -e JIANMU_IMAGE_URL=xxx \
    jianmudev/jianmu-runner-feishu:${version}
```

飞书发送消息卡片:
```
docker run --rm \
    -e JIANMU_BOT_WEBHOOK_URL=xxx \
    -e JIANMU_MSGTYPE=image \
    -e JIANMU_APP_ID=xxx \
    -e JIANMU_APP_SECRET=xxx \
    -e JIANMU_IMAGE_URL=xxx \
    -e JIANMU_MSG_TITLE=xxx \
    -e JIANMU_MSG_TEXT=xxx \
    -e JIANMU_MSG_MARKDOWN=xxx \
    -e JIANMU_MSG_AT_LIST='["xxx"]' \
    jianmudev/jianmu-runner-feishu:${version}
```


