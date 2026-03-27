from time import sleep

from selenium.common.exceptions import (
    ElementClickInterceptedException,
    StaleElementReferenceException,
)
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def clicar_quando_estavel(navegador, locator, timeout=20, tentativas=3):
    ultimo_erro = None

    for tentativa in range(tentativas):
        try:
            elemento = WebDriverWait(
                navegador,
                timeout,
                ignored_exceptions=(StaleElementReferenceException,),
            ).until(EC.element_to_be_clickable(locator))

            navegador.execute_script(
                "arguments[0].scrollIntoView({block: 'center', inline: 'nearest'});",
                elemento,
            )

            try:
                elemento.click()
            except ElementClickInterceptedException:
                navegador.execute_script("arguments[0].click();", elemento)

            return elemento
        except StaleElementReferenceException as erro:
            ultimo_erro = erro

            if tentativa < tentativas - 1:
                sleep(0.3)

    raise ultimo_erro
