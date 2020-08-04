TELEGRAM_TOKEN = ''
APP_URL = ''

IMGFLIP_USERNAME = ''
IMGFLIP_PASSWORD = ''

BASE_TELEGRAM_URL = 'https://api.telegram.org/bot{}'.format(TELEGRAM_TOKEN)
LOCAL_WEBHOOK_ENDPOINT = '{}/webhook'.format(APP_URL)
TELEGRAM_INIT_WEBHOOK_URL = '{}/setWebhook?url={}'.format(BASE_TELEGRAM_URL, LOCAL_WEBHOOK_ENDPOINT)
TELEGRAM_SEND_MESSAGE_URL = BASE_TELEGRAM_URL + '/sendMessage?chat_id={}&text={}'
TELEGRAM_SEND_ANIMATION_URL = BASE_TELEGRAM_URL + '/sendAnimation?chat_id={}&animation={}'
TELEGRAM_SEND_PHOTO_URL = BASE_TELEGRAM_URL + '/sendPhoto?chat_id={}&photo={}'
TELEGRAM_SEND_VOICE_URL = BASE_TELEGRAM_URL + '/sendVoice?chat_id={}&voice={}'