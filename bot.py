import requests
from telethon import events, Button, TelegramClient
import os
import logging
import telegram


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

        url = requests.get(f"https://bins-su-api.now.sh/api/{input}")
        res = url.json()
        vendor = res['data']['vendor']
        type = res['data']['type']
        level = res['data']['level']
        bank = res['data']['bank']
        country = res['data']['country']
        emoji = res['data']['countryInfo']['emoji']
        me = (await event.client.get_me()).username
        
        
        valid = f"""
**┏━━━━━━━━━━━━━━━━━━**
**┠⌬ BIN   :** {input}
**┠⌬ STATS :** Valid Bin ✅
**┠⌬ BRAND :** {vendor}
**┠⌬ TYPE  :** {type}
**┠⌬ LEVEL :** {level}
**┠⌬ BANK  :** {bank}
**┠⌬ COUNTRY :** {country}
**┠⌬ FLAG  :** {emoji}
**┗━━━━━━━━━━━━━━━━━━**
"""  
        
        await xx.edit(valid, parse_mode="markdown")
    except IndexError:
       await xx.edit("Plese provide a bin to check\n__`/bin yourbin`__")
    except KeyError:
        me = (await event.client.get_me()).username
        await xx.edit(f"**❌ INVALID BIN ❌**\n\n**Bin -** `{input}`\n**Status -** `Invalid Bin`\n\n**Checked By -** @{me}\n**User-ID - {event.sender_id}**")
    
print ("Successfully Started")
bin.run_until_disconnected()
