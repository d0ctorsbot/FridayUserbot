"""Check if userbot alive. If you change these, you become the gayest gay such that even the gay world will disown you."""
#IMG CREDITS: @WhySooSerious
import asyncio
from telethon import events
from uniborg.util import admin_cmd
from userbot import ALIVE_NAME
from telethon.tl.types import ChannelParticipantsAdmins
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Unknown"
ALIVE_STCR = "https://telegra.ph/Friday-Is-Online-07-15"
pm_caption = "`FRIDAY IS:` **ONLINE**\n\n"

pm_caption += "**SYSTEM STATUS**\n"


pm_caption += "`TELETHON VERSION:` **6.0.9**\n`Python:` **3.7.4**\n"

pm_caption += "`DATABASE STATUS:` **Functional**\n"

pm_caption += "**Current Branch** : `Nimeshchandhra1-patch-1`\n"

pm_caption += "**Friday OS** : `3.14`\n"

pm_caption += "**Current Sat** : `Sat-2.25`\n"

pm_caption += f"**My Boss** : {DEFAULTUSER} \n"

pm_caption += "**Heroku Database** : `AWS - Working Properly`\n\n"
#@command(outgoing=True, pattern="^.alive$")
@borg.on(admin_cmd(pattern=r"alive"))
async def amireallyalive(alive):
    chat = await alive.get_chat()
    await alive.delete()
    """ For .alive command, check if the bot is running.  """
    await borg.send_file(alive.chat_id, ALIVE_STCR,caption=pm_caption)
    await alive.delete() 
    
