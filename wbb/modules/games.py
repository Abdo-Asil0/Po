from pyrogram import filters
from pyrogram.types import Message

from wbb import SUDOERS, app

__MODULE__ = "Games 🎁"
__HELP__ = """
Use these commands and try to score.\n\n
/dice - Dice 🎲\n
/dart - Dart 🎯\n
/basket - Basket Ball 🏀\n
/bowling - Bowling Ball 🎳\n
/football - Football ⚽\n
/slot - Spin slot machine 🎰
"""

@app.on_message(filters.command("dice"))
async def throw_dice(client, message: Message): 
    await client.send_dice(message.chat.id, "🎲")

@app.on_message(filters.command("dart"))
async def throw_dice(client, message: Message): 
    await client.send_dice(message.chat.id, "🎯")

@app.on_message(filters.command("basket"))
async def throw_dice(client, message: Message): 
    await client.send_dice(message.chat.id, "🏀")

@app.on_message(filters.command("bowling"))
async def throw_dice(client, message: Message): 
    await client.send_dice(message.chat.id, "🎳")

@app.on_message(filters.command("football"))
async def throw_dice(client, message: Message): 
    await client.send_dice(message.chat.id, "⚽")

@app.on_message(filters.command("slot"))
async def throw_dice(client, message: Message): 
    await client.send_dice(message.chat.id, "🎰")