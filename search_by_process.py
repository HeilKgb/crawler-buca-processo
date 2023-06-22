from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep
from data_extraction import data_extraction

    # Essa parte é responsável pela conexão com o site, bem como por algumas configurações ao acessá-lo, como o tamanho da janela que será aberta e a opção "headless" para evitar que a página seja exibida toda vez que o código for executado.
options = Options()
    # options.add_argument('--headless')
options.add_argument('window-size=1200,800')
browser = webdriver.Chrome(options=options)
browser.get('https://eproc.trf2.jus.br/eproc/externo_controlador.php?acao=processo_consulta_publica')
sleep(1)
    # Aqui acontecerá a busca e input de pesquisa do cnpj 

input_place = browser.find_element(By.ID, 'txtNumProcesso')
input_place.send_keys('5012208-69.2019.4.02.0000')
input_place.submit()
sleep(3)
data_extraction(browser)



    

