from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
#import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://demoqa.com/text-box")

# Preenche o campo nome
driver.find_element(By.ID, "userName").send_keys("Teste QA")

#time.sleep(3)

# Preenche o campo email
driver.find_element(By.ID, "userEmail").send_keys("teste@email.com")

#time.sleep(3)

# Clica no botão
driver.find_element(By.ID, "submit").click()

#time.sleep(3)

driver.quit()


