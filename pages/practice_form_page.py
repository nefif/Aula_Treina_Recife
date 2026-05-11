from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class PracticeFormPage(BasePage):
    URL = "https://demoqa.com/automation-practice-form"

    # Mapeamento de Elementos (Locators)
    FIRST_NAME = (By.ID, "firstName")
    LAST_NAME = (By.ID, "lastName")
    EMAIL = (By.ID, "userEmail")
    GENDER_MALE = (By.XPATH, "//label[text()='Male']")
    MOBILE = (By.ID, "userNumber")
    SUBMIT = (By.ID, "submit")
    MODAL_CONTENT = (By.CLASS_NAME, "modal-content")

    # Ações da Página
    def open_page(self):
        self.open(self.URL)
        self.driver.execute_script("document.body.style.zoom='50%'")

    def fill_basic_info(self, first_name, last_name, email, mobile):
        self.type(self.FIRST_NAME, first_name)
        self.type(self.LAST_NAME, last_name)
        self.type(self.EMAIL, email)
        self.type(self.MOBILE, mobile)

    def choose_male_gender(self):
        # Apenas um clique simples no xpath direto
        self.click(self.GENDER_MALE)

    def submit_form(self):
        # Removemos o scroll via JS, então usamos um truque simples do Selenium
        submit_btn = self.driver.find_element(*self.SUBMIT)
        self.driver.execute_script("arguments[0].click();", submit_btn)

    def get_summary_value(self, label):
        locator = (By.XPATH, f"//td[text()='{label}']/following-sibling::td")
        return self.text_of(locator)