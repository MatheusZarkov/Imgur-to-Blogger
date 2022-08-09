# requirements.txt
        # imgurpython
        # requests
        # time
        # watchdog
        # configparser

# 1 Monitorar uma pasta
from sys import argv
import configparser
from imgurpython import ImgurClient
import sys
import time
import logging
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler


#if __name__ == "__main__":
#    logging.basicConfig(level=logging.INFO,
#                        format='%(asctime)s - %(message)s',
#                        datefmt='%Y-%m-%d %H:%M:%S')
#    path = r'C:\Users\usuario\Desktop\Testerr' # sys.argv[1] if len(sys.argv) > 1 else '.'
#    event_handler = LoggingEventHandler()
#    observer = Observer()
#    observer.schedule(event_handler, path, recursive=True)
#    observer.start()
#    try:
#        while True:
#            time.sleep(1)
#    finally:
#        observer.stop()
#        observer.join()

# 2 Upar os arquivos desta pasta para o imgur
config = configparser.ConfigParser()
config.read('Auth.ini')
client_id = config.get('Credentials', 'client_id')
client_secret = config.get('Credentials', 'client_secret')
client = ImgurClient(client_id, client_secret)

# 3 Copiar link do album no IMGUR

client = ImgurClient(client_id, client_secret)
items = client.gallery()
links = [item.link for item in items]
with open('Links.txt', 'w') as f:
    f.write('.png' '\n'.join(links)) #arrumar -> if tiver .mp4 não fazer nada, se não tiver colocar.png

# 4 Jogar um arquivo de texto com os parametros de postagem do blogger para uma pasta específica


arquivo = "Links.txt"

def Arquivoler():
    with open(arquivo, 'r') as f:
        for linha in f:
            print('<p>&nbsp;</p><div class="separator" style="clear: both; text-align: center;"><a href="',linha,'" imageanchor="1" style="margin-left: 1em; margin-right: 1em;"><img border="0" data-original-height="800" data-original-width="600" height="800" src="',linha,'" width="600" /></a></div><p></p><p><br /></p>')


        #for linha in arquivo:
         #   print(lines)


Arquivoler()

# 6 Monitorar esta pasta para novos arquivos

# 7 Abrir o Blogger pastaasiangirls e fazer novo post

# 8 Colar todos os parametros dentro post em HTML