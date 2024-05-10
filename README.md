# For what this bot?
This bot can track deleted messages and send you notifications about it, including the content of theese messages  
### Why this name?
In telegram, this bot can be connected in the menu "Telegram Business"
# Start bot  
1. In BotFather get token and turn on business mode  
2. In your tg account go to Settings -> Telegram Business-> Chatbots and enter your bot  
3. Initialize virtualvenv (python -m venv venv)  
4. Download all librares from requierements.txt  
5. Create .env file with "BOT_API_KEY = [your token]" or pass the token as an argument  
6. Download and run Redis  
7. Create derictories: content/photo, content/video, content/voice  
8. Run the commands:   alembic revision --autogenerate -m "start"   and   alembic upgrade head  
9. If you with .env file: enter command -> python main.py  
else: enter command -> python main.py [your bot token]  
### If you dont want to connect Redis
##### Replace in bot/main.py:  
"from aiogram.fsm.storage.redis import RedisStorage" -> "from aiogram.fsm.storage.memory import MemoryStorage"  
"dp = Dispatcher(storage=RedisStorage(redis=redis))" -> "dp = Dispatcher(storage=MemoryStorage())"  
##### And delete in bot/main.py:  
"redis = Redis()"  
### One library may contain a bug:  
(I dont remember wich one)  
If you catch it - go to github/issues, the problem is described there and it will be fixed in one line
# TODO
---50%--- TODO: database with SQLalchemy ORM (async) [messages, users, users configs]?  
TODO: config menu in telegram with configurate answers (regular expression?)  
TODO: fields for resend messages and answers  
