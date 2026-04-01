from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

driver = webdriver.Chrome()
driver.get("https://demoqa.com/upload-download")

# Criando arquivo de teste
caminho_arquivo = os.path.abspath("arquivo_teste.txt")

with open("arquivo_teste.txt", "w") as f:
    f.write("Teste de upload")

# Upload
driver.find_element(By.ID, "uploadFile").send_keys(caminho_arquivo)

time.sleep(2)

# Validação
resultado = driver.find_element(By.ID, "uploadedFilePath").text

assert "arquivo_teste.txt" in resultado

driver.quit()