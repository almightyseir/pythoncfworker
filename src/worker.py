from js import Response, Headers, fetch, console
from urllib.parse import urlparse
import json
from pyrogram import send_message

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


