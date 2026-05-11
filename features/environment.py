import os
from selenium import webdriver
from pages.practice_form_page import PracticeFormPage

def before_all(context):
    """
    Executa uma única vez antes de todos os testes começarem.
    Vamos garantir que a pasta 'evidencias' exista.
    """
    if not os.path.exists("evidencias"):
        os.makedirs("evidencias")

def before_scenario(context, scenario):
    """
    Executa antes de cada cenário (teste).
    """
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    context.page = PracticeFormPage(context.driver)

def after_step(context, step):
    """
    Executa após CADA passo (step) do seu arquivo .feature.
    """
    # 1. Trocamos os espaços em branco do nome do passo por sublinhados (_)
    # Ex: "Quando eu enviar o formulário" vira "Quando_eu_enviar_o_formulário"
    nome_seguro = step.name.replace(" ", "_")
    
    # 2. Montamos o caminho de onde a foto será salva
    caminho_foto = f"evidencias/{nome_seguro}.png"
    
    # 3. Pedimos para o Selenium "tirar a foto" da tela atual
    context.driver.save_screenshot(caminho_foto)

def after_scenario(context, scenario):
    """
    Executa após cada cenário, fechando o navegador.
    """
    context.driver.quit()