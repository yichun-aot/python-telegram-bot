# -*- coding: utf-8 -*-
import requests
import re

from env import TELEGRAM_SEND_MESSAGE_URL, TELEGRAM_SEND_PHOTO_URL, TELEGRAM_SEND_ANIMATION_URL, TELEGRAM_SEND_VOICE_URL
from modules.meme import fetch_meme_list, generate_meme
from modules.animal_pic import get_cat_pic, get_dog_pic, get_cat_gif, get_dog_gif
from modules.voice import generate_voice

class TelegramBot:

    """
    Initializes an instance of the TelegramBot class.

    Attributes:
        chat_id:str: Chat ID of Telegram chat, used to identify which conversation outgoing messages should be send to.
        text:str: Text of Telegram chat
        first_name:str: First name of the user who sent the message
        last_name:str: Last name of the user who sent the message
    """
    def __init__(self):
        self.chat_id = None
        self.text = None
        self.first_name = None
        self.last_name = None
        self.username = None

    """
    Parses Telegram JSON request from webhook and sets fields for conditional actions

    Args:
        data:str: JSON string of data
    """
    def parse_webhook_data(self, data):
        message = data['message']
        self.chat_id = message['chat']['id']
        self.incoming_message_text = message['text'].lower()
        self.first_name = message['from']['first_name']
        # self.last_name = message['from']['last_name']

    """
    Conditional actions based on set webhook data.

    Returns:
        bool: True if the action was completed successfully else false
    """
    def action(self):
        success = None

        help_text = "\n\nSend '/meme' to begin generating your own meme! \nSend '/dogpic'; '/doggif'; '/catpic'; '/catgif' to get your animal pictures!"

        if self.incoming_message_text == '/hello':
            self.outgoing_message_text = "Hello {}! This is Yichun Number 2 here. How can I help you today? 😉".format(self.first_name) + help_text
            success = self.send_message()
        elif self.incoming_message_text == '/meme':
            self.outgoing_message_text = "This is a list of memes which you can generate...\n\n" + fetch_meme_list() + "\n\nPlease reply in the format of '/meme_memeID_text1_text2' \n- i.e. '/meme_1_Hello_Bye'. Thanks! 🤩"
            success = self.send_message()
        # Format of incoming reply has to be '/meme_1_text1_text2' with regex pattern /meme_(\d)*_(.)*_(.)*
        elif re.match(r"/meme_(\d)+_(.)+_(.)+", self.incoming_message_text):
            self.outgoing_photo_str = generate_meme(self.incoming_message_text)
            success = self.send_photo()
        elif self.incoming_message_text == '/dogpic':
            self.outgoing_photo_str = get_dog_pic()
            success = self.send_photo()
        elif self.incoming_message_text == '/catpic':
            self.outgoing_photo_str = get_cat_pic()
            success = self.send_photo()
        elif self.incoming_message_text == '/doggif':
            self.outgoing_animation_str = get_dog_gif()
            success = self.send_animation()
        elif self.incoming_message_text == '/catgif': 
            self.outgoing_animation_str = get_cat_gif()
            success = self.send_animation()
        elif self.incoming_message_text =='/voice':
            self.outgoing_message_text = "Please reply in the format of '/voice_text' \n- i.e. '/voice_How are you?'. Thanks! 🤩"
            success = self.send_message()
        elif re.match(r"/voice_(.)+", self.incoming_message_text):
            self.outgoing_voice_str = generate_voice(self.incoming_message_text)
            success = self.send_voice()
        else:
            self.outgoing_message_text = "I am afraid that I do not understand you.. Do you want to try again? 🤪" + help_text
            success = self.send_message()
        
        return success

    """
    Sends message to Telegram servers.
    """
    def send_message(self):
        res = requests.get(TELEGRAM_SEND_MESSAGE_URL.format(self.chat_id, self.outgoing_message_text))
        return True if res.status_code == 200 else False
    
    def send_photo(self):
        res = requests.get(TELEGRAM_SEND_PHOTO_URL.format(self.chat_id, self.outgoing_photo_str))
        return True if res.status_code == 200 else False

    def send_animation(self):
        res = requests.get(TELEGRAM_SEND_ANIMATION_URL.format(self.chat_id, self.outgoing_animation_str))
        return True if res.status_code == 200 else False

    def send_voice(self):
        res = requests.get(TELEGRAM_SEND_VOICE_URL.format(self.chat_id, self.outgoing_voice_str))
        return True if res.status_code == 200 else False

    """
    Initializes the webhook

    Args:
        url:str: Provides the telegram server with a endpoint for webhook data
    """
    @staticmethod
    def init_webhook(url):
        requests.get(url)