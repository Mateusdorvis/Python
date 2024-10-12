from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.action_chains import ActionChains
driver = webdriver.Edge(service=Service(executable_path=r'c:\Users\mateu\Downloads\edgedriver_win32\msedgedriver.exe') )
driver.get(r"C:\xampp\htdocs\progr\python\ADT\selenium\index.html") #abre a pagina html
button_tag = driver.find_element(By.NAME, "botao") #eu coloquei lá na página index o nome da tag button de botão, para que no fim eu possa manipular o eelemnto
acao = ActionChains(driver)
acao.click(button_tag).perform()

input('Pressione enter para fehcar a janela')
# Fecha o navegador
driver.quit()
