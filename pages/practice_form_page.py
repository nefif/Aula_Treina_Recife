from selenium.webdriver.common.by import By
from pages.base_page import BasePage

# '(BasePage)' significa que esta classe herda (copia) tudo da BasePage
class PracticeFormPage(BasePage):
    URL = "https://demoqa.com/automation-practice-form"

    # --- MAPEAMENTO DE ELEMENTOS ---
    # Guardamos o endereço de cada campo (como se fosse o CEP do elemento)
    FIRST_NAME = (By.ID, "firstName")
    LAST_NAME = (By.ID, "lastName")
    EMAIL = (By.ID, "userEmail")
    GENDER_MALE = (By.XPATH, "//label[text()='Male']")
    MOBILE = (By.ID, "userNumber")
    SUBMIT = (By.ID, "submit")

    # --- AÇÕES DA PÁGINA ---
    def open_page(self):
        """Usa a função 'open' da classe mãe para abrir a URL."""
        self.open(self.URL)
        self.driver.execute_script("document.body.style.zoom='50%'") # Rola a página para baixo para mostrar os campos

    def fill_basic_info(self, first_name, last_name, email, mobile):
        """Ação que preenche o bloco de informações principais."""
        self.type(self.FIRST_NAME, first_name)
        self.type(self.LAST_NAME, last_name)
        self.type(self.EMAIL, email)
        self.type(self.MOBILE, mobile)

    def choose_male_gender(self):
        """Clica na opção 'Male' do campo de gênero."""
        self.click(self.GENDER_MALE)

    def submit_form(self):
        """Clica no botão de enviar usando um comando especial para evitar erros de tela."""
        submit_btn = self.driver.find_element(*self.SUBMIT)
        # Usamos o comando abaixo para garantir que o clique aconteça mesmo se algo estiver na frente
        self.driver.execute_script("arguments[0].click();", submit_btn)

    def get_summary_value(self, label):
        """Lê o valor de uma linha específica da tabela de resumo que aparece no final."""
        locator = (By.XPATH, f"//td[text()='{label}']/following-sibling::td")
        return self.text_of(locator)