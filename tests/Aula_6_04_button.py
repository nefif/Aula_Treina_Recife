from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import ActionChains
import time

# 1. Configuração do Driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window() # Melhora a visibilidade dos botões para o Selenium

# 2. Abrir o site
driver.get("https://demoqa.com/buttons")
time.sleep(2) # Espera a página carregar os elementos

actions = ActionChains(driver)

# --- Execução das Ações ---

# Double Click
double_btn = driver.find_element(By.ID, "doubleClickBtn")
actions.double_click(double_btn).perform()

# Right Click
right_btn = driver.find_element(By.ID, "rightClickBtn")
actions.context_click(right_btn).perform()

# Click normal (Usando XPATH para localizar pelo texto exato)
# Note que o ID desse botão no DemoQA é dinâmico, por isso o XPATH é melhor aqui
click_btn = driver.find_element(By.XPATH, "//button[text()='Click Me']")
click_btn.click()


time.sleep(2)

# Verificação do Double Click
assert driver.find_element(By.ID, "doubleClickMessage").text == "You have done a double click"
print("Sucesso: Double Click validado!")

# Verificação do Right Click
assert driver.find_element(By.ID, "rightClickMessage").text == "You have done a right click"
print("Sucesso: Right Click validado!")

# Verificação do Click Normal (ID: dynamicClickMessage)
assert driver.find_element(By.ID, "dynamicClickMessage").text == "You have done a dynamic click"
print("Sucesso: Click normal validado!")

# Fechar o navegador
time.sleep(2)
driver.quit()