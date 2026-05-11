from behave import given, when, then

@given("que acesso o formulário de prática do DemoQA")
def step_acessar_formulario(context):
    context.page.open_page()

@when("eu preencher apenas os campos obrigatórios")
def step_preencher_campos_obrigatorios(context):
    # Simplificamos a chamada para um método mais direto
    context.page.fill_basic_info("João", "Silva", "joao@email.com", "8199999999")
    context.page.choose_male_gender()

@when("enviar o formulário")
def step_enviar_formulario(context):
    context.page.submit_form()

@then("devo visualizar o resumo com os campos obrigatórios informados")
def step_validar_smoke(context):
    # Validações diretas e simples
    assert context.page.get_summary_value("Student Name") == "João Silva"
    assert context.page.get_summary_value("Gender") == "Male"
    assert context.page.get_summary_value("Mobile") == "8199999999"