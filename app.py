import json
import aiohttp
from os import environ
from aiohttp import web
import requests
import math

# fanpage token
PAGE_ACCESS_TOKEN = 'EAAjtNWoSWWkBABK3SZBB5mxLe9eDw7s5YRk3Yg9HNKZCqZBmoiZAZBIXZBXBhXOtgsfCkcaYas22iSNhFVswPrYw421JKjiD4mqRLx9ZA99t9so0kKqklPoZBYdagmR6X2KPBnGwXDcEnMmz99qZB7g1UeOPJSESkEZC5NrOSl9RGU7KFkUdoKVvd3'
# verify token
VERIFY_TOKEN = 'thuandzai'

class BotControl(web.View):

    async def get(self):
        query = self.request.rel_url.query
        if(query.get('hub.mode') == "subscribe" and query.get("hub.challenge")):
            if not query.get("hub.verify_token") == VERIFY_TOKEN:
                return web.Response(text='Verification token mismatch', status=403)
            return web.Response(text=query.get("hub.challenge"))
        return web.Response(text='Forbidden', status=403)

    async def post(self):
        data = await self.request.json()
        if data.get("object") == "page":
            await self.send_greeting("Chào bạn. Mình là bot demo của Ngô Thuận.")

            for entry in data.get("entry"):
                for messaging_event in entry.get("messaging"):
                    if messaging_event.get("message"):
                        sender_id = messaging_event["sender"]["id"]
                        message_text = messaging_event["message"]["text"]
                        url = 'https://bonded-halts.000webhostapp.com/TKB.json'
                        geturl = requests.get(url).json()
                        const = len(geturl)
                        if any(["thứ 2" in message_text.lower(), "Thứ 2" in message_text.lower()]):
                            for i in range(const):
                               await self.send_message(sender_id, geturl[i]['THỨ 2'])
                        elif any(["thứ 3" in message_text.lower(), "Thứ 3" in message_text.lower()]):
                            for i in range(const):
                               await self.send_message(sender_id, geturl[i]['THỨ 3'])
                        elif any(["thứ 4" in message_text.lower(), "Thứ 4" in message_text.lower()]):
                            for i in range(const):
                               await self.send_message(sender_id, geturl[i]['THỨ 4'])
                        elif any(["thứ 5" in message_text.lower(), "Thứ 5" in message_text.lower()]):
                            for i in range(const):
                               await self.send_message(sender_id, geturl[i]['THỨ 5'])
                        elif any(["thứ 6" in message_text.lower(), "Thứ 6" in message_text.lower()]):
                            for i in range(const):
                               await self.send_message(sender_id, geturl[i]['THỨ 6'])
                        elif any(["thứ 7" in message_text.lower(), "Thứ 7" in message_text.lower()]):
                            for i in range(const):
                               await self.send_message(sender_id, geturl[i]['THỨ 7'])
                        
                        else:
                            await self.send_message(sender_id, "Bạn dễ thương gì ấy ơi, Bạn Nói Gì Mình Không Hiểu ?")
                            await self.send_message(sender_id,
                                              "Do Bố Mình Lập Trình Nên Vẫn Còn Thiếu Sót, và sẽ bổ sung thêm ạ,Thank iu <3")

        return web.Response(text='ok', status=200)

    async def send_greeting(self, message_text):
        params = {
            "access_token": PAGE_ACCESS_TOKEN
        }
        headers = {
            "Content-Type": "application/json"
        }
        data = json.dumps({
            "setting_type": "greeting",
            "greeting": {
                "text": message_text
            }
        })
        async with aiohttp.ClientSession() as session:
            await session.post("https://graph.facebook.com/v3.0/me/thread_settings", params=params, headers=headers, data=data)

    async def send_message(self, sender_id, message_text):

        params = {
            "access_token": PAGE_ACCESS_TOKEN
        }
        headers = {
            "Content-Type": "application/json"
        }
        data = json.dumps({
            "recipient": {
                "id": sender_id
            },
            "message": {
                "text": message_text
            }
        })

        async with aiohttp.ClientSession() as session:
            await session.post("https://graph.facebook.com/v3.0/me/messages", params=params, headers=headers, data=data)



routes = [
    web.get('/', BotControl, name='verify'),
    web.post('/', BotControl, name='webhook'),
]

app = web.Application()
app.add_routes(routes)

if __name__ == '__main__':
    web.run_app(app, host='0.0.0.0', port=environ.get("PORT", 9090))
