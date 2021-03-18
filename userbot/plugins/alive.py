"""عند الشك من توقف التيليثون لديك 
قم بارسال امر .alive """
import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from platform import uname
from userbot import ALIVE_NAME
from userbot.utils import admin_cmd

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "**No Name set yet.** [Check Guide.](https://how2techy.com/xtra-guide1/)"

@command(outgoing=True, pattern="^.alive$")
async def amireallyalive(alive):
    """ For .alive command, check if the bot is running.  """
    await alive.edit("ان حسابك نشط اطمئن ✅"
                     
                     
                     "تم انشاء البوت من قبل : [- ᴀʜᴍᴀᴅ ᴀʟ ʙᴀʀᴏɴ⁦ .](tg://user?id=801023241)" 
                   "لـ  {DEFAULTUSER}"
                     "قناتي ~ [- B ʟ ᴀ ᴄ ᴋ T ᴇ ᴀ ᴍ.](https://t.me/cqcqq)"
