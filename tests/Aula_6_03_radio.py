from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Configuração do Driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# 1. Acessa o site
driver.get("https://demoqa.com/radio-button")
driver.maximize_window()

# 2. Clica no 'Yes' (clicando na label para evitar erro de elemento interceptado)
driver.find_element(By.XPATH, "//label[@for='yesRadio']").click()
resultado_yes = driver.find_element(By.CLASS_NAME, "text-success").text
assert resultado_yes == "Yes"
print("Clique no 'Yes' validado!")

# 3. Clicar no 'Impressive'
driver.find_element(By.XPATH, "//label[@for='impressiveRadio']").click()
resultado_impressive = driver.find_element(By.CLASS_NAME, "text-success").text
assert resultado_impressive == "Impressive"
print("Clique no 'Impressive' validado!")

# 4. Validar que o botão 'No' está desabilitado
# Aqui verificamos o atributo 'disabled' do input real
botao_no = driver.find_element(By.ID, "noRadio")
assert not botao_no.is_enabled()
print("Botão 'No' está corretamente desabilitado!")

print("\nTodos os testes passaram com sucesso!")

time.sleep(2)
driver.quit()