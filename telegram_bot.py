import requests

from config import TELEGRAM_SEND_MESSAGE_URL

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
        self.last_name = message['from']['last_name']

    """
    Conditional actions based on set webhook data.

    Returns:
        bool: True if the action was completed successfully else false
    """
    def action(self):
        success = None

        if self.incoming_message_text == '/hello':
            self.outgoing_message_text = "Hello {} {}!".format(self.first_name, self.last_name)
            success = self.send_message()
        
        return success

    """
    Sends message to Telegram servers.
    """
    def send_message(self):
        res = requests.get(TELEGRAM_SEND_MESSAGE_URL.format(self.chat_id, self.outgoing_message_text))
        return True if res.status_code == 200 else False
    
    """
    Initializes the webhook

    Args:
        url:str: Provides the telegram server with a endpoint for webhook data
    """
    @staticmethod
    def init_webhook(url):
        requests.get(url)