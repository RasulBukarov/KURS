# from itertools import count
import requests
Yandex_disk = "AQAAAABefF29AADLW0VrHjnxEU7omLOK6m5nbe4"
id = 8099964
TOKEN = "958eb5d439726565e9333aa30e50e0f937ee432e927f0dbd541c541887d919a7c56f95c04217915c32008"
URL = 'https://api.vk.com/metho+d/photos.getAll' 
offset = 0

class VK_USER:
    def __init__(self, Yandex_disk, id):
        self.Yandex_disk = Yandex_disk
        self.id = id
    def info_photo(self, URL, offset):
        params = {
            'access_token' : TOKEN,
            'owner_id' : id,
            'album_id' : 'profile',
            'count' : '1',
            'v' : '5.131',
            'extended' : '1',
            'offset' : offset
        }
        resp = requests.get(URL, params).json()['response']
        response = resp['items']
        return response
    def save_photo_album(self, offset):
        req = Mikhail.info_photo(URL, offset=offset)
        for el in req:
            date = el['date']
            count = 0
            for i in el['sizes']:
                if i['type'] != 'z':
                    count += 1
                else:
                    break
            url = el['sizes']['count']['url']
            like = el['likes']['count']
            file_name = 'photosVK/' + str(like) + '_' + str(date) + '.jpg'
            list = []
            dict = {}
            dict["filename"] = file_name
            dict["size"] = "z"
            list.append(dict)
            URL_upload = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
            params = {'url': url, 'path': file_name, 'overwrite': 'true'}
            headers = {
                'Content-Type': 'application/json',
                'Authorization': 'OAuth {}'.format(Yandex_disk)
            }
            resp = requests.post(url=URL_upload, params=params, headers=headers)
Mikhail = VK_USER(Yandex_disk, id)
count_photo = 5
params = {
    'access_token': TOKEN,
    'owner_id': id,
    'album_id': 'profile',
    'count': '1',
    'v': '5.131',
    'extended': '1',
    'offset': offset
}
# count_photo = requests.get(URL, params).json()['response']['count']
count_photo=input('Введите число фотографий, которое вы хотите сохранить. '
                  'Если хотите сохранить все фото - напишите "+"'
                  ' По умолчанию программа сохраняет 5 фото.')
if count_photo == '+':
    count_photo = requests.get(URL, params).json()['response']['count']
else:
    count_photo = int(count_photo)
from tqdm import tqdm
for i in tqdm(range(count_photo)):
    offset += 1
    Mikhail.save_photo_album(offset=offset)
