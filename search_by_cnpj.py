import requests
from bs4 import BeautifulSoup
from selenium import webdriver 
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.chrome.options import Options
from data_extraction import data_extraction

# O webdrive do selenium será responsavél pela conexão com site
options = Options()
# options.add_argument('--headless')
options.add_argument('window-size=1200,800')
browser = webdriver.Chrome(options=options)

browser.get('https://eproc.trf2.jus.br/eproc/externo_controlador.php?acao=processo_consulta_publica')

sleep(1)
# Selecionará o botão da pessoa judirica
button = browser.find_element(By.ID, 'rdoPessoaJuridica')
button.click()
sleep(0.5)
# Pesquisará o cnpj 
input_place = browser.find_element(By.ID, 'txtCpfCnpj')
# cnpj = input('Digite o cnpj: ')
cnpj = '33649575000199'
input_place.send_keys(cnpj)
input_place.submit()
sleep(5)

# Entrará em um processo do cnpj fornecido
data_process = browser.find_element(By.XPATH, '//*[@id="divInfraAreaTabela"]/table/tbody/tr[4]/td[1]/a')
if (data_process):
  data_process.click()
  sleep(5)
  data_extraction(browser)
