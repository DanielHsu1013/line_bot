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



    if msg in ['爛', '你好爛', '這甚麼爛程式', '爛程式']:
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
            original_content_url='https://i.imgur.com/3gOfodT.jpg',
            preview_image_url='https://i.imgur.com/3gOfodT.jpg'
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


    if msg in ['開心', '快樂', 'happy', 'Happy', '心情好', '好心情', '喜', '喜歡' ]:
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


    if msg in ['你好可愛', '你怎麼這麼可愛', '你超可愛', '好可愛喔', '好可愛', '你也太可愛了吧', '可愛']:
        image_message = ImageSendMessage(
            original_content_url='https://i.imgur.com/amRMc9g.jpg',
            preview_image_url='https://i.imgur.com/amRMc9g.jpg'
        )

        line_bot_api.reply_message(
            event.reply_token, 
            image_message)


    if msg in ['今天是我的生日', '我今天生日', '可以唱生日快樂給我聽嗎', '可以唱生日快樂給我聽嗎?', '生日', '生日快樂' ]:
        image_message = ImageSendMessage(
            original_content_url='https://i.imgur.com/6LT8Qy4.jpg',
            preview_image_url='https://i.imgur.com/6LT8Qy4.jpg'
        )

        line_bot_api.reply_message(
            event.reply_token, 
            image_message)


    if msg in ['怪人', '奇怪', 'weirdo', 'weird', 'Weirdo', '神經病']:
        image_message = ImageSendMessage(
            original_content_url='https://i.imgur.com/nbdTIWD.jpg',
            preview_image_url='https://i.imgur.com/nbdTIWD.jpg'
        )

        line_bot_api.reply_message(
            event.reply_token, 
            image_message)

    if msg in ['不是', '不是這個', '否', 'no', 'No', '不對', '這不是我要的', '我不要這個', ]:
        image_message = ImageSendMessage(
            original_content_url='https://i.imgur.com/Ef5BVhr.jpg',
            preview_image_url='https://i.imgur.com/Ef5BVhr.jpg'
        )

        line_bot_api.reply_message(
            event.reply_token, 
            image_message)


    if msg in ['起床', '早上', '早安', '太陽曬屁股']:
        image_message = ImageSendMessage(
            original_content_url='https://i.imgur.com/sjLjq65.jpg',
            preview_image_url='https://i.imgur.com/sjLjq65.jpg'
        )

        line_bot_api.reply_message(
            event.reply_token, 
            image_message)


    if msg in ['酷', '帥', '厲害', '計畫通']:
        image_message = ImageSendMessage(
            original_content_url='https://i.imgur.com/obU8uWZ.jpg',
            preview_image_url='https://i.imgur.com/obU8uWZ.jpg'
        )

        line_bot_api.reply_message(
            event.reply_token, 
            image_message)


    if msg in ['哭', '哭腰', '靠腰', '哭喔', '哭ㄟ', '傻眼']:
        image_message = ImageSendMessage(
            original_content_url='https://i.imgur.com/ZfiANhP.jpg',
            preview_image_url='https://i.imgur.com/ZfiANhP.jpg'
        )

        line_bot_api.reply_message(
            event.reply_token, 
            image_message)


    if msg in ['等', '等等', '等一下', '讓我想想', '讓我想一想', '等喔']:
        image_message = ImageSendMessage(
            original_content_url='https://i.imgur.com/khbC5q5.jpg',
            preview_image_url='https://i.imgur.com/khbC5q5.jpg'
        )

        line_bot_api.reply_message(
            event.reply_token, 
            image_message)

    if msg in ['快', '快點', '快一點', '你好慢', '好慢', '好慢喔', '太慢了吧']:
        image_message = ImageSendMessage(
            original_content_url='https://i.imgur.com/TxVq5pq.jpg',
            preview_image_url='https://i.imgur.com/TxVq5pq.jpg'
        )

        line_bot_api.reply_message(
            event.reply_token, 
            image_message)


    if msg in ['哈囉', '嗨嗨', 'Hi', 'hi', 'HI', '你好', '妳好', '嗨', 'Ciao', 'ciao', '安安', '起床', '起來', 'hello', 'Hello', 'HELLO']:
        r = '安安，早安、午安、晚上好！在下是可愛寶寶，你/妳的Meme Zone寶寶迷因庫小助理。先聲名本寶寶不太會聊天，目前還在學習中。請多擔待。請問今天需要什麼?'
    elif msg in ['來聊天', '可以聊天嗎?','要不要聊天?' ,'可以聊天嗎' ,'要不要聊天', '要來聊天嗎'] :
        r = '很抱歉，本寶寶才一歲。還沒有學會聊天技能'
    elif msg in ['我想要梗圖', '我想要迷因', '我想要找迷因', 'meme', 'MEME', 'Meme', '迷因', '我想找迷因', '找迷因', '找MEME', '找meme', '找Meme', '梗圖', '可愛寶寶迷因', '可愛寶寶梗圖', '可愛寶寶meme', '可愛寶寶Meme', '可愛寶寶MEME']:
        r = '請問今天想生產哪種寶寶迷因呢?'
     

    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=r))




if __name__ == "__main__":
    app.run()