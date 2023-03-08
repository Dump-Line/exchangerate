import telebot
import config
from flask import Flask


app = Flask(__name__)
bot = telebot.TeleBot(config.TOKEN, skip_pending=True)







