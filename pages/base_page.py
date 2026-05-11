from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    """
    Esta é a nossa Classe Base. 
    Ela contém as ações que se repetem em qualquer site (clicar, escrever, abrir link).
    """

    def __init__(self, driver):
        """
        O 'Nascimento': Sempre que criarmos uma página, ela recebe o navegador (driver).
        """
        self.driver = driver # 'self.driver' guarda o navegador para esta página usar
        self.wait = WebDriverWait(driver, 10) # Criamos um 'garçom' que espera até 10 segundos

    def open(self, url):
        """Abre o site que passarmos por texto."""
        self.driver.get(url)

    def click(self, locator):
        """Espera o elemento ficar clicável na tela e depois clica."""
        # O 'garçom' (wait) procura o elemento antes de tentarmos o clique
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    def type(self, locator, text):
        """Espera o campo aparecer, limpa o que estiver escrito e digita o novo texto."""
        element = self.wait.until(EC.visibility_of_element_located(locator))
        element.clear() # Limpa o campo para não acumular texto
        element.send_keys(text) # Digita o texto que enviamos

    def text_of(self, locator):
        """Espera o elemento aparecer e lê o texto que está escrito nele."""
        element = self.wait.until(EC.visibility_of_element_located(locator))
        return element.text