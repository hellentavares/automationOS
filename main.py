from utils.web_automation import login
from utils.actions import DashboardActions
from utils.data_handler import get_first_document
import time
from utils.os_automations import Osactions

""" Faz login e retorna o driver """
if __name__ == "__main__":
    driver = login()  
    
    if driver:  # Verifica se o login foi bem-sucedido
        try:
            actions = DashboardActions(driver) 
            os_actions = Osactions(driver)

            # Executa ações antes da busca
            actions.start_service()
            actions.close_internal_os()
            actions.start_external_os()

            # Obtém um documento para teste
            excel_path = "data/users_to_search.xlsx"
            document = get_first_document(excel_path)

            if document:
                print("Iniciando pesquisa do usuário...")
                actions.search_user(document)  
                time.sleep(3)
                
                print("Iniciando novo serviço...")
                actions.start_new_service() 
                time.sleep(3)

                print("Fechando modal, se necessário...")
                actions.handle_modal()  
                time.sleep(3)

                print('Selecionando solicitante...')
                actions.select_requester() 
                time.sleep(3)

                print("Selecionando nova O.S...")
                actions.create_new_os()
                time.sleep(3)

                print("Selecionando botão de confirmar...")
                actions.confirm_action()
                time.sleep(3)

                print("Selecionando etiqueta...")
                actions.select_label()
                time.sleep(3)

                print("Abrindo O.S...")
                actions.button_select_label()
                time.sleep(3)

                print("Selecionando a primeira categoria...")
                os_actions.first_category()
                time.sleep(3)

                print("Selecionando seletor 'Administrativo'...")
                os_actions.select_adm()

            time.sleep(20)  # Aguarda antes de fechar

        finally:
            driver.quit()  
    else:
        print("Error: Login failed. Check credentials or selectors.")
