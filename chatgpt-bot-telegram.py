import telebot
import openai

openai.api_key = "TU SECRET KEY DE OPENAI"

bot = telebot.TeleBot(token="EL TOKEN QUE TE DA BOTFATHER DE TELEGRAM")

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

bot.polling()
