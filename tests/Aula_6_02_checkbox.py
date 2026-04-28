from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://demoqa.com/checkbox")
driver.maximize_window()

elemento_tree_home = driver.find_element(By.XPATH, "//span[@aria-label='Select Home']/preceding-sibling::span[contains(@class, 'rc-tree-switcher')]").click()
elemento_tree_documents = driver.find_element(By.XPATH, "//span[@aria-label='Select Documents']/preceding-sibling::span[contains(@class, 'rc-tree-switcher')]").click() 
elemento_tree_workspace = driver.find_element(By.XPATH, "//span[@aria-label='Select WorkSpace']/preceding-sibling::span[contains(@class, 'rc-tree-switcher')]").click()
elemento_checkbox_angular = driver.find_element(By.XPATH, "//span[@aria-label='Select Angular']").click()

resultado = driver.find_element(By.ID, "result").text

assert "angular" in resultado
print("Teste passou com Sucesso!")

