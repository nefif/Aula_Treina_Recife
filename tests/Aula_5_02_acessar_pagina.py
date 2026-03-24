from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

#url = "https://demoqa.com"

# Acessa um site especifico
driver.get("https://demoqa.com")
#driver.get(url)

driver.maximize_window()

driver.quit()


