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
time.sleep(1)
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

def mostrar_menu():
    menu = str("Olá, eu sou o seu assistente virtual. Como posso ajudá-lo hoje? Digite o número correspondente à sua escolha: \n 1 - Status do pedido \n 2 - Suporte técnico \n 3 - Feedback\n 4 - Falar com um atendente humano")
    return menu

menu = mostrar_menu()
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
        telefone_cliente = driver.find_element(By.XPATH,contato_cliente)
        telefone_final = telefone_cliente.text 
        print(telefone_final)
        time.sleep(1)

        # Capturando a mensagem do cliente
        todas_as_msg = driver.find_elements(By.CLASS_NAME,msg_cliente)
        todas_as_msg_texto = [e.text for e in todas_as_msg]
        msg = todas_as_msg_texto[-1]
        time.sleep(5)
        if msg.isdigit():
            numero1 = int(msg)
            if numero1 == 1:
                campo_de_texto = driver.find_element(By.XPATH,caixa_msg)
                campo_de_texto.click()
                time.sleep(1)
                campo_de_texto.send_keys('resposta 1', Keys.ENTER)
            elif numero1 == 2:
                campo_de_texto = driver.find_element(By.XPATH,caixa_msg)
                campo_de_texto.click()
                campo_de_texto.send_keys('resposta 2', Keys.ENTER)
                time.sleep(1)

            elif numero1 == 3:
                campo_de_texto = driver.find_element(By.XPATH,caixa_msg)
                campo_de_texto.click()
                time.sleep(1)
                campo_de_texto.send_keys('resposta 3', Keys.ENTER)

            else:
                campo_de_texto = driver.find_element(By.XPATH,caixa_msg)
                campo_de_texto.click()
                time.sleep(1)
                campo_de_texto.send_keys('resposta 4', Keys.ENTER)

        else:
            campo_de_texto = driver.find_element(By.XPATH,caixa_msg)
            campo_de_texto.click()
            time.sleep(1)
            campo_de_texto.send_keys(menu, Keys.ENTER)        
        # print(msg)
        

        # #Respondendo o cliente
        # campo_de_texto = driver.find_element(By.XPATH,caixa_msg)
        # campo_de_texto.click()
        # time.sleep(1)
        # if msg == 1:
        #     campo_de_texto.send_keys('resposta 1', Keys.ENTER)
        # elif todas_as_msg == 2:
        #     campo_de_texto.send_keys('resposta 2', Keys.ENTER)
        # elif todas_as_msg == 3:
        #     campo_de_texto.send_keys('resposta 3', Keys.ENTER)
        # elif todas_as_msg == 4:
        #     campo_de_texto.send_keys('resposta 4', Keys.ENTER)
        # else:
        #     campo_de_texto.send_keys(menu, Keys.ENTER)
            
        

        #Fechando o contato
        webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()


    except:
        print('Aguardando Nova Mensagem')
        #entao vou tentar isso aqui 



while True:
    bot()
