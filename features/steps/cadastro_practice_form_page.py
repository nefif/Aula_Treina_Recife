from behave import given, when, then

@given("que acesso o formulário de prática do DemoQA")
def step_acessar_formulario(context):
    # Pegamos a página de dentro da 'mochila' (context) e pedimos para abrir
    context.page.open_page()

@when("eu preencher apenas os campos obrigatórios")
def step_preencher_campos_obrigatorios(context):
    # Chamamos as ações que mapeamos lá no Page Object
    context.page.fill_basic_info("João", "Silva", "joao@email.com", "8199999999")
    context.page.choose_male_gender()

@when("enviar o formulário")
def step_enviar_formulario(context):
    context.page.submit_form()

@then("devo visualizar o resumo com os campos obrigatórios informados")
def step_validar_smoke(context):
    """
    O momento da verdade: verificamos se o que o robô vê na tela 
    é o que realmente deveria estar lá (Assert).
    """
    # Comparamos o valor na tela com o valor que digitamos
    assert context.page.get_summary_value("Student Name") == "João Silva"
    assert context.page.get_summary_value("Gender") == "Male"
    assert context.page.get_summary_value("Mobile") == "8199999999"