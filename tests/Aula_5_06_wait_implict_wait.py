from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Define espera global de até 10 segundos
driver.implicitly_wait(10)

driver.get("https://demoqa.com/text-box")

driver.find_element(By.ID, "userName").send_keys("Teste QA")

driver.quit()

