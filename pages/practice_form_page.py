from pathlib import Path
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from pages.base_page import BasePage


class PracticeFormPage(BasePage):
    """
    Page Object do formulário de prática do DemoQA.

    Aqui ficam:
    - locators
    - ações da tela
    - consultas ao resultado
    """

    URL = "https://demoqa.com/automation-practice-form"

    # Campos do formulário
    FIRST_NAME = (By.ID, "firstName")
    LAST_NAME = (By.ID, "lastName")
    EMAIL = (By.ID, "userEmail")
    GENDER_MALE = (By.XPATH, "//label[text()='Male']")
    GENDER_FEMALE = (By.XPATH, "//label[text()='Female']")
    GENDER_OTHER = (By.XPATH, "//label[text()='Other']")
    MOBILE = (By.ID, "userNumber")
    DATE_OF_BIRTH = (By.ID, "dateOfBirthInput")
    MONTH_SELECT = (By.CLASS_NAME, "react-datepicker__month-select")
    YEAR_SELECT = (By.CLASS_NAME, "react-datepicker__year-select")
    SUBJECTS = (By.ID, "subjectsInput")
    HOBBY_SPORTS = (By.XPATH, "//label[text()='Sports']")
    HOBBY_READING = (By.XPATH, "//label[text()='Reading']")
    HOBBY_MUSIC = (By.XPATH, "//label[text()='Music']")
    UPLOAD = (By.ID, "uploadPicture")
    CURRENT_ADDRESS = (By.ID, "currentAddress")
    STATE_INPUT = (By.ID, "react-select-3-input")
    CITY_INPUT = (By.ID, "react-select-4-input")
    SUBMIT = (By.ID, "submit")

    # Modal de resultado
    MODAL_CONTENT = (By.CLASS_NAME, "modal-content")

    def open_page(self):
        """Abre o formulário."""
        self.open(self.URL)

    def fill_name(self, first_name: str, last_name: str):
        """Preenche primeiro nome e sobrenome."""
        self.type(self.FIRST_NAME, first_name)
        self.type(self.LAST_NAME, last_name)

    def fill_email(self, email: str):
        """Preenche o e-mail."""
        self.type(self.EMAIL, email)

    def choose_gender(self, gender: str = "Male"):
        """
        Seleciona o gênero.
        Como o input é escondido, clicamos no label visível.
        """
        if gender.lower() == "male":
            self.click(self.GENDER_MALE)
        elif gender.lower() == "female":
            self.click(self.GENDER_FEMALE)
        else:
            self.click(self.GENDER_OTHER)

    def fill_mobile(self, mobile: str):
        """Preenche o celular."""
        self.type(self.MOBILE, mobile)

    def select_birth_date(self, day: str, month: str, year: str):
        """
        Seleciona data de nascimento usando os selects do calendário.
        Exemplo:
        day=15, month=May, year=1992
        """
        self.click(self.DATE_OF_BIRTH)

        month_element = self.wait.until(EC.visibility_of_element_located(self.MONTH_SELECT))
        Select(month_element).select_by_visible_text(month)

        year_element = self.wait.until(EC.visibility_of_element_located(self.YEAR_SELECT))
        Select(year_element).select_by_visible_text(year)

        day_locator = (
            By.XPATH,
            f"//div[contains(@class,'react-datepicker__day') and text()='{int(day)}' "
            f"and not(contains(@class,'react-datepicker__day--outside-month'))]"
        )
        self.click(day_locator)

    def add_subject(self, subject: str):
        """
        Adiciona uma disciplina no campo Subjects.
        O campo aceita texto + ENTER.
        """
        self.type(self.SUBJECTS, subject, clear=False)
        self.driver.switch_to.active_element.send_keys(Keys.ENTER)

    def choose_hobby(self, hobby: str):
        """Marca um hobby."""
        hobby = hobby.lower()
        if hobby == "sports":
            self.click(self.HOBBY_SPORTS)
        elif hobby == "reading":
            self.click(self.HOBBY_READING)
        elif hobby == "music":
            self.click(self.HOBBY_MUSIC)

    def upload_picture(self, file_path: str):
        """Faz upload de arquivo."""
        self.type(self.UPLOAD, file_path)

    def fill_address(self, address: str):
        """Preenche o endereço atual."""
        self.type(self.CURRENT_ADDRESS, address)

    def select_state(self, state_text: str):
        """
        Seleciona o estado digitando parte do nome e confirmando com ENTER.
        """
        self.type(self.STATE_INPUT, state_text, clear=False)
        self.driver.switch_to.active_element.send_keys(Keys.ENTER)

    def select_city(self, city_text: str):
        """
        Seleciona a cidade digitando parte do nome e confirmando com ENTER.
        """
        self.type(self.CITY_INPUT, city_text, clear=False)
        self.driver.switch_to.active_element.send_keys(Keys.ENTER)

    def submit_form(self):
        """Envia o formulário."""
        self.click(self.SUBMIT)

    def is_success_modal_visible(self, timeout: int = 3) -> bool:
        """
        Verifica se o modal de sucesso apareceu.
        Usado no cenário negativo para garantir que o envio não aconteceu.
        """
        try:
            self.wait.__class__(self.driver, timeout).until(
                EC.visibility_of_element_located(self.MODAL_CONTENT)
            )
            return True
        except TimeoutException:
            return False

    def get_summary_value(self, label: str) -> str:
        """
        Retorna o valor mostrado na tabela do modal.
        Exemplo:
        label = 'Student Name'
        """
        locator = (
            By.XPATH,
            f"//td[text()='{label}']/following-sibling::td"
        )
        return self.text_of(locator)

    def get_summary_text(self) -> str:
        """Retorna todo o texto do modal de confirmação."""
        return self.text_of(self.MODAL_CONTENT)

    def get_uploaded_file_name(self) -> str:
        """Retorna apenas o nome do arquivo enviado, não o caminho completo."""
        full_path = self.driver.find_element(*self.UPLOAD).get_attribute("value")
        return Path(full_path).name