with open('token.txt', 'r') as file_object:
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

res = requests.get(URL, params=params)
res_dict = res.json()['response']['items']
for i in res_dict:
    photo_name = str(i['likes']['count']) + '-' + str(i['date'])
    photo_url = str(i['sizes'][-1]['url'])

    token = ""
    headers = {'Content-Type': 'application/json','Authorization': 'OAuth {}'.format(token)}
    upload_url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'

    params = {'path': photo_url, "overwrite": "true"}

    response = requests.get(upload_url, headers=headers, params=params).json()

    url = response.get("href", "")

    resp = requests.post(url, data=open(photo_name, 'rb'))
