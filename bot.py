from selenium import webdriver
import time
import os
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import os
import time
import requests

dir_path = os.getcwd() #criar pastas
chrome_options2 = Options()
chrome_options2.add_argument(r"user-data-dir=" + dir_path + "profile/zap") # adiciona os argumentos de options e concatena com a variável de criar pastas - salvar a seção dentro da pasta atual do sistema
driver = webdriver.Chrome(chrome_options2)
driver.get('https://web.whatsapp.com/')

# API
agent = {"User-Agent": 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'}

# CHAVE
api = requests.get("https://editacodigo.com.br/index/api-whatsapp/Udezw2NmFmDqajjP0nPvOleGMHKoLq1J" ,  headers=agent)


time.sleep(60)

api = api.text
api = api.split(".n.")
bolinha_notificacao = api[3].strip()
contato_cliente = api[4].strip()
caixa_msg = api[5].strip()
msg_cliente = api[6].strip()
caixa_msg2 = api[7].strip()
caixa_pesquisa = api[8].strip()
