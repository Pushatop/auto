import datetime
from telethon.sync import *
from time import sleep
photo = "photo.png" # сюда абсольютний путь к фото если вы на телефоне на пк можно указывать только название если файл в папке в которой скрипт
    
api_id = input('Введите api_id' )
api_hash = input('Введите api_hash')
phone = input('Введите номер телефона')
msg = input('Введите сообщение')
withphoto = input('С фото?')
delay = input('Введите задержку')
chats = input('Введите чаты в таком формате @chat1 @chat2 @chat3')
piartime = input(f'Введите сколько сообщений будет всего')
photopiar = True if str(withphoto).lower() == "да" else False
sesion = TelegramClient(phone, api_hash=api_hash, api_id=int(api_id))
sesion.connect()
if not sesion.is_user_authorized():
    sesion.send_code_request(phone)
    sesion.sign_in(phone, input('Введите код'))
i = 0
while True:
    
    for chat in str(chats).split():
        try:
            if photopiar:
                sesion.send_file(chat, photo, caption=str(msg))
            else:
                sesion.send_message(chat, str(msg))
        except Exception as ex:
            print(ex)
    sleep(int(delay))
    i += 1
    if i >= int(piartime):
        exit()






