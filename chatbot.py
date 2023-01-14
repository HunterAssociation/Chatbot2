import pyrogram
from pyrogram import Client, filters
from pyrogram.types import Message
import telebot
import openai

openai.api_key = "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"

bot = telebot.TeleBot(token="5943097003:AAFAYW8r-EBn3yWIqqELWVivGxHLggnt0dI")

def generate_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        temperature=0.5,
)

    return response["choices"][0]["text"]

bot.set_my_commands([
    {
        "command": "/chat", "/ai"
        "description": "Kirim pesan ke Bot dengan cara /chat <pesan>"
    }
])

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    AUTHORIZED_USER_IDS = ['']
    text = message.text
    response = generate_response(text)

    bot.send_message(chat_id=message.chat.id, text=response)
    #else:
        #bot.send_message(chat_id=message.chat.id, text="You are not authorized to receive responses from this bot.")

@Client.on_message(filters.command(["start"]))
async def start(client, message):
        await message.reply("Halo...")

bot.polling()
