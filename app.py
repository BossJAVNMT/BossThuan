import json
import aiohttp
from os import environ
from aiohttp import web

# fanpage token
PAGE_ACCESS_TOKEN = 'EAAjtNWoSWWkBAKHoqaoOIAaR0ZBonggRw5cy4IVoEM5KaiFkDSntzySLmM2r8nRyZBebDmmIr8LZABPZCkLee8GimSNYqIfs63EbZCjEbLxMAIPnpF3LZBq0Pa7aLZC7k5rQQXQZBKlX4cyv8XKakcZC0HbDHiLccPzQpjGu2xIcccwC4eZCw8pmJK'
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

                        if any(["chào" in message_text.lower(), "hi " in message_text.lower(),
                                "hello" in message_text.lower(), "có ai" in message_text.lower(),
                                "có ở đó" in message_text.lower(), "hi" == message_text.lower(),"alo" in message_text.lower()]):
                            await self.send_message(sender_id, "Chào Bạn :)")
                        elif any(["bạn tên" in message_text.lower(), "mày tên" in message_text.lower(),
                                "your name" in message_text.lower(), "cậu tên" in message_text.lower(),
                                "bot tên" in message_text.lower()]):
                            await self.send_message(sender_id, "Mình Tên Là Bot Dzai :))")
                        elif any(["tác giả" in message_text.lower(), "người viết" in message_text.lower(),
                                "ai lập" in message_text.lower(), ]):
                            await self.send_message(sender_id, "Hí Hí Bố Thuận Dzai Đã Tạo Ra Mình Nhaaa <3")
                        elif any(["bố mày là ai" in message_text.lower(), "ba mày" in message_text.lower(), "cha mày" in message_text.lower(), "bố mày" in message_text.lower(), "tía mày" in message_text.lower()]):
                            await self.send_message(sender_id, "Bố tớ á. Đzai lắm :))")
                            await self.send_message(sender_id, "Info bố tớ nhè: https://www.facebook.com/ThuannDzaiO.o")
                        elif any(["địt" in message_text.lower(),"mẹ mày" in message_text.lower(),"con mẹ mày" in message_text.lower(),
                        "lồn" in message_text.lower(),"bòi" in message_text.lower(),"ngu"  in message_text.lower(),"óc chó"  in message_text.lower(),"óc lồn"  in message_text.lower()]):
                            await self.send_message(sender_id, "Mình là Bot Dễ Thương Hiền Lành")
                            await self.send_message(sender_id, "Bố mình bảo rằng không thèm care mấy con CHÓ bên đường chửi con :)")
                        elif any(["đánh nhau" in message_text.lower(),"dịt nhau" in message_text.lower(),"chém nhau" in message_text.lower()]):
                            await self.send_message(sender_id, "Ngon Thì Nhào Zô ?")
                        elif any(["zô"  in message_text.lower(),"lẹ" in message_text.lower()]):
                            await self.send_message(sender_id, "Có Cai Lon ?")
                        elif any(["yêu mình" in message_text.lower(), "yêu chị" in message_text.lower(), "yêu anh" in message_text.lower(),"yêu tớ " in message_text.lower()]):
                            await self.send_message(sender_id, "Yêu Yêu Cái Đầu Puồi ?")
                            await self.send_message(sender_id, "Câu Đấy Là Dành Cho Bọn Khác, Còn Với You Thì <3 To Đùng :))")
                        elif any(["đẹp trai" in message_text.lower(),"ngon zai" in message_text.lower(),"dzai" in message_text.lower()]):
                            await self.send_message(sender_id, "Mình Biết Bạn Đang Nói Bố Mình Đzai Mà :v")
                        elif any(["hihi" in message_text.lower(),"haha" in message_text.lower(),"hehe" in message_text.lower(),"hí hí" in message_text.lower()]):
                            await self.send_message(sender_id, "Cười Gì ?")
                        elif any(["thích" in message_text.lower(), "tỏ tình"  in message_text.lower()]):
                            await self.send_message(sender_id, "Anh <3 Em")
                        elif any(["ừ" in message_text.lower(),"ờ" in message_text.lower(),"ừa" in message_text.lower(),"um" in message_text.lower(),"oke" in message_text.lower(),
                        "okay" in message_text.lower(),"thôi" in message_text.lower()]):
                            await self.send_message(sender_id, "Oke Cưng!")
                        elif any(["eii" in message_text.lower(),"ơi" in message_text.lower(),"hú" in message_text.lower(),"ê" in message_text.lower()]):
                            await self.send_message(sender_id, "Dạ ?")
                        elif any(["bye" in message_text.lower(),"bái bai" in message_text.lower(),"cút" in message_text.lower(),"tạm biệt" in message_text.lower(),"biến" in message_text.lower()]):
                            await self.send_message(sender_id, "Bye Bạn Nhaaa <3")
                        elif any(["khen" in message_text.lower(),"thế nào" in message_text.lower(),"xinh" in message_text.lower()]):
                            await self.send_message(sender_id, "Bạn Ngon Lắm :))")
                        elif any(["trai hay là gái" in message_text.lower()]):
                            await self.send_message(sender_id, "Mình Bê Đê Nhaaa :((")
                        elif any(["làm toán" in message_text.lower(),"làm văn" in message_text.lower()]):
                            await self.send_message(sender_id, "Huấn Rosse: Không Làm Mà Đòi Có Ăn Thì Ăn Đầu B*i ăn C*t")
                        elif any(["nhậu" in message_text.lower(),"ụm" in message_text.lower()]):
                            await self.send_message(sender_id, "Nâu Nâu, Nát Lắm :((")
                            await self.send_message(sender_id, "Bạn bao nhế :3")
                        elif any(["rửa bát" in message_text.lower(),"nấu" in message_text.lower(),"cơm" in message_text.lower(),"bếp" in message_text.lower()]):
                            await self.send_message(sender_id, "Thịt bạn còn làm được chứ mấy thứ này ez :)")

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