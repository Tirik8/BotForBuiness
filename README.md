# For what this bot?
This bot can track deleted messages and send you notifications about it, including the content of theese messages  
# Start bot  
1. In BotFather get token and turn on business mode
2. Create .env file with "BOT_API_KEY = [your token]" or pass the token as an argument
3. Download all librares from requierements.txt  
4. Download and run Redis
5. If you with .env file: enter command -> python main.py  
else: enter command -> python main.py [your bot token]
# TODO
---30%--- TODO: database with SQLalchemy ORM (async) [subscribes, price list, messages, users, users configs]?  
TODO: config menu for subscribers with configurate answers (regular expression?)  
TODO: inline buttons (with another library?)  
TODO: telegram payments for subscribe  
TODO: admins for bot? (admins can subscribe, unsubscribe, edit price list, edit config)  
TODO: handlers for voice, video and picture messages  
TODO: fields for resend messages and answers  
TODO: hadnler for rewited messages  
# DONE  
---OK--- env vars for bot config  
---OK--- rewrite bot to async  
---OK--- include redis  
---OK--- include advanced logging  
