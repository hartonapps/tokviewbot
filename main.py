import requests
import re
import time

session = requests.Session()
base_url = "https://zefoy.com/"

def get_token():
    r = session.get(base_url)
    token = re.findall(r'name="token" value="(.*?)"', r.text)
    if token:
        return token[0]
    return None

def send_views(link):
    token = get_token()
    if not token:
        print("Token not found")
        return

    data = {
        "link": link,
        "token": token
    }

    r = session.post(base_url, data=data)
    print("Response:", r.text[:100])

link = input("Enter TikTok link: ")
amount = int(input("How many times: "))

for i in range(amount):
    send_views(link)
    print("Sent:", i+1)
    time.sleep(30)
