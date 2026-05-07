from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://demoqa.com/links")
driver.maximize_window()

# Clicar no link (abre nova aba)
driver.find_element(By.ID, "simpleLink").click()

time.sleep(2)

# Trocar para nova aba
abas = driver.window_handles
driver.switch_to.window(abas[1])

time.sleep(1)

# Validação simples
assert "https://demoqa.com/" == driver.current_url
print("Sucesso: Link validado!")

time.sleep(1)

driver.quit()