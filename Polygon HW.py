import os
import time

import requests

API_BASE_URL = "https://cloud-api.yandex.net/"

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        request = requests.get(API_BASE_URL + 'v1/disk/resources/upload', params={'path': '443/'+file},
                               headers={'accept': 'application/json', 'authorization': f'OAuth {token}'})
        print(request.json())
        r = requests.put(request.json()['href'], headers={'accept': 'application/json'}, files={'file': open(file, 'rb')})


if __name__ == '__main__':
    file_name = []
    token = ''
    for file in file_name:
        path_to_file = os.path.join(os.getcwd(), file)
        uploader = YaUploader(token)
        result = uploader.upload(path_to_file)


