import requests
from telethon import events, Button, TelegramClient
import os
import logging


logging.basicConfig(level=logging.INFO)

try:
    API_ID = int(os.environ.get("API_ID", 6))
    API_HASH = os.environ.get("API_HASH", None)
    TOKEN = os.environ.get("TOKEN", None)
except ValueError:
    print("You forgot to fullfill vars")
    print("Bot is quitting....")
    exit()
except Exception as e:
    print(f"Error - {str(e)}")
    print("Bot is quitting.....")
    exit()
except ApiIdInvalidError:
    print("Your API_ID or API_HASH is Invalid.")
    print("Bot is quitting.")
    exit()

bot = TelegramClient('bin', API_ID, API_HASH)
bin = bot.start(bot_token=TOKEN)

@bin.on(events.NewMessage(pattern="^[!?/]start$"))
async def start(event):
    if event.is_group:
        await event.reply("**Bin-Checker is Alive**")
        return
    await event.reply(f"**Heya {event.sender.first_name}**\nIts a Bin-Checker Bot To Check Your Bins Are Valid Or Not.", buttons=[
    [Button.url("My Developer", "https://t.me/Dileepa_Malshan")]
    ])

@bin.on(events.NewMessage(pattern="^[!?/]help$"))
async def help(event):
    text = """
**Welcome to HelpMenu:**

- /start - To Start Me :)
- /help - To Get Help Menu
- /bin - To check is your bin valid or not
"""
    await event.reply(text, buttons=[[Button.url("My Developer ", "https://t.me/Dileepa_Malshan")]])

@bin.on(events.NewMessage(pattern="^[!?/]fake"))
async def binc(event):
    xx = await event.reply("`Processing.....`")
    try:
        input = event.text.split(" ", maxsplit=1)[1]

        url = f"https://randomuser.me/api/"
    response = requests.get(url).json()
    gender = response["results"][0]["gender"]
    name = response["results"][0]["name"]
    location = response["results"][0]["location"]
    birthday = response["results"][0]["dob"]
    if gender == "male":

        try:
            message = f"""
            Name 🙋‍♂️ : {name['title']}.{name['first']} {name['last']}
            Address 👇
            Street 🛣 : {location['street']['number']} {location['street']['name']}
            City 🌆 : {location['city']}
            State 🚏 : {location['state']}
            Country 🏜: {location['country']}
            Post Code 📮 : {location['postcode']}
            Contact 👇  
            Email 📧 : {response['results'][0]['email']}
            Phone 📱 : {response['results'][0]['phone']}
            Age 👇
            Birthday 🎂 : {birthday['date']}
            """
        
print ("Successfully Started")
bin.run_until_disconnected()
