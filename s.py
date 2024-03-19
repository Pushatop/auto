import datetime
from telethon.sync import *
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from time import sleep
photo = "photo.png" # сюда абсольютний путь к фото если вы на телефоне на пк можно указывать только название если файл в папке в которой скрипт
key = input('Введите ключ')
uri = "mongodb+srv://dany:Dan098070@cluster0.1disjcs.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(uri)
db = client.piar_bit
coll = db.keys
data = coll.find_one(filter={"_key": key})
key_stop = datetime.datetime.strptime(data["key_data"], '%Y-%m-%d %H:%M:%S')-datetime.datetime.now()
print(f"Осталлся {key_stop.days} день")
if data and  key_stop.days >= 0:
    
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
else:
    print("Ключ неверный, купите у @pushatop")
    exit()





