from linebot import LineBotApi, WebhookHandler
from linebot.models import TextSendMessage
import json
import os
from firebase import firebase
import google.generativeai as genai


# 使用環境變量讀取憑證
token = os.getenv('LINE_BOT_TOKEN')
secret = os.getenv('LINE_BOT_SECRET')
firebase_url = os.getenv('FIREBASE_URL')
gemini_key = os.getenv('GEMINI_API_KEY')


# Initialize the Gemini Pro API
genai.configure(api_key=gemini_key)

def linebot(request):
    body = request.get_data(as_text=True)
    json_data = json.loads(body)
    try:
        line_bot_api = LineBotApi(token)
        handler = WebhookHandler(secret)
        signature = request.headers['X-Line-Signature']
        handler.handle(body, signature)
        event = json_data['events'][0]
        tk = event['replyToken']
        user_id = event['source']['userId']
        msg_type = event['message']['type']

        fdb = firebase.FirebaseApplication(firebase_url, None)
        user_chat_path = f'chat/{user_id}'
        chat_state_path = f'state/{user_id}'
        chatgpt = fdb.get(user_chat_path, None)

        if msg_type == 'text':
            msg = event['message']['text']

            if chatgpt is None:
                messages = []
            else:
                messages = chatgpt

            if msg == '!清空':
                reply_msg = TextSendMessage(text='對話歷史紀錄已經清空！')
                fdb.delete(user_chat_path, None)
            else:
                model = genai.GenerativeModel('gemini-pro')
                messages.append({'role':'user','parts': [msg]})                
                response = model.generate_content(messages)
                messages.append({'role':'model','parts': [response.text]})                
                reply_msg = TextSendMessage(text=response.text)
                # 更新firebase中的對話紀錄
                fdb.put_async(user_chat_path, None , messages)
                
            line_bot_api.reply_message(tk, reply_msg)

        else:
            reply_msg = TextSendMessage(text='你傳的不是文字訊息呦')
            line_bot_api.reply_message(tk, reply_msg)

    except Exception as e:
        detail = e.args[0]
        print(detail)
    return 'OK'
