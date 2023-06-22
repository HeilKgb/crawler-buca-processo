import requests
from bs4 import BeautifulSoup
from selenium import webdriver 
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.chrome.options import Options
from data_extraction import data_extraction


options = Options()
# options.add_argument('--headless')
options.add_argument('window-size=1200,800')
browser = webdriver.Chrome(options=options)

browser.get('https://eproc.trf2.jus.br/eproc/externo_controlador.php?acao=processo_consulta_publica')
 
input_place = browser.find_element(By.ID, 'txtStrParte')
#Pesquisará o nome da pessoa física ou jurídica
# name = input('Digite o nome da parte: ')
name = "CLUBE DE REGATAS DO FLAMENGO"
input_place.send_keys(name)
input_place.submit()
sleep(2)
# Entrará no link que leva as informações sobre processos associados 
link = browser.find_element(By.XPATH, '//*[@id="divInfraAreaTabela"]/table/tbody/tr[2]/td[1]/a')
link.click()
sleep(5)

# Entrará em um processo 
data_process = browser.find_element(By.XPATH, '//*[@id="divInfraAreaTabela"]/table/tbody/tr[2]/td[1]/a')
if (data_process):
  data_process.click()
  sleep(5)
  data_extraction(browser)

