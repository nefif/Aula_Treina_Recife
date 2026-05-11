import os
from selenium import webdriver
from pages.practice_form_page import PracticeFormPage

def before_all(context):
    """
    Executa uma única vez, antes de TODOS os testes.
    Aqui verificamos se a pasta de fotos já existe.
    """
    if not os.path.exists("evidencias"):
        os.makedirs("evidencias")

def before_scenario(context, scenario):
    """
    Executa antes de cada Cenário.
    Prepara o navegador e coloca as ferramentas na 'Mochila' (context).
    """
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    
    # Criamos a nossa página e guardamos na mochila para os Steps usarem
    context.page = PracticeFormPage(context.driver)

def after_step(context, step):
    """
    Executa após cada Passo (Dado, Quando, Então).
    Tira uma foto da tela para servir de prova (evidência).
    """
    # Deixa o nome da foto bonitinho (troca espaço por _)
    nome_foto = step.name.replace(" ", "_")
    caminho = f"evidencias/{nome_foto}.png"
    
    # O Selenium tira a foto e salva na pasta
    context.driver.save_screenshot(caminho)

def after_scenario(context, scenario):
    """
    Executa após o fim do Cenário.
    Fecha o navegador para não gastar memória do computador.
    """
    context.driver.quit()