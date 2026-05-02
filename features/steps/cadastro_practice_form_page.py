from pathlib import Path

from behave import given, when, then

from pages.practice_form_page import PracticeFormPage


def _criar_arquivo_upload():
    """
    Cria um arquivo simples para o upload.
    Isso ajuda na aula porque o aluno enxerga o fluxo completo do envio de arquivo.
    """
    resources_dir = Path("resources")
    resources_dir.mkdir(exist_ok=True)

    arquivo = resources_dir / "texto.txt"
    arquivo.write_text("Teste de upload", encoding="utf-8")
    return str(arquivo.resolve())


@given("que acesso o formulário de prática do DemoQA")
def step_acessar_formulario(context):
    """
    O Page Object já foi inicializado no environment.py.
    Aqui apenas navegamos até a página.
    """
    context.page.open_page()
    context.driver.execute_script("document.body.style.zoom='65%'")


@when("eu preencher todos os campos do formulário")
def step_preencher_todos_os_campos(context):
    """
    Fluxo completo:
    - preenche campos obrigatórios
    - preenche campos opcionais
    - faz upload
    - seleciona estado e cidade
    """
    context.page.fill_name("João", "Silva")
    context.page.fill_email("joao@email.com")
    context.page.choose_gender("Male")
    context.page.fill_mobile("8199999999")
    context.page.select_birth_date(day="15", month="May", year="1992")
    context.page.add_subject("Maths")
    context.page.choose_hobby("Sports")
    context.page.upload_picture(_criar_arquivo_upload())
    context.page.fill_address("Rua Exemplo, 123")
    context.page.select_state("Uttar")
    context.page.select_city("Ag")


@when("eu preencher apenas os campos obrigatórios")
def step_preencher_campos_obrigatorios(context):
    """
    Smoke test:
    aqui validamos somente o que é essencial para submissão.
    """
    context.page.fill_name("João", "Silva")
    context.page.choose_gender("Male")
    context.page.fill_mobile("8199999999")
    

@when("eu tentar enviar o formulário sem preencher um campo obrigatório")
def step_tentar_enviar_com_erro(context):
    """
    Cenário negativo:
    vamos deixar o campo Mobile sem preencher de propósito.
    """
    context.page.fill_name("João", "Silva")
    context.page.choose_gender("Male")
    # Campo obrigatório omitido de propósito:
    # context.page.fill_mobile("8199999999")
    context.page.submit_form()


@when("enviar o formulário")
def step_enviar_formulario(context):
    """Passo genérico para submeter o formulário."""
    context.page.submit_form()


@then("devo visualizar o resumo com todos os dados informados")
def step_validar_resumo_completo(context):
    """
    Validações do fluxo completo.
    Aqui mostramos ao aluno como verificar o dado exatamente na coluna correta da tabela.
    """
    assert context.page.is_success_modal_visible(), "O modal de sucesso não apareceu."

    assert context.page.get_summary_value("Student Name") == "João Silva"
    assert context.page.get_summary_value("Student Email") == "joao@email.com"
    assert context.page.get_summary_value("Gender") == "Male"
    assert context.page.get_summary_value("Mobile") == "8199999999"
    assert context.page.get_summary_value("Date of Birth") == "15 May,1992"
    assert context.page.get_summary_value("Subjects") == "Maths"
    assert context.page.get_summary_value("Hobbies") == "Sports"
    assert context.page.get_summary_value("Picture") == "texto.txt"
    assert context.page.get_summary_value("Address") == "Rua Exemplo, 123"
    assert context.page.get_summary_value("State and City") == "Uttar Pradesh Agra"


@then("devo visualizar o resumo com os campos obrigatórios informados")
def step_validar_smoke(context):
    """
    Smoke test:
    a ideia é validar o mínimo para o cadastro ser aceito.
    """
    assert context.page.is_success_modal_visible(), "O modal de sucesso não apareceu."

    assert context.page.get_summary_value("Student Name") == "João Silva"
    assert context.page.get_summary_value("Gender") == "Male"
    assert context.page.get_summary_value("Mobile") == "8199999999"


@then("o formulário não deve ser enviado com sucesso")
def step_validar_negativo(context):
    """
    Validação negativa:
    se um campo obrigatório faltar, o modal de sucesso não deve aparecer.
    """
    assert not context.page.is_success_modal_visible(), (
        "O modal apareceu, mas o teste negativo esperava falha no envio."
    )