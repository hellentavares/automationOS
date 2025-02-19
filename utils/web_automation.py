from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from config.credentials import SITE_URL, USERNAME, PASSWORD
from config.selectors import LoginSelectors

def login():
    """Função para realizar login no site e retornar o driver."""

    try:
        driver = webdriver.Chrome()
        driver.get(SITE_URL)
        driver.maximize_window()  #Maximiza a janela do navegador


        time.sleep(2)  # Espera carregar a página

        username_field = driver.find_element(By.XPATH, LoginSelectors.USERNAME_FIELD)
        password_field = driver.find_element(By.XPATH, LoginSelectors.PASSWORD_FIELD)
        login_button = driver.find_element(By.XPATH, LoginSelectors.LOGIN_BUTTON)

        username_field.send_keys(USERNAME)
        password_field.send_keys(PASSWORD)
        login_button.click()  # Clica no botão de login

        time.sleep(5)  # Aguarda login

        print("Login realizado com sucesso!")

        return driver  # Retorna o driver para ser usado em outras ações

    except Exception as e:
        print(f"Erro ao realizar login: {e}")
        driver.quit()  # Fecha o navegador em caso de erro
        return None  # Retorna None para evitar erros futuros
