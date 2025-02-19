from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from config.selectors import DashboardSelectors

class DashboardActions:
    """Classe contendo todas as ações dentro do sistema após o login."""

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 30)  # Tempo máximo de espera para elementos

    def start_service(self):
        """Inicia um atendimento."""
        self._click_element(DashboardSelectors.START_BUTTON, "Iniciar nova Solicitação.")

    def close_internal_os(self):
        """Fecha a O.S interna."""
        self._click_element(DashboardSelectors.CLICK_BUTTON, "Fechar aba de solicitação interna.")

    def start_external_os(self):
        """Inicia uma O.S externa."""
        self._click_element(DashboardSelectors.OS_BUTTON, "Iniciar nova solicitação externa.")

    def search_user(self, document):
        """Digita um documento no campo de pesquisa de usuário, sem limpar antes."""
        if self.driver is None:
            print("Error: Invalid driver. Cannot search user.")
            return
        try:
            search_field = self.wait.until(EC.presence_of_element_located((By.XPATH, DashboardSelectors.SEARCH_USER)))
            print("Aguardando o campo de pesquisa ser ativado e interativo...")
            self.wait.until(EC.element_to_be_clickable((By.XPATH, DashboardSelectors.SEARCH_USER)))        
            print(f"Digitando documento: {document}")
            search_field.send_keys(document)
            time.sleep(2)  # Pequeno delay para evitar problemas de processamento
        except Exception as e:
            print(f"Erro ao pesquisar usuário: {e}")

    def _click_element(self, xpath, success_message):
        """Método genérico para clicar em um elemento."""
        if self.driver is None:
            print("Error: Invalid driver. Cannot perform action.")
            return

        try:
            element = self.wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
            element.click()
            print(success_message)
        except Exception as e:
            print(f"Error performing action: {e}")

    def start_new_service(self):
        """Clica no botão 'Iniciar Novo Serviço' após pesquisar o usuário."""
        if self.driver is None:
            print("Error: Invalid driver. Cannot start new service.")
            return
        try:
            button = self.wait.until(EC.presence_of_element_located((By.XPATH, DashboardSelectors.START_NEW_SERVICE)))
            self.wait.until(EC.element_to_be_clickable((By.XPATH, DashboardSelectors.START_NEW_SERVICE)))
            button.click()
            print("Novo serviço iniciado com sucesso.")
        except Exception as e:
            print(f"Erro ao iniciar novo serviço: {e}")

    def handle_modal(self):
        """Espera e clica no modal de confirmação."""
        if self.driver is None:
            print("Error: Invalid driver. Cannot interact with modal.")
            return
        try:
            print("Aguardando o modal aparecer...")
            modal = self.wait.until(EC.presence_of_element_located((By.XPATH, DashboardSelectors.MODAL_SELECTOR)))
            print("Aguardando o modal ser interativo...")
            self.wait.until(EC.element_to_be_clickable((By.XPATH, DashboardSelectors.MODAL_SELECTOR)))
            print("Clicando no modal...")
            modal.click()
            print("Modal clicado com sucesso.")
        except Exception as e:
            print(f"Erro ao interagir com o modal: {e}")

    def select_requester(self):
        """Clica no botão 'Selecionar Solicitante'."""
        try:
            button = self.wait.until(EC.element_to_be_clickable((By.XPATH, DashboardSelectors.SELECT_REQUESTER_BUTTON)))
            button.click()
            print("Solicitante selecionado com sucesso.")
        except Exception as e:
            print(f"Erro ao selecionar solicitante: {e}")

    def create_new_os(self):
        """Clicar no botão 'criar nova solicitação'."""
        try:
            button = self.wait.until(EC.element_to_be_clickable((By.XPATH, DashboardSelectors.BUTTON_NEW_OS)))
            button.click()
            print("Botão de criar nova solicitação selecionado com sucesso")
        except Exception as e:
            print(f"Erro ao clicar no botão de nova solicitação: {e}")

    def confirm_action(self):
        "Confirmar o inicio de uma nova solicitação"
        try:
            button = self.wait.until(EC.element_to_be_clickable((By.XPATH,DashboardSelectors.CONFIRM_ACTION)))
            button.click()
            print("Selecionando botão de confirmação")
        except Exception as e: 
            print(f"Botão de confirmar ação selecionado com sucesso: {e}")

    def select_label(self):
        "Selecionar etiqueta do plano"
        try:
            button = self.wait.until(EC.element_to_be_clickable((By.XPATH, DashboardSelectors.TABLE_TAG)))
            button.click()
            print("Etiqueta selecionada com sucesso")
        except Exception as e:
            print(f"Erro ao selecionar etiqueta {e}")

    def button_select_label(self):
        "Selecionar botão de etiqueta do plano"
        try:
            button = self.wait.until(EC.element_to_be_clickable((By.XPATH, DashboardSelectors.SELECT_LABEL)))
            button.click()
            print("Botão de selecionar etiqueta selecionado com sucesso")
        except Exception as e:
            print(f"Erro ao selecionar botão de selecionar etiqueta")