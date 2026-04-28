#Importa o Selenium para controlar o navegado
from selenium import webdriver
import time

#Baixa automaticamente o driver do Chrome
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

#Abre o navegador (sem acessar nenhum site)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

#Maximiza a tela
driver.maximize_window()

#Fecha o navegador
driver.quit()


