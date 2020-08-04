import requests

def get_cat_pic():
    URL = 'https://api.thecatapi.com/v1/images/search?mime_types=jpg'
    response = requests.request('GET',URL).json()
    print(response)
    
    return response[0]['url']

def get_dog_pic():
    URL = 'https://api.thedogapi.com/v1/images/search?mime_types=jpg'
    response = requests.request('GET',URL).json()
    print(response)
    
    return response[0]['url']

def get_cat_gif():
    URL = 'https://api.thecatapi.com/v1/images/search?mime_types=gif'
    response = requests.request('GET',URL).json()
    print(response)
    
    return response[0]['url']

def get_dog_gif():
    URL = 'https://api.thedogapi.com/v1/images/search?mime_types=gif'
    response = requests.request('GET',URL).json()
    print(response)
    
    return response[0]['url']