import requests
from pprint import pprint


class YaNewFolder:
    def __init__(self, token: str):
        self.token = token

    def get_headers(self):
        return {'Content-Type': 'application/json',
                'Authorization': f'OAuth {self.token}'}

    def put_new_folder(self, folder_name):
        new_folder_url = 'https://cloud-api.yandex.net/v1/disk/resources'
        headers = self.get_headers()
        params = {'path': folder_name}
        response = requests.put(new_folder_url, headers=headers, params=params)
        print(response.status_code)
        return response.status_code

if __name__ == '__main__':
    token = input('Введите ваш Token: ')
    folder_name = input('Введите название папки')
    ya_new_folder = YaNewFolder(token)
    result = ya_new_folder.put_new_folder(folder_name)