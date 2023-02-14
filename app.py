from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
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

#message wtith user
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = event.message.text
    r = '可以請你說人話嗎? (若要叫醒小助理，請先喚醒他)'

    if msg in ['Hi', 'hi', 'HI', '你好', '妳好', '嗨', 'Ciao', 'ciao', '安安', '起床', '起來', 'hello', 'Hello', 'HELLO']:
        r = '安安，早安、午安、晚上好！在下是可愛寶寶，你/妳的Meme Zone寶寶迷因庫小助理`，請問今天需要什麼?'
    elif msg in ['聊', '講話']:
        r = '很抱歉，本寶寶才一歲。還沒有學會聊天技能'
    elif msg in ['吃大便']:
        r = '你才想吃大便吧?'
    
    if msg in ['meme', 'MEME', 'Meme', '迷因', '我想找迷因', '找迷因', '找MEME', '找meme', '找Meme', '梗圖', '可愛寶寶迷因', '可愛寶寶梗圖', '可愛寶寶meme', '可愛寶寶Meme', '可愛寶寶MEME']:
        r = '請問今天想生產哪種寶寶迷因呢?'





    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=r))


if __name__ == "__main__":
    app.run()