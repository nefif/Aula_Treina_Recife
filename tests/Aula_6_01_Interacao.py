from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://demoqa.com/text-box")
driver.maximize_window()

elemento_full_name = driver.find_element(By.ID, "userName").send_keys("Teste Selenium")
elemento_email = driver.find_element(By.ID, "userEmail").send_keys("teste@selenium.com")
elemento_current_address = driver.find_element(By.ID, "currentAddress").send_keys("Rua Teste, 123")

btn_submit = driver.find_element(By.ID, "submit").click()

resultado = driver.find_element(By.ID, "output").text    

assert "Teste Selenium" in resultado
print("Teste passou com Sucesso!")

assert "teste@selenium.com" in resultado
print("Teste passou com Sucesso!")

assert "Rua Teste, 123" in resultado
print("Teste passou com Sucesso!")  

driver.quit()
