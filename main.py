import os
from pyrogram import Client, filters
from pyrogram.types import Message

API_ID = int(os.environ.get("API_ID"))
API_HASH = os.environ.get("API_HASH")
BOT_TOKEN = os.environ.get("BOT_TOKEN")

app = Client(
    "auto_ban_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

@app.on_message(filters.left_chat_member)
async def auto_ban(client: Client, message: Message):
    user = message.left_chat_member
    chat_id = message.chat.id

    try:
        await client.ban_chat_member(chat_id, user.id)
        await message.reply_text(
            f"🚫 {user.mention} group leave kiya tha.\nPermanent ban kar diya gaya."
        )
    except Exception as e:
        print(e)

print("Bot Started ✅")
app.run()
