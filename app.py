from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, ImageSendMessage
)

app = Flask(__name__)

line_bot_api = LineBotApi('txxdJs06LJjEmPkAu1cD0qN6VQWvUbGcDzytZ+VdNEhhjCejas2XqSdnP80F9LbnKL4WZWa1ryDkrmWWUbw5Cjfu1E3L628GqzOjCyOSHgzRCdo8tOlYd3LExUGTQYHTmJZEjo3To1IC6MCeOADz2wdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('4ed29c44db401ce4d951957b5551d4aa')


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'

#message with user
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = event.message.text
    r = '我今年一歲，還不聽不懂你說什麼(OrQ)'



    if msg in ['爛', '你好爛', '這甚麼爛程式']:
        image_message = ImageSendMessage(
            original_content_url='https://i.imgur.com/ydwgx1F.jpg',
            preview_image_url='https://i.imgur.com/ydwgx1F.jpg'
        )

        line_bot_api.reply_message(
            event.reply_token, 
            image_message)

    if msg in ['晚安', '掰掰', '再見', '明天見']:
        image_message = ImageSendMessage(
            original_content_url='https://i.imgur.com/0hhmZN6.jpg',
            preview_image_url='https://i.imgur.com/0hhmZN6.jpg'
        )

        line_bot_api.reply_message(
            event.reply_token, 
            image_message)

    if msg in ['吃大便', '你是不是想吃大便', '你吃大便' ]:
        image_message = ImageSendMessage(
            original_content_url='https://i.imgur.com/tArnBjV.jpg',
            preview_image_url='https://i.imgur.com/tArnBjV.jpg'
        )

        line_bot_api.reply_message(
            event.reply_token, 
            image_message)


    if msg in ['好吧', 'ok', 'OK', 'Ok', '好', '沒關係' ]:
        image_message = ImageSendMessage(
            original_content_url='https://i.imgur.com/NOTTPZW.jpg',
            preview_image_url='https://i.imgur.com/NOTTPZW.jpg'
        )

        line_bot_api.reply_message(
            event.reply_token, 
            image_message)


    if msg in ['挑倖', '嗆人', '決鬥' ]:
        image_message = ImageSendMessage(
            original_content_url='https://i.imgur.com/g7tnM8p.jpg',
            preview_image_url='https://i.imgur.com/g7tnM8p.jpg'
        )

        line_bot_api.reply_message(
            event.reply_token, 
            image_message)


    if msg in ['開心', '快樂', 'happy', 'Happy', '心情好', '好心情', '喜' ]:
        image_message = ImageSendMessage(
            original_content_url='https://i.imgur.com/mbGL9Oc.jpg',
            preview_image_url='https://i.imgur.com/mbGL9Oc.jpg'
        )

        line_bot_api.reply_message(
            event.reply_token, 
            image_message)


    if msg in ['嘲諷', '諷刺', '取笑', '笑死' ]:
        image_message = ImageSendMessage(
            original_content_url='https://i.imgur.com/Vxn4r6w.jpg',
            preview_image_url='https://i.imgur.com/Vxn4r6w.jpg'
        )

        line_bot_api.reply_message(
            event.reply_token, 
            image_message)


    if msg in ['你好可愛', '你怎麼這麼可愛', '你超可愛', '好可愛喔', '好可愛' ]:
        image_message = ImageSendMessage(
            original_content_url='https://i.imgur.com/Vxn4r6w.jpg',
            preview_image_url='https://i.imgur.com/Vxn4r6w.jpg'
        )

        line_bot_api.reply_message(
            event.reply_token, 
            image_message)


    if msg in ['今天是我的生日', '我今天生日', '可以唱生日快樂給我聽嗎', '可以唱生日快樂給我聽嗎?', '生日', '生日快樂' ]:
        image_message = ImageSendMessage(
            original_content_url='https://i.imgur.com/Vxn4r6w.jpg',
            preview_image_url='https://i.imgur.com/Vxn4r6w.jpg'
        )

        line_bot_api.reply_message(
            event.reply_token, 
            image_message)


    if msg in ['嗨嗨', 'Hi', 'hi', 'HI', '你好', '妳好', '嗨', 'Ciao', 'ciao', '安安', '起床', '起來', 'hello', 'Hello', 'HELLO']:
        r = '安安，早安、午安、晚上好！在下是可愛寶寶，你/妳的Meme Zone寶寶迷因庫小助理。先聲名本寶寶不太會聊天，目前還在學習中。請多擔待。請問今天需要什麼?'
    elif msg in ['來聊天', '可以聊天嗎?','要不要聊天?' ,'可以聊天嗎' ,'要不要聊天'] :
        r = '很抱歉，本寶寶才一歲。還沒有學會聊天技能'
    elif msg in ['meme', 'MEME', 'Meme', '迷因', '我想找迷因', '找迷因', '找MEME', '找meme', '找Meme', '梗圖', '可愛寶寶迷因', '可愛寶寶梗圖', '可愛寶寶meme', '可愛寶寶Meme', '可愛寶寶MEME']:
        r = '請問今天想生產哪種寶寶迷因呢?'
    elif msg in ['不是這個', '這不是我要的','不是' ,'不' ,'no', 'No'] :
        r = '很抱歉，本寶寶找不到你要的圖'        

    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=r))








if __name__ == "__main__":
    app.run()