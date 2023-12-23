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

line_bot_api = LineBotApi('tV3IJ3+GQVAijC1ln2c1HjqR8yIr6Ecs7W/w12HNDq21XLmh5MYBY1K1mkGh26HraJ5snw3WWY8D34V/oQwDjQ69Mg5Sx97+7fGbXEVvnfxDu4HUcOktTtSEYbXyCS1VB55hOuRG0Ap9GbMNcDIpqwdB04t89/1O/w1cDnyilFU=')

    # line_bot_api.push_message("U5da6b12cd475edeb05f53987ec2dd45d", TextSendMessage(text="คิดถึงแป้ง"))
line_bot_api.get_bot_info()