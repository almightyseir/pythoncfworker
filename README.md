#
<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif">
<h4 align="center">ꜱɪᴍᴘʟᴇ ᴄᴏᴅᴇ ꜰᴏʀ ᴛɢʙᴏᴛ ɪɴ ᴄꜰ ᴡᴏʀᴋᴇʀ ᴜꜱɪɴɢ ᴘʏᴛʜᴏɴ</p>


```
from js import Response, Headers, fetch, console
from urllib.parse import urlparse
import json

token = "" #or use env,declare them in wrangler.toml
async def send_message(chat_id, text):
    url = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={text}"
    await fetch(url)

async def on_fetch(request):
    url = urlparse(request.url)
    if url.path == "/bot" and request.method == 'POST':
        request_body = await request.text()
        tg_json = json.loads(request_body)
        if "message" in tg_json:
            chat_id = tg_json["message"]["chat"]["id"]
            if tg_json["message"]["text"] == "/start":
                firstname = tg_json["message"]["from"]["first_name"]
                text = f"Hey {firstname} ❣️!\nThis is a simple telegram bot made in cf workers using python😁"
                await send_message(chat_id, text)
                return Response.new("OK...", {"status": 200})
    elif url.path == "/":
        return Response.new("Python Worker :)", {"status": 200})

    return Response.new("Invalid request", {"status": 400})



   
```
#
