from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()

# 1 - Acessar o site
driver.get("https://demoqa.com/")

time.sleep(3)

# 2 - Clicar no ícone Elements
elements = driver.find_element(By.XPATH, "//h5[text()='Elements']")
elements.click()

time.sleep(2)

# 3 - Clicar em Text Box
text_box = driver.find_element(By.XPATH, "//span[text()='Text Box']")
text_box.click()

time.sleep(2)

# 4 - Preencher os campos
full_name = driver.find_element(By.ID, "userName")
full_name.send_keys("Teste Selenium")

time.sleep(1)

email = driver.find_element(By.ID, "userEmail")
email.send_keys("teste@email.com")

time.sleep(1)

# 5 - Clicar em Submit
submit = driver.find_element(By.ID, "submit")
submit.click()

time.sleep(3)

driver.quit()