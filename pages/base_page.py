from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    """
    Classe base para centralizar ações comuns de qualquer página.

    A ideia aqui é evitar repetição de código:
    - clicar com espera explícita
    - digitar com espera explícita
    - ler textos da tela
    """

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def open(self, url: str):
        """Abre uma URL no navegador."""
        self.driver.get(url)

    def click(self, locator):
        """
        Clica em um elemento somente quando ele estiver clicável.
        Também faz scroll até o elemento, o que ajuda em páginas longas.
        """
        element = self.wait.until(EC.element_to_be_clickable(locator))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        element.click()

    def type(self, locator, text: str, clear: bool = True):
        """
        Digita em um campo de texto com espera explícita.
        """
        element = self.wait.until(EC.visibility_of_element_located(locator))
        if clear:
            element.clear()
        element.send_keys(text)

    def text_of(self, locator) -> str:
        """Retorna o texto de um elemento visível."""
        element = self.wait.until(EC.visibility_of_element_located(locator))
        return element.text