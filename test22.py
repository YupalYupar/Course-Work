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
TOKEN = ''
def creating_folder(path):
    URL = 'https://cloud-api.yandex.net/v1/disk/resources'
    token = TOKEN
    headers = {'Content-Type': 'application/json', 'Accept': 'application/json', 'Authorization': f'OAuth {TOKEN}'}
    requests.put(f'{URL}?path={path}', headers=headers)
#creating_folder('photoes')

def uploadin_photoes():
    res = requests.get(URL, params=params)
    res_dict = res.json()['response']['items']
    for i in res_dict:
        photo_name = str(i['likes']['count']) + '-' + str(i['date'])
        photo_url = str(i['sizes'][-1]['url'])
        imag = requests.get(photo_url)
        picture_name = photo_name + '.jpg'
        with open(picture_name,'wb') as fila:
            fila.write(imag.content)
        y = yadisk.YaDisk(token=TOKEN)
        y.upload(picture_name,f"/photoes/{picture_name}")
#uploadin_photoes()

if __name__ == "__main__":
    creating_folder('photoes')
    uploadin_photoes()
