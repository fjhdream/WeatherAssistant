import os
import urllib.parse
import urllib.request
import requests
from dotenv import load_dotenv

load_dotenv()

# sever 酱 key
send_key = os.environ["PUSH_SERVER_SEND_KEY"]
# ntyf topic
topic = os.environ["PUSH_NTFY_SUB_PREFIX"]


def send(desp='', city=''):
    send_to_ntfy(desp, city)
    send_to_server(desp)


# 推动给 ntfy
def send_to_ntfy(desp, city: str):
    url = "https://ntfy.fjhdream.cn/" + topic + city.upper()
    requests.post(url,
                  data=desp.encode(encoding='utf-8'))


# 推送给 Server 酱
def send_to_server(desp):
    data = urllib.parse.urlencode({'title': "今日天气提醒", 'desp': desp}).encode('utf-8')
    url = f'https://sctapi.ftqq.com/{send_key}.send'
    req = urllib.request.Request(url, data=data, method='POST')
    with urllib.request.urlopen(req) as response:
        result = response.read().decode('utf-8')
    return result
