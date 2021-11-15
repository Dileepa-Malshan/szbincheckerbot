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

        url = requests.get(f"https://randomuser.me/api/")
        res = url.json()
        gender = res['results'][0]['gender']
        name = res['results'][0]['name']
        location = res['results'][0]['location']
        birthday = res['results'][0]['dob']
        valid = f"""
<b>┏━━━━━━━━━━━━━━━━━━</b>
<b>┠⌬ GENDER :</b> <code>{gender}</code>
<b>┠⌬ NAME  :</b> <code>{name}</code>
<b>┠⌬ LOCATION :</b> <code>{location}</code>
<b>┠⌬ BIRTHDAY  :</b> <code>{dob}</code>
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
import requests
import json

servers=json.loads(requests.get('https://single-developers.herokuapp.com/servers').content)
for server in servers:
    id=str(server)
    ip=servers[str(server)]['ip']
    location=servers[str(server)]['location']
    emoji=servers[str(server)]['emoji']
    print(
f"""◇ Server ID : {id}
◇ Server Host : {ip}
◇ Server Location : {emoji} {location} {emoji}
""")
serverid=input('Server ID : ')

server=json.loads(requests.get(f'https://single-developers.herokuapp.com/servers?id={serverid}').content)
status=requests.get(f'https://single-developers.herokuapp.com/servers?status={serverid}').content
ip=server['ip']
location=server['location']
emoji=server['emoji']
print(
f"""
◇ Server ID : {serverid}
◇ Server Host : {ip}
◇ Server Location : {emoji} {location} {emoji}

◇ Server Status : {str(status)}"""
)

username=input('User Name : ')
password=input('Password : ')

ssh=serverid+'$'+username+'$'+password
ssh_result=requests.get(f'https://single-developers.herokuapp.com/create?ssh={str(ssh)}').content
try:
    json_ssh=json.loads(ssh_result)
    user_name=json_ssh['username']
    passwd=json_ssh['password']
    port=json_ssh['port']
    ex_date=json_ssh['ex_date']
    login=json_ssh['login']
    print(
f"""
◇ Server Location : {emoji} {location} {emoji}

◇ Server Host : {ip}
◇ SSL Port : {port}
◇ User Name : {user_name}
◇ Password : {passwd}
◇ Expire Date : {ex_date}
◇ Login : {login}

<  https://t.me/SingleDevelopers  />"""
)
except:
    print(ssh_result)
