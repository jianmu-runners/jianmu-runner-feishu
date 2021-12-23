# jianmu-runner-feishu

## 介绍
用于对接飞书机器人

## 飞书说明
[如何获取AppId和AppSecret](https://open.feishu.cn/document/home/develop-a-bot-in-5-minutes/create-an-app)

[如何开启应用权限](https://open.feishu.cn/document/ukTMukTMukTM/uQjN3QjL0YzN04CN2cDN)

![permission.png](./images/permission.png)

开启应用权限后，需要发布版本才能生效，发布版本时，可用性选择所有员工

![usability.png](./images/usability.png)

[如何查看userid](https://open.feishu.cn/document/home/user-identity-introduction/how-to-get)

## 发布到建木Hub
* 通过建木CI执行[feishu_notice_text.yml](https://gitee.com/jianmu-runners/jianmu-runner-list/blob/master/release_dsl/feishu_notice_text.yml) ，可将飞书通知-文本节点发布到建木Hub
* 通过建木CI执行[feishu_notice_post.yml](https://gitee.com/jianmu-runners/jianmu-runner-list/blob/master/release_dsl/feishu_notice_post.yml) ，可将飞书通知-富文本节点发布到建木Hub
* 通过建木CI执行[feishu_notice_image.yml](https://gitee.com/jianmu-runners/jianmu-runner-list/blob/master/release_dsl/feishu_notice_image.yml) ，可将飞书通知-图片节点发布到建木Hub
* 通过建木CI执行[feishu_notice_interactive.yml](https://gitee.com/jianmu-runners/jianmu-runner-list/blob/master/release_dsl/feishu_notice_interactive.yml) ，可将飞书通知-消息卡片节点发布到建木Hub


## 参数说明
可参考[飞书-群机器人参数说明](https://www.feishu.cn/hc/zh-CN/articles/360024984973)

### 全局参数
```
bot_webhook_url: 机器人webhook地址，必填
```

### 根据通知类型设置不同的参数

#### text
```
msg_text: 文本内容，必填
```

#### post
```
msg_title: 文本标题，非必填
msg_text: 文本内容，必填
msg_link_text: 超链接文本内容，非必填
msg_link_href: 超链接地址，非必填
msg_at_list: userid的列表，提醒群中的指定成员(@某个成员)，@all表示提醒所有人，非必填
msg_at_phone_list: 手机号列表，提醒群中的指定成员(@某个成员)，@all表示提醒所有人，非必填。需要App ID和App Secret，并且还要开启"通过手机号或邮箱获取用户ID"和"获取用户userID"的权限

# 通过手机号@成员时，需要App ID和App Secret，并且还要开启"通过手机号或邮箱获取用户ID"和"获取用户userID"的权限
app_id: 飞书应用App ID
app_secret: 飞书应用App Secret
```

#### image
```
app_id: 飞书应用App ID,必填
app_secret: 飞书应用App Secret，必填
image_url: 图片url，必填，图片大小不能超过10MB
```

#### interactive
```
msg_title: 文本标题，非必填
image_url: 图片url，非必填，图片大小不能超过10MB
msg_text: 文本内容，必填
msg_markdown: markdown文本，非必填
msg_at_phone_list: 手机号列表，提醒群中的指定成员(@某个成员)，@all表示提醒所有人，非必填。需要App ID和App Secret，并且还要开启"通过手机号或邮箱获取用户ID"和"获取用户userID"的权限

# 发送图片，需要App ID和App Secret
# 通过手机号@成员，需要App ID和App Secret，并且还要开启"通过手机号或邮箱获取用户ID"和"获取用户userID"的权限
app_id: 飞书应用App ID
app_secret: 飞书应用App Secret
```
[markdown支持语法](https://open.feishu.cn/document/ukTMukTMukTM/uADOwUjLwgDM14CM4ATN)

## 构建docker镜像
```
# 创建docker镜像
docker build -t jianmurunner/feishu_notice_xxx:${version} -f dockerfile/Dockerfile .

# 上传docker镜像
docker push jianmurunner/feishu_notice_xxx:${version}
```

## 用法
飞书发送文本通知:
```
docker run --rm \
  -e JIANMU_BOT_WEBHOOK_URL=xxx \
  -e JIANMU_MSG_TEXT=xxx \
  jianmurunner/feishu_notice_text:${version} \
  /usr/local/bin/text.py
```

飞书发送富文本通知:
```
docker run --rm \
  -e JIANMU_BOT_WEBHOOK_URL=xxx \
  -e JIANMU_MSG_TITLE=xxx \
  -e JIANMU_MSG_TEXT=xxx \
  -e JIANMU_MSG_LINK_TEXT=xxx \
  -e JIANMU_MSG_LINK_HREF=xxx \
  -e JIANMU_MSG_AT_LIST='["xxx"]' \
  -e JIANMU_APP_ID=xxx \
  -e JIANMU_APP_SECRET=xxx \
  -e JIANMU_MSG_AT_PHONE_LIST='["xxx"]' \
  jianmurunner/feishu_notice_post:${version} \
  /usr/local/bin/post.py
```

飞书发送图片:
```
docker run --rm \
    -e JIANMU_BOT_WEBHOOK_URL=xxx \
    -e JIANMU_APP_ID=xxx \
    -e JIANMU_APP_SECRET=xxx \
    -e JIANMU_IMAGE_URL=xxx \
    jianmurunner/feishu_notice_image:${version} \
    /usr/local/bin/image.py
```

飞书发送消息卡片:
```
docker run --rm \
    -e JIANMU_BOT_WEBHOOK_URL=xxx \
    -e JIANMU_APP_ID=xxx \
    -e JIANMU_APP_SECRET=xxx \
    -e JIANMU_IMAGE_URL=xxx \
    -e JIANMU_MSG_TITLE=xxx \
    -e JIANMU_MSG_TEXT=xxx \
    -e JIANMU_MSG_MARKDOWN=xxx \
    -e JIANMU_MSG_AT_LIST='["xxx"]' \
    jianmurunner/feishu_notice_interactive:${version} \
    /usr/local/bin/interactive.py
```


