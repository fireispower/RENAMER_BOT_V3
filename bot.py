import asyncio
from pyrogram import Client, compose,idle
import os

from plugins.cb_data import app as Client2

TOKEN = os.environ.get("TOKEN", "6412599320:AAFde10xeuFFaSfGOnbDVL57jATTtBQDMF8")

API_ID = int(os.environ.get("API_ID", "7350195"))

API_HASH = os.environ.get("API_HASH", "b4105c3fddc4474048dfe79683555d0c")

STRING = os.environ.get("STRING", "")


bot = Client(

           "Renamer",

           bot_token=TOKEN,

           api_id=API_ID,

           api_hash=API_HASH,

           plugins=dict(root='plugins'))
           

if STRING:
    apps = [Client2,bot]
    for app in apps:
        app.start()
    idle()
    for app in apps:
        app.stop()
    
else:
    bot.run()
