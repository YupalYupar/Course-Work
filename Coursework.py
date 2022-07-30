with open('VKtoken.txt', 'r') as file_object:
    token = file_object.read().strip()

import json
import yadisk
import time
import requests
from pprint import pprint


URL = 'https://api.vk.com/method/photos.get'
params = {
    'access_token': token,
    'v':'5.131',
    'album_id': 'profile',
    'extended': 'likes',
    'photo_sizes' : 'z'
}

photo_dict = {}
res = requests.get(URL, params=params)
res_dict = res.json()['response']['items']

for i in res_dict:
    photo_name = str(i['likes']['count']) + '-' + str(i['date'])
    photo_url = str(i['sizes'][-1]['url'])
    imag = requests.get(photo_url)
    picture_name = photo_name + '.jpg'
    with open(picture_name,'wb') as fila:
        fila.write(imag.content)
    y = yadisk.YaDisk(token='')
    y.upload(picture_name,f"/photoes/{picture_name}")
