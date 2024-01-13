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

#------------------------------------------------------------------------------------------------------
# API do Edita Código 
# https://editacodigo.com.br/index/api-whatsapp

## API
agent = {"User-Agent": 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'}

## CHAVE
api = requests.get("https://editacodigo.com.br/index/api-whatsapp/Udezw2NmFmDqajjP0nPvOleGMHKoLq1J" ,  headers=agent)

#------------------------------------------------------------------------------------------------------

api = api.text
api = api.split(".n.")
bolinha_notificacao = api[3].strip()
contato_cliente = api[4].strip()
caixa_msg = api[5].strip()
msg_cliente = api[6].strip()
caixa_msg2 = api[7].strip()
caixa_pesquisa = api[8].strip()

dir_path = os.getcwd() #criar pastas
chrome_options2 = Options()
chrome_options2.add_argument(r"user-data-dir=" + dir_path + "profile/zap") # adiciona os argumentos de options e concatena com a variável de criar pastas - salvar a seção dentro da pasta atual do sistema
driver = webdriver.Chrome(chrome_options2)
driver.get('https://web.whatsapp.com/')
time.sleep(10)

def bot():
    try:
        
        #CAPTURAR A BOLINHA
        bolinha = driver.find_element(By.CLASS_NAME,bolinha_notificacao)
        bolinha = driver.find_elements(By.CLASS_NAME,bolinha_notificacao)
        clica_bolinha = bolinha[-1]
        acao_bolinha = webdriver.common.action_chains.ActionChains(driver)
        acao_bolinha.move_to_element_with_offset(clica_bolinha,0,-20)
        acao_bolinha.click()
        acao_bolinha.perform()
        acao_bolinha.click()
        acao_bolinha.perform()
        time.sleep(1)

        #PEGAR O TELEFONE
        telefone_cliente = driver.find_element(By.XPATH,'//*[@id="main"]/header/div[2]/div/div/span')
        telefone_final = telefone_cliente.text 
        print(telefone_final)
        time.sleep(1)








        #l7jjieqr cfzgl7ar ei5e7seu h0viaqh7 tpmajp1w c0uhu3dl riy2oczp dsh4tgtl sy6s5v3r gz7w46tb lyutrhe2 qfejxiq4 fewfhwl7 ovhn1urg ap18qm3b ikwl5qvt j90th5db aumms1qt
        #faça isso aqui 
        #caso nao consiga, tenta uma outra coisa

    except:
        print('ola')
        #entao vou tentar isso aqui 



while True:
    bot()
