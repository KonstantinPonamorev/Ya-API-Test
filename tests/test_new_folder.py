import pytest
import requests
from main import YaNewFolder

fixture = [
    '123',
    'NewFolder',
    'SomeFolder1',
    '1BestFolder'
]

class TestNewFolder:

    @pytest.mark.parametrize('folder', fixture)
    def test_new_folder_correct(self, folder):
        token = input('Введите токен')
        ya_new_folder = YaNewFolder(token)
        assert ya_new_folder.put_new_folder(folder) == #Параметр Response

    # def test_new_folder_empty(self):
    #     token = input('Введите токен')
    #     ya_new_folder = YaNewFolder(token)
    #
    # def test_new_folder_symbols(self):
    #     token = input('Введите токен')
    #     ya_new_folder = YaNewFolder(token)


