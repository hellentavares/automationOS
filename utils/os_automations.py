from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from config.selectors import AutomationOs
from selenium.webdriver.support.ui import Select


class Osactions:
    """Classe contendo todas as ações dentro da O.S em andamento"""

    def __init__(self, driver):
            self.driver = driver
            self.wait = WebDriverWait(driver, 30)  # Tempo máximo de espera para elementos

    def _click_element(self, xpath, success_message):
        """Método genérico para clicar em um elemento."""
        if self.driver is None:
            print("Error: Invalid driver. Cannot perform action.")
            return

    def firsh_category(self):
            """Clicar no dropdonw da 1ª categoria'."""
            try:
                button = self.wait.until(EC.element_to_be_clickable((By.XPATH, AutomationOs.CATEGORY_ONE)))
                button.click()
                print("Botão para abrir dropdown (categoria 1) selecionado com sucesso")
            except Exception as e:
                print(f"Erro ao clicar em botão para abrir dropdown (categoria 1) {e}")

    def select_adm(self):
            """selecionar 'Admnistrativo' nas categorias"""
            try:
                button = self.wait.until(EC.element_to_be_clickable(By.XPATH, AutomationOs.SELECT_ADM))
                button.click()
                print("Categoria 'Administrativo' selecionado com sucesso.")
            except Exception as e:
                 print(f"Erro ao selecionar categoria 'Administrativo'")

"""def select_adm(self):
            Digitar 'Administrativo' no campo SELECT_ADM e pressionar Enter
            try:
                input_field = self.wait.until(EC.element_to_be_clickable((By.XPATH, AutomationOs.SELECT_ADM)))
                input_field.clear()  # Limpa o campo antes de digitar
                input_field.send_keys("Administrativo")
                input_field.send_keys(Keys.RETURN)  # Pressiona Enter
                print("Categoria 'Administrativo' selecionada com sucesso.")
            except Exception as e:
                print(f"Erro ao selecionar categoria 'Administrativo': {e}")"""




