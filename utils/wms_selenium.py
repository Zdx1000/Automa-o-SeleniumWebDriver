from utils.navegador import navegador_google
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


class WmsSelenium:
    def __init__(self, navegador=None) -> None:
        if navegador is None:
            self.navegador = navegador_google()
        else:
            self.navegador = navegador

    
    def selenium_click(self, by, value, timeout=20):
        element = WebDriverWait(self.navegador, timeout).until(
            lambda driver: driver.find_element(by, value).is_displayed() and
                           driver.find_element(by, value).is_enabled()
        )
        element = self.navegador.find_element(by, value)
        element.click()

    def selenium_send_keys(self, by, value, keys, timeout=20):
        element = WebDriverWait(self.navegador, timeout).until(
            lambda driver: driver.find_element(by, value).is_displayed() and
                           driver.find_element(by, value).is_enabled()
        )
        element = self.navegador.find_element(by, value)
        element.clear()
        element.send_keys(keys)

    def selenium_click_element(self, by, value, index):
        element = self.navegador.find_elements(by, value)
        element[index].click()

    def selenium_send_keys_element(self, by, value, index, keys):
        element = self.navegador.find_elements(by, value)
        element[index].clear()
        element[index].send_keys(keys)

    
    def login_suplay(self):
        # Login
        self.selenium_click(By.CLASS_NAME, 'actionButton', 20)
        self.selenium_click(By.ID, 'menuButtonToggle', 20)
        self.selenium_click(By.LINK_TEXT, 'Supply Chain Advantage', 20)


