import json
import csv
import pandas as pd
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By


def data_extraction(browser):
    # Informações contidas na capa do processo
    numero_processo = browser.find_element(By.ID, 'txtNumProcesso')
    data_autuacao = browser.find_element(By.ID, 'txtAutuacao')
    situacao = browser.find_element(By.ID, 'txtSituacao')

    # Salva e escreve os dados em um arquivo json
    data = {'numero_processo': numero_processo.text, 'data_autuacao': data_autuacao.text, 'situacao': situacao.text}

    with open("db_capa_processo.json", "w") as file:
      json.dump(data, file, indent=4)

    # Informações referentes a partes e representantes
    parte_field = browser.find_element(By.ID, 'fldPartes')
    partes_table = parte_field.find_element(By.CLASS_NAME, 'infraTable')
    lines = partes_table.find_elements(By.CSS_SELECTOR, 'tr')
    
    table_information = []

    for l in lines[1:]:
        cell = l.find_elements(By.CSS_SELECTOR, 'td')
        instituicao = cell[0].text.strip().split('\n')[0]
        names = [celula.text.strip() if celula.text.strip() else 'null' for celula in cell[1:]]
        lines_information = [instituicao] + names
        table_information.append(lines_information)
    
    partes_representantes = pd.DataFrame(table_information, columns=['Instituição', 'Nome/OAB'])
    partes_representantes.to_csv('db_partes_representantes.csv', index=False)

    with open('db_partes_representantes.csv', 'r') as file_csv:
      csv_reader = csv.DictReader(file_csv)
      data = list(csv_reader)

    with open('db_partes_representantes.json', 'w') as file_json:
      json.dump(data, file_json, indent=4)

    # Informações das movimentações
    lines_movements = browser.find_elements(By.CSS_SELECTOR, 'tr')
    final_line = lines_movements[-1]

    cells_movements = final_line.find_elements(By.CSS_SELECTOR, 'td')
    data_table = []
    for l in lines_movements:
        cells_movements = l.find_elements(By.CSS_SELECTOR, 'td')

        line_data = [cell_movements.text for cell_movements in cells_movements]
        data_table.append(line_data)

    movements = data_table[-10:]
    
    movements_json =  pd.DataFrame(movements, columns=['Evento', 'Data/Hora', 'Descrição', 'Usuário', 'Documentos'])
    movements_json.to_csv('db_movements.csv',index=False)

    with open('db_movements.csv', 'r') as file_csv:
      csv_reader = csv.DictReader(file_csv)
      data = list(csv_reader)

    with open('db_movements.json', 'w') as file_json:
      json.dump(data, file_json, indent=4)
