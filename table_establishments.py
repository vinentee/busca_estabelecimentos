from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
import chromedriver_autoinstaller_fix
import pandas as pd
import time
estabelecimento = input('Insira o nome de um estabelecimento: ')
quantidade = int(input('Diga a quantidade de estabelecimentos que você deseja encontrar: '))
chromedriver_autoinstaller_fix.install()  
navegador = webdriver.Chrome()
navegador.get('https://www.google.com.br/maps')
navegador.find_element(By.ID, 'searchboxinput').send_keys(estabelecimento)
navegador.find_element(By.ID, 'searchboxinput').send_keys(Keys.ENTER)
estabelecimentos_dict = {}
lista_nomes = []
lista_enderecos = []
lista_contatos = []
time.sleep(2)
contador = 3
for _ in range(quantidade):
    element = navegador.find_element(By.XPATH, f'//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[1]/div[1]/div[{contador}]/div/a')
    navegador.execute_script("arguments[0].scrollIntoView(true);", element)
    nome_restaurante = element.get_attribute('aria-label')
    element.click()
    time.sleep(1)
    lista_infos = navegador.find_elements(By.CLASS_NAME, 'CsEnBe')
    for infos in lista_infos:
        if 'Endereço' in str(infos.get_attribute('aria-label')):
            try:
                endereco = str(infos.get_attribute('aria-label')) 
            except:
                endereco = 'Endereço não encontrado'               
        if 'Telefone' in str(infos.get_attribute('aria-label')):
            try:
                contato = str(infos.get_attribute('aria-label'))
            except:
                contato = 'Contato não encontrado'
    contato = contato.replace('Telefone', '').replace('(', '').replace('', '').replace(')', '').replace(':', '').replace('-', '').replace(' ', '')
    if nome_restaurante not in lista_nomes:
        lista_nomes.append(nome_restaurante)
    if endereco not in lista_enderecos:
        lista_enderecos.append(endereco)
    if contato not in lista_contatos:
        lista_contatos.append(contato)
    contador += 2
    time.sleep(2)
    
estabelecimentos_dict['Nome'] = lista_nomes
estabelecimentos_dict['Endereço'] = lista_enderecos
estabelecimentos_dict['Contato'] = lista_contatos

max_length = max(map(len, estabelecimentos_dict.values()))

for chave, valor in estabelecimentos_dict.items():
    estabelecimentos_dict[chave] = valor + [None] * (max_length - len(valor))
tabela = pd.DataFrame(estabelecimentos_dict)
tabela.to_excel(f'lista_{estabelecimento}.xlsx', index=False)