# Original concept adapted from https://medium.com/daily-python/python-script-to-generate-meme-daily-python-11-e08aee07e940

import requests
import urllib

from env import IMGFLIP_USERNAME, IMGFLIP_PASSWORD

def fetch_meme():

    data = requests.get('https://api.imgflip.com/get_memes').json()['data']['memes']
    images = [{'name':image['name'],'url':image['url'],'id':image['id']} for image in data]

    return images

def fetch_meme_list():
    i = 1
    meme_list = ""
    for img in fetch_meme():
        meme_list = meme_list + str(i) + ' ' + img['name'] + '\n'
        i = i+1
    
    return meme_list

def generate_meme(incoming_text):

    images = fetch_meme()

    id = int(incoming_text.split("_")[1])
    if id > 100:
        id = id % 100
    text0 = incoming_text.split("_")[2]
    text1 = incoming_text.split("_")[3]

    #Fetch the generated meme
    URL = 'https://api.imgflip.com/caption_image'
    params = {
        'username':IMGFLIP_USERNAME,
        'password':IMGFLIP_PASSWORD,
        'template_id':images[id-1]['id'],
        'text0':text0,
        'text1':text1
    }
    response = requests.request('POST',URL,params=params).json()
    print(response)
    
    return response['data']['url']