import os
import sys
import asyncio
from random import choice
from SpamX import (OWNER_ID, HNDLR, SUDO_USERS, LOGS_CHANNEL)
from pyrogram import Client, filters
from pyrogram.types import Message
from SpamX.data import *

Usage = f"**❌ Wrong Usage ❌** \n Type: `{HNDLR}help dm`"

@Client.on_message(filters.user(SUDO_USERS) & filters.command(["dmraid"], prefixes=HNDLR))
async def dmraid(xspam: Client, e: Message):
      """ Module: Dm Raid """
      chankit = "".join(e.text.split(maxsplit=1)[1:]).split(" ", 2)
      if len(chankit) == 2:
          ok = await xspam.get_users(chankit[1])
          id = ok.id
          if int(id) in Neurons:
                text = f"I can't raid on @NeuroticAssociation's Owner"
                await e.reply_text(text)
          elif int(id) == OWNER_ID:
                text = f"This guy is Owner Of this Bots."
                await e.reply_text(text)
          elif int(id) in SUDO_USERS:
                text = f"This guy is a sudo user."
                await e.reply_text(text)
          else:
              counts = int(chankit[0])
              await e.reply_text("⚜️ Dm Raid Started Successfully ⚜️")
              for _ in range(counts):
                    reply = choice(RAID)
                    msg = f"{reply}"
                    await xspam.send_message(id, msg)
                    await asyncio.sleep(0.10)
      elif e.reply_to_message:
          user_id = e.reply_to_message.from_user.id
          ok = await xspam.get_users(user_id)
          id = ok.id
          if int(id) in Neurons:
                text = f"I can't raid on @NeuroticAssociation's Owner"
                await e.reply_text(text)
          elif int(id) == OWNER_ID:
                text = f"This guy is Owner Of this Bots."
                await e.reply_text(text)
          elif int(id) in SUDO_USERS:
                text = f"This guy is a sudo user."
                await e.reply_text(text)
          else:
              counts = int(chankit[0])
              await e.reply_text("⚜️ Dm Raid Started Successfully ⚜️")
              for _ in range(counts):
                    reply = choice(RAID)
                    msg = f"{reply}"
                    await xspam.send_message(id, msg)
                    await asyncio.sleep(0.10)
      else:
          await xspam.reply_text(Usage)
      if LOGS_CHANNEL:
         try:
            await xspam.send_message(LOGS_CHANNEL, f"started DM Raid By User: {e.from_user.id} \n\n On User: {id} \n Counts: {counts}")
         except Exception as a:
             print(a)
             pass
         
@Client.on_message(filters.user(SUDO_USERS) & filters.command(["dm"], prefixes=HNDLR))
async def dm(xspam: Client, e: Message):
      chankit = "".join(e.text.split(maxsplit=1)[1:]).split(" ", 2)
      if len(chankit) == 2:
          usr = str(chankit[0])
          ok = await xspam.get_users(usr)
          id = ok.id
          if int(id) in Neurons:
                text = f"I can't raid on @NeuroticAssociation's Owner"
                await e.reply_text(text)
          elif int(id) == OWNER_ID:
                text = f"This guy is Owner Of this Bots."
                await e.reply_text(text)
          elif int(id) in SUDO_USERS:
                text = f"This guy is a sudo user."
                await e.reply_text(text)
          else:
              msg = str(chankit[1])
              await e.reply_text("🔸 Message Delivered 🔸")
              await xspam.send_message(id, msg)
      elif e.reply_to_message:
          user_id = e.reply_to_message.from_user.id
          ok = await xspam.get_users(user_id)
          id = ok.id
          if int(id) in Neurons:
                text = f"I can't raid on @NeuroticAssociation's Owner"
                await e.reply_text(text)
          elif int(id) == OWNER_ID:
                text = f"This guy is Owner Of this Bots."
                await e.reply_text(text)
          elif int(id) in SUDO_USERS:
                text = f"This guy is a sudo user."
                await e.reply_text(text)
          else:
              msg = str(chankit[0])
              await e.reply_text("🔸 Message Delivered 🔸️")
              await xspam.send_message(id, msg)
      else:
          await xspam.reply_text(Usage)
      if LOGS_CHANNEL:
         try:
            await xspam.send_message(LOGS_CHANNEL, f"Direct Message By User: {e.from_user.id} \n\n On User: {id}")
         except Exception as a:
             print(a)
             pass



@Client.on_message(filters.user(SUDO_USERS) & filters.command(["dmspam"], prefixes=HNDLR))
async def dmspam(xspam: Client, e: Message):
      chankit = "".join(e.text.split(maxsplit=1)[1:]).split(" ", 2)
      chankitop = chankit[1:]
      if len(chankitop) == 2:
          msg = str(chankitop[1])
          ok = await xspam.get_users(chankit[0])
          id = ok.id
          if int(id) in Neurons:
                text = f"I can't raid on @NeuroticAssociation's Owner"
                await e.reply_text(text)
          elif int(id) == OWNER_ID:
                text = f"This guy is Owner Of this Bots."
                await e.reply_text(text)
          elif int(id) in SUDO_USERS:
                text = f"This guy is a sudo user."
                await e.reply_text(text)
          else:
              counts = int(chankitop[0])
              await e.reply_text("☢️ Dm Spam Started ☢️")
              for _ in range(counts):
                    await xspam.send_message(id, msg)
                    await asyncio.sleep(0.10)
      elif e.reply_to_message:
          user_id = e.reply_to_message.from_user.id
          ok = await xspam.get_users(user_id)
          id = ok.id
          if int(id) in Neurons:
                text = f"I can't raid on @NeuroticAssociation's Owner"
                await e.reply_text(text)
          elif int(id) == OWNER_ID:
                text = f"This guy is Owner Of this Bots."
                await e.reply_text(text)
          elif int(id) in SUDO_USERS:
                text = f"This guy is a sudo user."
                await e.reply_text(text)
          else:
              counts = int(chankit[0])
              msg = str(chankitop[0])
              await e.reply_text("☢️ Dm Spam Started ☢️")
              for _ in range(counts):
                    await xspam.send_message(id, msg)
                    await asyncio.sleep(0.10)
      else:
          await xspam.reply_text(Usage)
      if LOGS_CHANNEL:
         try:
            await xspam.send_message(LOGS_CHANNEL, f"started DM Spam By User: {e.from_user.id} \n\n On User: {id} \n Counts: {counts} \n Message: {msg}")
         except Exception as a:
             print(a)
             pass
