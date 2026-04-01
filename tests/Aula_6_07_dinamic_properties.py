from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://demoqa.com/dynamic-properties")

# 10 segundos é o tempo limite, mas ele continuará assim que o botão mudar (em 5s)
wait = WebDriverWait(driver, 10)

print("Aguardando as mudanças dinâmicas (5 segundos)...")

# --- VALIDAÇÃO 1: MUDANÇA DE COR ---
# Usamos 'text_to_be_present_in_element_attribute' que é mais estável para classes
wait.until(
    EC.text_to_be_present_in_element_attribute((By.ID, "colorChange"), "class", "text-danger")
)
print("Sucesso: O botão mudou para a cor vermelha (classe 'text-danger')!")

# --- VALIDAÇÃO 2: ELEMENTO QUE APARECE ---
# Este botão não existe no HTML no início, ele é 'injetado' depois de 5 segundos
botao_novo = wait.until(
    EC.visibility_of_element_located((By.ID, "visibleAfter"))
)
print(f"Sucesso: O botão '{botao_novo.text}' apareceu!")

driver.quit()