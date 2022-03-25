import pytest
import requests
from main import YaNewFolder


TOKEN = ''

fixture1 = [
    '1',
    '12',
    'HI 123',
    '45667Hello',
    'New Folder'
]

class TestNewFolder:

    @pytest.mark.parametrize('folder', fixture1)
    def test_new_folder_correct(self, folder):
        ya_new_folder = YaNewFolder(TOKEN)
        assert ya_new_folder.put_new_folder(folder) in range(200, 299)

    def test_new_folder_empty(self):
        ya_new_folder = YaNewFolder(TOKEN)
        assert ya_new_folder.put_new_folder('') in range(400, 499)

    def test_new_folder_symbols(self):
        ya_new_folder = YaNewFolder(TOKEN)
        assert ya_new_folder.put_new_folder('/') in range(400, 499)