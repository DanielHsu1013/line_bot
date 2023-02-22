#openai_api_key = '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'
import random
import requests

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

line_bot_api = LineBotApi('ea/BLUWOvQXmOmOC5s1h6GaJb2+RKYpnnI1ROnArigQT6bm2Fqyr9QWOHZk7vdrfKL4WZWa1ryDkrmWWUbw5Cjfu1E3L628GqzOjCyOSHgx917KE+5d1xdPRly44EUSdtw6c7q0dF6eJ4TnA1eH9FQdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('4ed29c44db401ce4d951957b5551d4aa')

class Play:
    def __init__(self):
        self.x = random.randint(1,100)
        self.c = 0

    def guess_game(self, y):
        self.c = self.c + 1
        if y == self.x:
            self.c = self.c + 1
            return f'答對了~你一共猜了{self.c - 1}次'
        elif y >= self.x:
            return f'再低一點~. 你已經猜了{self.c}次'
        else:
            return f'再高一點~. 你已經猜了{self.c}次'


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

# a list of image URLs
image_urls = [
    'https://i.imgur.com/ydwgx1F.jpg',
    'https://i.imgur.com/0hhmZN6.jpg',
    'https://i.imgur.com/3gOfodT.jpg'
    'https://i.imgur.com/NOTTPZW.jpg',
    'https://i.imgur.com/g7tnM8p.jpg',
    'https://i.imgur.com/mbGL9Oc.jpg',
    'https://i.imgur.com/Vxn4r6w.jpg',
    'https://i.imgur.com/amRMc9g.jpg',
    'https://i.imgur.com/7MgoxCJ.jpg',
    'https://i.imgur.com/NuDcPM0.jpg',
    'https://i.imgur.com/h7RH2y8.jpg',
    'https://i.imgur.com/qpcJBEJ.jpg',
    'https://i.imgur.com/MTLN8mo.jpg',
    'https://i.imgur.com/pW4vjva.jpg',
    'https://i.imgur.com/MG5dOh1.jpg',
    'https://i.imgur.com/5lC44Y0.jpg',
    'https://i.imgur.com/vFK1vtb.jpg',
    'https://i.imgur.com/ZfiANhP.jpg',
    'https://i.imgur.com/3fJJOnU.jpg',
    'https://i.imgur.com/pTiI7MX.jpg',
    'https://i.imgur.com/2V8aIcA.jpg',
    'https://i.imgur.com/4Wk4CSu.jpg',
    'https://i.imgur.com/uiJ69uC.jpg',
    'https://i.imgur.com/uiJ69uC.jpg',
    'https://i.imgur.com/bW3OwjV.jpg',
    'https://i.imgur.com/D5KQczy.jpg',
    'https://i.imgur.com/APRBk0h.jpg',
    'https://i.imgur.com/kXRUUga.jpg',
    'https://i.imgur.com/XWimhbR.jpg',
    'https://i.imgur.com/T9cjpKB.jpg',
    'https://i.imgur.com/5UNwYSv.jpg',
    'https://i.imgur.com/jiDCArw.jpg',
]

# guess game
# class Play:
#     def __init__(self):
#         print('要開始喽~')

#     def guess_game(self):
#         x = random.randint(1,100)
#         c = 0

#         while True:
#             c = c + 1
#             mgs = input('0到100，請猜一個數字~')
#             msg = int(msg)
#             if msg == x:
#                 c = c + 1
#                 r = '答對了~你一共猜了', c - 1, '次'
#                 break
#             elif msg >= x:
#                 r = '再低一點~. 你已經猜了', c, '次'
#             else:
#                 r = '再高一點~. 你已經猜了', c, '次'


#         line_bot_api.reply_message(
#             event.reply_token,
#             TextSendMessage(text=r))



# Sends a message containing a random image to the specified user
def send_random_image_message(user_id):
    image_url = random.choice(image_urls)
    image_response = requests.get(image_url)
    image_content = image_response.content
    message = ImageSendMessage(original_content_url=image_url, preview_image_url=image_url)
    line_bot_api.push_message(user_id, message)


# Your existing code for handling incoming messages
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    user_id = event.source.user_id
    msg = event.message.text


    if event.message.text == '猜數字':
        game = Play() # create an instance of the Play class
        game.guess_game()
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text='要開始喽~'))
    # elif event.message.text.isdigit():
    #     guess_result = game.guess_game(int(event.message.text))
    #     line_bot_api.reply_message(
    #         event.reply_token,
    #         TextSendMessage(text=r))


    if msg in ['隨機', '每日迷因', '隨機梗圖', 'random', '隨機寶寶']:
        send_random_image_message(user_id)

        line_bot_api.reply_message(
            event.reply_token, 
            image_message)


    else :
        r = '我今年一歲，還聽不懂你說什麼(OrQ)'



    if msg in ['爛', '你好爛', '這甚麼爛程式', '爛程式']:
        image_message = ImageSendMessage(
            original_content_url='https://i.imgur.com/ydwgx1F.jpg',
            preview_image_url='https://i.imgur.com/ydwgx1F.jpg'
        )

        line_bot_api.reply_message(
            event.reply_token, 
            image_message)


    if msg in ['co co', '貓', '貓咪', '摳摳', '摳摳龍']:
        image_message = ImageSendMessage(
            original_content_url='https://i.imgur.com/E27hB0l.jpg',
            preview_image_url='https://i.imgur.com/E27hB0l.jpg'
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


    if msg in ['你好可愛', '你怎麼這麼可愛', '你超可愛', '好可愛喔', '好可愛', '你也太可愛了吧', '可愛', '可愛寶寶']:
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

    if msg in ['不是', '不是這個', '否', 'no', 'No', '不對', '這不是我要的', '我不要這個', '怎麼醬', '怎麼這樣']:
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


    if msg in ['哭', '哭腰', '靠腰', '哭喔', '哭ㄟ', '傻眼', '可憐阿', '可憐', '可憐啊']:
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
        r = '在下是可愛寶寶~ 你/妳的寶寶迷因庫小助理。先聲名本寶寶不太會聊天，目前還在學習中。請多擔待。請問今天需要什麼?✧(•⌄• )◞ (若要獲得隨機寶寶圖，請輸入"隨機寶寶")'
    elif msg in ['來聊天', '可以聊天嗎?','要不要聊天?' ,'可以聊天嗎' ,'要不要聊天', '要來聊天嗎'] :
        r = '很抱歉，本寶寶才一歲。還沒有學會聊天技能'
    elif msg in ['我想要梗圖', '我想要迷因', '我想要找迷因', 'meme', 'MEME', 'Meme', '迷因', '我想找迷因', '找迷因', '找MEME', '找meme', '找Meme', '梗圖', '可愛寶寶迷因', '可愛寶寶梗圖', '可愛寶寶meme', '可愛寶寶Meme', '可愛寶寶MEME']:
        r = '請問今天想生產哪種寶寶迷因呢?'
    elif msg in ['智障', '智障寶寶']:
        r = '你才智障哩~'
    elif msg in ['我想玩遊戲']:
        game = Play() # create an instance of the Play class
        game.guess_game() # call the guess_game method on the instance



    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=r))




if __name__ == "__main__":
    app.run()


