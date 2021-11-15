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
        first = res['results']['name']['first']
        last =  res['results']['name']['last']
        gend = res['results']['gender']
        street = res['results']['location']['street']
        city = res['results']['location']['city']
        state = res['results']['location']['state']
        email = res['results']['email']
        dob = res['results']['dob']['date']
        age = res['results']['dob']['age']
        cell = res['results']['cell']
        phone = res['results']['phone']
        ssn = res['results']['id']['value']
        me = (await event.client.get_me()).username

        valid = f"""
<b>┏━━━━━━━━━━━━━━━━━━</b>
<b>┠⌬ FIRST NAME :</b> <code>{first} {last}</code>
<b>┠⌬ GENDER :</b> <code>{gend}</code>
<b>┠⌬ STREET  :</b> <code>{street}</code>
<b>┠⌬ CITY :</b> <code>{city}</code>
<b>┠⌬ STATE  :</b> <code>{state}</code>
<b>┠⌬ BIRTHDAY :</b> <code>{dob}</code>
<b>┠⌬ AGE :</b> <code>{age}</code>
<b>┠⌬ SSN:</b> <code>{ssn}</code>
<b>┠⌬ CELL :</b> <code>{cell}</code>
<b>┠⌬ PHONE :</b> <code>{phone}</code>
<b>┠⌬ EMAIL :</b> <code>{email}</code>
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
