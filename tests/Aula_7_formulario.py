from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://demoqa.com/automation-practice-form")

first_name=driver.find_element(By.ID, "firstName").send_keys("João")

last_name=driver.find_element(By.ID, "lastName").send_keys("Silva")

email=driver.find_element(By.ID, "userEmail").send_keys("joao@email.com")

gender=driver.find_element(By.ID, "gender-radio-1").click() # Seleciona o gênero masculino

phone_number=driver.find_element(By.ID, "userNumber").send_keys("81999999999")

select_birth_date=driver.find_element(By.ID, "dateOfBirthInput").click()

select_month = Select(driver.find_element(By.CLASS_NAME, "react-datepicker__month-select"))
select_month.select_by_visible_text("May") # Seleciona o mês de maio
#time.sleep(2)

select_month.select_by_index(5) # Seleciona o mês de junho
#time.sleep(2)

select_month.select_by_value("6") # Seleciona o mês de julho
#time.sleep(2)


select_year = Select(driver.find_element(By.CLASS_NAME, "react-datepicker__year-select"))
select_year.select_by_visible_text("1990")
#time.sleep(2)

select_year.select_by_index(91) # Seleciona o ano de 1991
#time.sleep(2)

select_year.select_by_value("1992") # Seleciona o ano de 1992
#time.sleep(2)

select_day=driver.find_element(By.XPATH, '//*[@id="dateOfBirth"]/div[2]/div[2]/div/div/div/div/div[2]/div[2]/div[2]/div[3]').click() # Seleciona o dia 15
#time.sleep(2)

hobby=driver.find_element(By.ID, "hobbies-checkbox-1").click()
#hobby=driver.find_element(By.ID, "hobbies-checkbox-2").click()
#hobby=driver.find_element(By.ID, "hobbies-checkbox-3").click()
#time.sleep(2)

subject=driver.find_element(By.ID, "subjectsInput")
subject.send_keys("Maths")
subject.send_keys(Keys.ENTER)

remover_subject=driver.find_element(By.XPATH, "//div[text()='Maths']/following-sibling::div").click() # Clica na opção "Maths" que aparece após digitar o texto

# O ponto (.) indica que é uma classe CSS
#driver.find_element(By.CSS_SELECTOR, ".css-8mmkcg").click()

# Localiza o SVG que possui a classe específica
#driver.find_element(By.XPATH, //*[local-name()='svg' and @class='css-8mmkcg']).click()

subject.send_keys("Hindi")
subject.send_keys(Keys.ENTER)

caminho_arquivo = os.path.abspath("Texto.txt")

with open("Texto.txt", "w") as f:
    f.write("Teste de upload")
    
upload_file=driver.find_element(By.ID, "uploadPicture").send_keys(caminho_arquivo)

current_address=driver.find_element(By.ID, "currentAddress").send_keys("Rua Exemplo, 123")

state = driver.find_element(By.ID, "react-select-3-input")
state.send_keys("Uttar")
state.send_keys(Keys.TAB)

city = driver.find_element(By.ID, "react-select-4-input")
city.send_keys("Ag")
city.send_keys(Keys.TAB)

btn_submit=driver.find_element(By.ID, "submit").click()

wait = WebDriverWait(driver, 10)
wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "modal-content")))

print("\n--- Iniciando Validações da Tabela ---")

# Validação do Nome Completo
# Buscamos o <td> que tem o texto 'Student Name' e pegamos o <td> ao lado (sibling)
celula_nome = driver.find_element(By.XPATH, "//td[text()='Student Name']/following-sibling::td").text
assert celula_nome == "João Silva"
print(f"Nome validado: {celula_nome}")

# Validação do E-mail
celula_email = driver.find_element(By.XPATH, "//td[text()='Student Email']/following-sibling::td").text
assert celula_email == "joao@email.com"
print(f"E-mail validado: {celula_email}")

# Validação do Gênero
celula_genero = driver.find_element(By.XPATH, "//td[text()='Gender']/following-sibling::td").text
assert celula_genero == "Male"
print(f"Gênero validado: {celula_genero}")

# Validação do Celular (Mobile)
celula_celular = driver.find_element(By.XPATH, "//td[text()='Mobile']/following-sibling::td").text
assert celula_celular == "8199999999"
print(f"Celular validado: {celula_celular}")

# Validação do Endereço
celula_endereco = driver.find_element(By.XPATH, "//td[text()='Address']/following-sibling::td").text
assert celula_endereco == "Rua Exemplo, 123"
print(f"Endereço validado: {celula_endereco}")


""" wait = WebDriverWait(driver, 10)
modal = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "modal-content")))

# 2. Validação por bloco de texto (O que você já fez, muito bom para iniciantes)
resultado_texto = modal.text

assert "João Silva" in resultado_texto
print("Confirmação: Nome completo encontrado no modal.")

# 3. Validação Específica por Campo (Nível Instrutor)
# Vamos ensinar o aluno a checar se o valor está na linha correta da tabela
def validar_campo(label, valor_esperado):
    # Procura o <td> que contém o Label e pega o próximo <td> (o valor)
    xpath_celula = f"//td[text()='{label}']/following-sibling::td"
    valor_na_tabela = driver.find_element(By.By.XPATH, xpath_celula).text
    
    assert valor_esperado in valor_na_tabela
    print(f"Validação OK: O campo '{label}' exibe '{valor_na_tabela}'")

# Chamando as validações específicas
validar_campo("Student Name", "João Silva")
validar_campo("Student Email", "joao@email.com")
validar_campo("Mobile", "8199999999")
validar_campo("Address", "Rua Exemplo, 123")
validar_campo("State and City", "Uttar Pradesh Agra")
 """
 
time.sleep(2)

driver.quit()