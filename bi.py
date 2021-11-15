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

@bin.on(events.NewMessage(pattern="^[!?/]bin"))
async def binc(event):
    xx = await event.reply("`Processing.....`")
    try:
        input = event.text.split(" ", maxsplit=1)[1]

        url = requests.get(f"https://randomuser.me/api/1.2/?nat={input}")
        res = url.json()
        first = ['results'][0]['name']['first']
        last =  ['results'][0]['name']['last']
        gend = ['results'][0]['gender']
        street = ['results'][0]['location']['street']
        city = ['results'][0]['location']['city']
        state = ['results'][0]['location']['state']
        email = ['results'][0]['email']
        dob = ['results'][0]['dob']['date']
        age = ['results'][0]['dob']['age']
        cell = ['results'][0]['cell']
        phone = ['results'][0]['phone']
        ssn = ['results'][0]['id']['value']
        
        me = (await event.client.get_me()).username

        valid = f"""
<b>┏━━━━━━━━━━━━━━━━━━</b>
<b>┠⌬ BIN   :</b> <code>{input} {emoji}</code>
<b>┠⌬ BRAND :</b> <code>{vendor}</code>
<b>┠⌬ TYPE  :</b> <code>{type}</code>
<b>┠⌬ LEVEL :</b> <code>{level}</code>
<b>┠⌬ BANK  :</b> <code>{bank}</code>
<b>┠⌬ COUNTRY :</b> <code>{country}</code>
<b>┗━━━━━━━━━━━━━━━━━━</b>
"""
        await xx.edit(valid, parse_mode="HTML")
    except IndexError:
       await xx.edit("Plese provide a bin to check\n__`/bin yourbin`__")
    except KeyError:
        me = (await event.client.get_me()).username
        await xx.edit(f"**❌ INVALID BIN ❌**\n\n**Bin -** `{input}`\n**Status -** `Invalid Bin`\n\n**Checked By -** @{me}\n**User-ID - {event.sender_id}**")

print ("Successfully Started")
bin.run_until_disconnected()
