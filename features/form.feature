# language: pt

@demoqa @practice_form
Funcionalidade: Preenchimento do formulário de prática do DemoQA
  Como estudante de automação de testes
  Eu quero validar o formulário de prática do DemoQA
  Para exercitar a estrutura POM + BDD com Selenium

  Contexto:
    Dado que acesso o formulário de prática do DemoQA

  @e2e
  Cenário: Fluxo Completo - preencher todos os campos
    Quando eu preencher todos os campos do formulário
    E enviar o formulário
    Então devo visualizar o resumo com todos os dados informados

  @smoke
  Cenário: Smoke Test - preencher apenas os campos obrigatórios
    Quando eu preencher apenas os campos obrigatórios
    E enviar o formulário
    Então devo visualizar o resumo com os campos obrigatórios informados

  @negative @validation
  Cenário: Teste Negativo - não seguir se faltar campo obrigatório
    Quando eu tentar enviar o formulário sem preencher um campo obrigatório
    Então o formulário não deve ser enviado com sucesso