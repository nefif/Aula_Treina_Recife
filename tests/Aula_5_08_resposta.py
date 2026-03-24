from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()

wait = WebDriverWait(driver, 10)

# 1 - Acessar o site
driver.get("https://demoqa.com/")

# 2 - Clicar no ícone Elements
elements = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//h5[text()='Elements']"))
)
elements.click()

# 3 - Clicar em Text Box
text_box = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//span[text()='Text Box']"))
)
text_box.click()

# 4 - Preencher os campos
full_name = wait.until(
    EC.visibility_of_element_located((By.ID, "userName"))
)
full_name.send_keys("Teste Selenium")

email = wait.until(
    EC.visibility_of_element_located((By.ID, "userEmail"))
)
email.send_keys("teste@email.com")

# 5 - Clicar em Submit
submit = wait.until(
    EC.element_to_be_clickable((By.ID, "submit"))
)
submit.click()

driver.quit()