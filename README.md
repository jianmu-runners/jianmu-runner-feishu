# jianmu-runner-notice

#### 介绍
用于对接飞书机器人

#### 参数说明
可参考[飞书-群机器人参数说明](https://www.feishu.cn/hc/zh-CN/articles/360024984973)

##### 全局参数
```
# 机器人webhook地址
JIANMU_BOT_WEBHOOK_URL

# 消息类型(text/fulltext/chat/image/interactive)
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
```
[如何查看userid](https://open.feishu.cn/document/home/user-identity-introduction/how-to-get)

chat
```
# 分享群的open_chat_id
JIANMU_SHARE_CHAT_ID
```

image
```
# 图片内容的base64编码，必填，图片（base64编码前）最大不能超过2M，支持JPG,PNG格式
JIANMU_IMAGE_BASE64
```

#### 构建docker镜像
```
# 创建docker镜像
docker build -t jianmudev/jianmu-runner-feishu-notice:${version} .

# 上传docker镜像
docker push jianmudev/jianmu-runner-feishu-notice:${version}
```

#### 用法
企业微信发送通知:
```
docker run --rm \
  -e JIANMU_BOT_WEBHOOK_URL=xxx \
  -e JIANMU_MSGTYPE=xxx \
  -e JIANMU_TEXT_CONTENT=xxx \
  -e JIANMU_MENTIONED_MOBILE_LIST='["xxx"]' \
  jianmudev/jianmu-runner-feishu-notice:${version}
```
