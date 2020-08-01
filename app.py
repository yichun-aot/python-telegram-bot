from flask import Flask, request, jsonify

from telegram_bot import TelegramBot
from config import TELEGRAM_INIT_WEBHOOK_URL

# Create app object which is our app server
app = Flask(__name__)

# Provides the telegram server with our Ngrok URL
TelegramBot.init_webhook(TELEGRAM_INIT_WEBHOOK_URL)

# Actual local endpoint
@app.route('/webhook', methods=['POST'])
def index():
    # Get Json data
    req = request.get_json()
    # Create bot object
    bot = TelegramBot()
    # Feed Json data to the bot
    bot.parse_webhook_data(req)
    # Get action from bot depending on the Json data
    success = bot.action()
    # Respond the boolean value of success to Telegram server to not repeat sending the data
    return jsonify(success=success) # TODO: Success should reflect the success of the reply

# Only execute if the current py script is executed by itself, not other modules
if __name__ == '__main__':
    app.run(port=5000)


# https://telegram.me

# check bot initialization: https://api.telegram.org/bot<822448732:AAGUNRBnPPHjVhOqySQZk_QzP_VaZhgx9i0>/getme
# check webhook url: https://api.telegram.org/bot822448732:AAGUNRBnPPHjVhOqySQZk_QzP_VaZhgx9i0/getWebhookInfo