
#este script que eu fiz serve justamente para preencher formulario automaticamente
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.action_chains import ActionChains
driver = webdriver.Edge(service=Service(executable_path=r'c:\Users\mateu\Downloads\edgedriver_win32\msedgedriver.exe') )
driver.get(r"C:\xampp\htdocs\progr\python\ADT\selenium\form.html") #abre a pagina html

entrada = driver.find_element(By.ID, 'name')
entrada.send_keys('Mateus da Silva Dorvis') #coloca no input meu nome completo

input_tag = driver.find_element(By.NAME, "Enviar") 
acao = ActionChains(driver)
acao.click(input_tag).perform() #depois colocar meu nome no input, clica no botão para enviar o meu nome

input('Pressione enter para fehcar a janela')
# Fecha o navegador
driver.quit()
