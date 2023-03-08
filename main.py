import json
import telebot
import config
import time
from app import bot
import requests


while 1:
	url = 'https://garantex.io/api/v2/trades?market=usdtrub&limit=1'
	page = requests.get(url)
	bot.send_message(config.CHAT_ID, f"USDT/RUB: 	{page.json()[0]['price']}")
	time.sleep(70)





"""

@app.route('/' + config.TOKEN, methods=['POST'])
def getMessage():
	bot.process_new_updates([telebot.telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
	return "!", 200


@app.route("/")
def webhook():
	bot.remove_webhook()
	bot.set_webhook(url=config.DOKKU_LINK + config.TOKEN)
	return "!", 200


# Получаем новые сообщения
if __name__ == "__main__":
	app.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000))) 
	print("START")

"""

bot.remove_webhook()
if __name__ == '__main__':
	bot.polling(none_stop=True)
	








	
