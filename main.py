import requests
import os
TOKEN = os.getenv("TOKEN")
import time
import json

url = f"https://api.telegram.org/bot{TOKEN}/getUpdates"

def get_updates():

    url = f"https://api.telegram.org/bot{TOKEN}/getUpdates"
    r = requests.get(url)
    return r.json()

def send_message(text, chat_id):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={text}"
    r=requests.get(url)
    return r.json()

CHAT_ID = 7157297566
idx = -1
while True:
    response=requests.get(url)
    data=response.json()
    result=data["result"]
    last_update=result[-1]
    
    last_update_id = last_update['update_id']
    
    if last_update_id != idx:
        text=last_update["message"]["text"]
        chat_id=last_update["message"]["chat"]["id"]
        send_message(text,chat_id)
        print(last_update_id, idx)
    idx = last_update_id
    time.sleep(0.5)



