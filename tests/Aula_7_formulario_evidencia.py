from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time
from datetime import datetime

# =========================
# 📸 CONFIGURAÇÃO SCREENSHOT
# =========================

timestamp_execucao = datetime.now().strftime("%Y%m%d_%H%M%S")
PASTA_SCREENSHOTS = f"screenshots/{timestamp_execucao}"

os.makedirs(PASTA_SCREENSHOTS, exist_ok=True)

def tirar_screenshot(driver, nome_etapa):
    caminho = os.path.join(PASTA_SCREENSHOTS, f"{nome_etapa}.png")
    driver.save_screenshot(caminho)
    print(f"[SCREENSHOT] {caminho}")

# =========================
# 🚀 INÍCIO AUTOMAÇÃO
# =========================

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://demoqa.com/automation-practice-form")

driver.execute_script("document.body.style.zoom='50%'")
driver.save_screenshot('prints/01_tela_inicial.png')  # Screenshot da tela inicial
tirar_screenshot(driver, "01_pagina_aberta")

# =========================
# ✍️ PREENCHIMENTO
# =========================

driver.find_element(By.ID, "firstName").send_keys("João")
driver.find_element(By.ID, "lastName").send_keys("Silva")
driver.save_screenshot('prints/02_nome_preenchido.png')  # Screenshot da tela inicial
tirar_screenshot(driver, "02_nome_preenchido")

driver.find_element(By.ID, "userEmail").send_keys("joao@email.com")
driver.save_screenshot('prints/03_email.png')  # Screenshot da tela inicial
tirar_screenshot(driver, "03_email")

driver.find_element(By.ID, "gender-radio-1").click()
driver.save_screenshot('prints/04_genero.png')  # Screenshot da tela inicial
tirar_screenshot(driver, "04_genero")

driver.find_element(By.ID, "userNumber").send_keys("81999999999")
driver.save_screenshot('prints/05_telefone.png')  # Screenshot da tela inicial
tirar_screenshot(driver, "05_telefone")

# =========================
# 📅 DATA
# =========================

driver.find_element(By.ID, "dateOfBirthInput").click()

select_month = Select(driver.find_element(By.CLASS_NAME, "react-datepicker__month-select"))
select_month.select_by_index(5)

select_year = Select(driver.find_element(By.CLASS_NAME, "react-datepicker__year-select"))
select_year.select_by_visible_text("1992")

driver.find_element(By.XPATH, "//div[contains(@class,'react-datepicker__day') and text()='27']").click()

driver.save_screenshot('prints/06_data_nascimento.png')  # Screenshot da tela inicial
tirar_screenshot(driver, "06_data_nascimento")

# =========================
# 🎯 HOBBY E SUBJECT
# =========================

driver.find_element(By.ID, "hobbies-checkbox-1").click()

subject = driver.find_element(By.ID, "subjectsInput")
subject.send_keys("Hindi")
subject.send_keys(Keys.TAB)

driver.save_screenshot('prints/07_hobby_subject.png')  # Screenshot da tela inicial
tirar_screenshot(driver, "07_hobby_subject")

# =========================
# 📎 UPLOAD
# =========================

caminho_arquivo = os.path.abspath("Texto.txt")

with open("Texto.txt", "w") as f:
    f.write("Teste de upload")

driver.find_element(By.ID, "uploadPicture").send_keys(caminho_arquivo)

driver.save_screenshot('prints/08_upload.png')  # Screenshot da tela inicial
tirar_screenshot(driver, "08_upload")

# =========================
# 🏠 ENDEREÇO
# =========================

driver.find_element(By.ID, "currentAddress").send_keys("Rua Exemplo, 123")

state = driver.find_element(By.ID, "react-select-3-input")
state.send_keys("Har")
state.send_keys(Keys.TAB)

city = driver.find_element(By.ID, "react-select-4-input")
city.send_keys("Kar")
city.send_keys(Keys.TAB)

driver.save_screenshot('prints/09_endereco.png')  # Screenshot da tela inicial
tirar_screenshot(driver, "09_endereco")

# =========================
# 📤 SUBMIT
# =========================

driver.find_element(By.ID, "submit").click()

wait = WebDriverWait(driver, 10)
wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "modal-content")))

driver.save_screenshot('prints/10_modal_sucesso.png')  # Screenshot do modal de sucesso
tirar_screenshot(driver, "10_modal_sucesso")

# =========================
# ✅ VALIDAÇÕES
# =========================

print("\n--- Iniciando Validações ---")

def validar(label, esperado):
    valor = driver.find_element(By.XPATH, f"//td[text()='{label}']/following-sibling::td").text
    assert valor == esperado
    print(f"{label} OK: {valor}")

validar("Student Name", "João Silva")
validar("Student Email", "joao@email.com")
validar("Gender", "Male")
validar("Address", "Rua Exemplo, 123")

driver.save_screenshot('prints/11_validacoes.png')  # Screenshot das validações

time.sleep(2)
driver.quit()