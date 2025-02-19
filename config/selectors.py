class LoginSelectors:
    """Classe contendo os seletores da página de login."""
    USERNAME_FIELD = '/html/body/section/div[2]/form/input[1]'  
    PASSWORD_FIELD = '//*[@id="UserPassword2"]'
    LOGIN_BUTTON = '//*[@id="ButtonLogin"]'

class DashboardSelectors:
    """Classe contendo os seletores das ações dentro do sistema."""
    START_BUTTON = '//*[@id="assignmentTasks_wrapper"]/div[1]/div[4]/button'  # Iniciar atendimento
    CLICK_BUTTON = '/html/body/div[5]/div[3]/div[1]/div[1]/div[1]/div/span/button'  # Fechar O.S interna
    OS_BUTTON = '//*[@id="erpToolbar"]/div[3]/button[1]'  # Iniciar O.S externa
    SEARCH_USER = '//*[@id="search"]'  # Campo para digitar o documento do usuário
    START_NEW_SERVICE = '//button[@tooltip="Iniciar um novo atendimento"]'
    MODAL_SELECTOR = '/html/body/div[6]/div[3]/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/div/div'
    SELECT_REQUESTER_BUTTON = '/html/body/div[6]/div[3]/div/div[2]/button[1]'
    BUTTON_NEW_OS = '/html/body/div[6]/div[3]/div/div[2]/button[1]'
    CONFIRM_ACTION = '/html/body/div[6]/div[3]/div/div[3]/button[1]'
    TABLE_TAG = '//*[contains(text(), "Origem do Endereço")]'
    SELECT_LABEL = '/html/body/div[4]/div[3]/div/div[2]/button'


class AutomationOs: 
    """Classe para ações feitas após a O.S ser aberta"""
    CATEGORY_ONE = '//*[@id="serviceCategoryId1"]'
    SELECT_ADM = '//*[@id="serviceCategoryId1="Administrativo"]'
 