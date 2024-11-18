from selenium.common.exceptions import *
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep
import pyautogui


def iniciar_driver():
    chrome_options = Options()
    arguments = ['--lang=pt-BR', '--window-size=1300,1000', '--incognito']
    for argument in arguments:
        chrome_options.add_argument(argument)

    chrome_options.add_experimental_option('prefs', {
        'download.prompt_for_download': False,
        'profile.default_content_setting_values.notifications': 2,
        'profile.default_content_setting_values.automatic_downloads': 1,

    })
    driver = webdriver.Chrome(service=ChromeService(
        ChromeDriverManager().install()), options=chrome_options)

    wait = WebDriverWait(
        driver,
        10,
        poll_frequency=1,
        ignored_exceptions=[
            NoSuchElementException,
            ElementNotVisibleException,
            ElementNotSelectableException,
        ]
    )
    return driver, wait


driver, wait = iniciar_driver()
# Entrar no site do instagram
driver.get('https://www.instagram.com/')
pyautogui.alert(text='Insira seu e-mail e senha e entre, após isso a automação iniciará.')
sleep(40)
# Verificar se postagem foi curtida, caso não tenha sido, clicar curtir, caso já tenha sido, aguardar 24hrs
while True:
    # Navegar até a página alvo
    driver.get('https://instagram.com/devaprender')
    sleep(5)
    # Clicar na última  postagem
    postagens = wait.until(EC.visibility_of_any_elements_located(
        (By.XPATH, "//div[@class='_aagu']")))
    sleep(5)
    postagens[0].click()
    # Verificar se postagem foi curtida, caso não tenha sido, clicar curtir, caso já tenha sido, aguardar 24hrs
    elementos_postagem = wait.until(EC.visibility_of_any_elements_located(
        (By.XPATH, "//div[@class='_abm0 _abl_']")))
    if len(elementos_postagem) == 6:
        elementos_postagem[0].click()
        sleep(86400)
    else:
        print('postagem já foi curtida')
        sleep(86400)