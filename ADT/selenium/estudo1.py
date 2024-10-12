from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service

# Definir o caminho para o WebDriver do Microsoft Edge
path = r'c:\Users\mateu\Downloads\edgedriver_win32\msedgedriver.exe'

# Criar o serviço do WebDriver
service = Service(executable_path=path) #sempre quando queremos abrir uma janela, deve iniciar o serviço

# Iniciar o WebDriver do Edge com o serviço
driver = webdriver.Edge(service=service)

# Acessar uma página web
driver.get("https://google.com")

# Localizar o campo de busca e fazer uma pesquisa
search_box = driver.find_element(By.NAME, "q")#procura no atributo name do html q
search_box.send_keys("Selenium com Microsoft Edge") #faz uma busca 
search_box.submit()

input('Pressione enter para fehcar a janela')

# Fecha o navegador
driver.quit()
