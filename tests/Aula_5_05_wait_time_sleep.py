import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://demoqa.com/text-box")

time.sleep(5)  # Espera 5 segundos

driver.find_element(By.ID, "userName").send_keys("Teste QA")

time.sleep(2)  # Espera 2 segundos

driver.quit()

