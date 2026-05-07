from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://demoqa.com/text-box")

# Cria um objeto de espera
wait = WebDriverWait(driver, 10)

# Espera o campo aparecer
campo_nome = wait.until(
    EC.visibility_of_element_located((By.ID, "userName"))
)

campo_nome.send_keys("Teste QA")

driver.quit()


