from js import fetch

token = "" #or use env,declare them in wrangler.toml
async def send_message(chat_id, text):
    url = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={text}"
    await fetch(url)

#add more too busy rn