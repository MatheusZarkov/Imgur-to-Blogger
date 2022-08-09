from imgurpython import ImgurClient
import os
import configparser
config = configparser.ConfigParser()
config.read('Auth.ini')
client_id = config.get('Credentials', 'client_id')
client_secret = config.get('Credentials', 'client_secret')
client = ImgurClient(client_id, client_secret)


class Uploader():
    def __init__(self):
        pass

    def upador(self):
        path = (r'C:\Users\usuario\Desktop\Blogger poster\ ')
        for items in path:
            ImgurClient.upload_from_path(items, path, config=client_id, anon=False)
            print(upador, items.link)

p = Uploader()
p.upador()