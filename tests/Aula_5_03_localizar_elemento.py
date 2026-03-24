from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://demoqa.com/text-box")

# Localiza o campo de nome
elemento_nome = driver.find_element(By.ID, "userName")

""" if elemento_nome:
	print("Elemento Encontrado")
else:
    print("Elemento não encontrado") """

driver.quit()


