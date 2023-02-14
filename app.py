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


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = event.message.text
    s = "hi 你好"
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text= s)


if __name__ == "__main__":
    app.run()