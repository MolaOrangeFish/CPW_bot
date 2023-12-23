from flask import Flask, request
import json
import numpy as np
from linebot import (LineBotApi, WebhookHandler)
from linebot.models import (
 MessageEvent, TextMessage, TextSendMessage, ImageSendMessage,
 SourceUser, SourceGroup, SourceRoom,
 TemplateSendMessage, ConfirmTemplate, MessageTemplateAction,
 ButtonsTemplate, URITemplateAction, PostbackTemplateAction,
 CarouselTemplate, CarouselColumn, PostbackEvent,
 StickerMessage, StickerSendMessage, LocationMessage, LocationSendMessage,
 ImageMessage, VideoMessage, AudioMessage,
 UnfollowEvent, FollowEvent, JoinEvent, LeaveEvent, BeaconEvent
)

app = Flask(__name__)

##long live token
Channel_access_token ='tV3IJ3+GQVAijC1ln2c1HjqR8yIr6Ecs7W/w12HNDq21XLmh5MYBY1K1mkGh26HraJ5snw3WWY8D34V/oQwDjQ69Mg5Sx97+7fGbXEVvnfxDu4HUcOktTtSEYbXyCS1VB55hOuRG0Ap9GbMNcDIpqwdB04t89/1O/w1cDnyilFU='
line_bot_api = LineBotApi(Channel_access_token)

#function การตอบกลับ
def event_handle(object):
    print(object)
    msgType = object['message']['type']
    userId = object['source']['userId']
    msgId = object['message']['id']

    if(msgType == "text"):
        msgTxt = object['message']['text']
        replyObj = TextSendMessage(text=msgTxt)
        line_bot_api.push_message(userId,replyObj)
    else:
        sk_id = np.random.randint(1,17)
        replyObj = StickerSendMessage(sticker_id= '52002740', package_id= '11537')
        line_bot_api.push_message(userId,replyObj)
    return ''

#ต่อ webhook with ngrok at lineDev ไว้รอ user send msg มา
@app.route('/webhook',methods = ['POST'])
def callback():
    json_line = request.get_json(force=False)
    json_line = json.dumps(json_line)
    decoded = json.loads(json_line)
    event = len(decoded['events'])
    for i in range(event):
        object= decoded['events'][i]
        event_handle(object)
    return '',200

if __name__ == '__main__':
    app.run(port = 8080)