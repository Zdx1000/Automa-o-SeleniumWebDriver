from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep

class BloqueioDAO:
    def __init__(self, navegador, item, quantidades, tipo: int = None, motivo: str = None):
        self.navegador = navegador
        self.item = item
        self.quantidades = quantidades
        self.tipo = tipo
        self.motivo = motivo

    def processo_bloquear(self):
        while True:
            try:
                consus = WebDriverWait(self.navegador, 20).until(
                    lambda driver: driver.find_element(By.CSS_SELECTOR, 'input.k-textbox').is_displayed() and
                                    driver.find_element(By.CSS_SELECTOR, 'input.k-textbox').is_enabled()
                )
                consus = self.navegador.find_element(By.CSS_SELECTOR, 'input.k-textbox')
                consus.send_keys(self.item)
                break
            except:
                pass

        # Consultar
        consultar = WebDriverWait(self.navegador, 20).until(
            lambda driver: driver.find_element(By.LINK_TEXT,
                                                'Consultar').is_displayed() and
                            driver.find_element(By.LINK_TEXT,
                                                'Consultar').is_enabled()
        )
        consultar = self.navegador.find_element(By.LINK_TEXT, 'Consultar')
        consultar.click()


        bloquear = WebDriverWait(self.navegador, 20).until(
            lambda driver: driver.find_element(By.LINK_TEXT,
                                                'Bloqueio').is_displayed() and
                            driver.find_element(By.LINK_TEXT,
                                                'Bloqueio').is_enabled()
        )
        bloquear = self.navegador.find_element(By.LINK_TEXT,
                                            'Bloqueio')
        bloquear.click()
        sleep(1)

        estoque_cont = self.navegador.find_elements(By.CSS_SELECTOR,
                                                'input.k-textbox')
        
        estoque_cont[1].clear()
        sleep(0.5)
        estoque_cont[1].send_keys("99999")



        if self.tipo == 3:
            qtde_bloq = self.navegador.find_elements(By.CSS_SELECTOR,
                                                    'input.k-textbox')
            
            qtde_bloq[8].clear()
            sleep(0.5)
            qtde_bloq[8].send_keys(f"{self.quantidades}")

        elif self.tipo == 1 or self.tipo == 2:
            qtde_bloq = self.navegador.find_elements(By.CSS_SELECTOR,
                                                    'input.k-textbox')
            
            qtde_bloq[7].clear()
            sleep(0.5)
            qtde_bloq[7].send_keys(f"{self.quantidades}")


        if self.tipo == 2:
            motivos = self.navegador.find_elements(By.CSS_SELECTOR,
                                                'span.k-input')
            motivos[2].click()

            sleep(0.5)

            esc = self.navegador.find_elements(By.CSS_SELECTOR,
                            'li.k-item')

            for x in esc:
                if "101 - SALDO" == x.text:
                    x.click()
                    break
        if self.tipo == 3:
            motivos = self.navegador.find_elements(By.CSS_SELECTOR,
                                                'span.k-input')
            motivos[2].click()

            sleep(0.5)

            esc = self.navegador.find_elements(By.CSS_SELECTOR,
                            'li.k-item')
            for x in esc:
                if "99 - Dep. Negociacao" == x.text:
                    x.click()
                    break

        feito2 = WebDriverWait(self.navegador, 20).until(
            lambda driver: driver.find_element(By.LINK_TEXT,
                                                'Bloquear').is_displayed() and
                            driver.find_element(By.LINK_TEXT,
                                                'Bloquear').is_enabled()
        )
        feito2 = self.navegador.find_element(By.LINK_TEXT,
                                        'Bloquear')
        feito2.click()

        sleep(1.5)
        ok4 = WebDriverWait(self.navegador, 20).until(
            lambda driver: driver.find_element(By.CLASS_NAME, 'hj-dlg-button').is_displayed() and
                            driver.find_element(By.CLASS_NAME, 'hj-dlg-button').is_enabled()
        )
        ok4 = self.navegador.find_element(By.CLASS_NAME, 'hj-dlg-button')
        ok4.click()
        sleep(1)
        
        return None
    
    def processo_desbloquear(self):
        while True:
            try:
                consus = WebDriverWait(self.navegador, 20).until(
                    lambda driver: driver.find_element(By.CSS_SELECTOR, 'input.k-textbox').is_displayed() and
                                    driver.find_element(By.CSS_SELECTOR, 'input.k-textbox').is_enabled()
                )
                consus = self.navegador.find_element(By.CSS_SELECTOR, 'input.k-textbox')
                consus.send_keys(self.item)
                break
            except:
                pass

        # Consultar
        consultar = WebDriverWait(self.navegador, 20).until(
            lambda driver: driver.find_element(By.LINK_TEXT,
                                                'Consultar').is_displayed() and
                            driver.find_element(By.LINK_TEXT,
                                                'Consultar').is_enabled()
        )
        consultar = self.navegador.find_element(By.LINK_TEXT, 'Consultar')
        consultar.click()

        sleep(1.5)
        desbloquear = WebDriverWait(self.navegador, 20).until(
            lambda driver: driver.find_element(By.LINK_TEXT,
                                                'Desbloqueio').is_displayed() and
                            driver.find_element(By.LINK_TEXT,
                                                'Desbloqueio').is_enabled()
        )
        desbloquear = self.navegador.find_element(By.LINK_TEXT,
                                                'Desbloqueio')
        desbloquear.click()
        
        sleep(1)
        if self.tipo == 1 or self.tipo == 2:
            click_desbloq = WebDriverWait(self.navegador, 20).until(
                lambda driver: driver.find_element(By.XPATH,
                                                    '/html/body/div[1]/div[2]/div/div/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/div[2]/div[3]/div[1]/hj-flex-container/div/hj-flex-grow/div/div/hj-grid/div[2]/div/div[2]/table/tbody/tr[1]/td[10]/a/hj-label').is_displayed() and
                                driver.find_element(By.XPATH,
                                                    '/html/body/div[1]/div[2]/div/div/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/div[2]/div[3]/div[1]/hj-flex-container/div/hj-flex-grow/div/div/hj-grid/div[2]/div/div[2]/table/tbody/tr[1]/td[10]/a/hj-label').is_enabled()
            )
            click_desbloq = self.navegador.find_element(By.XPATH,
                                                    '/html/body/div[1]/div[2]/div/div/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/div[2]/div[3]/div[1]/hj-flex-container/div/hj-flex-grow/div/div/hj-grid/div[2]/div/div[2]/table/tbody/tr[1]/td[10]/a/hj-label')
            click_desbloq.click()

            # Quantidade a bloquear
            qtd_bloq = WebDriverWait(self.navegador, 20).until(
                lambda driver: driver.find_element(By.XPATH,
                                                    '/html/body/div[1]/div[2]/div/div/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/div[2]/div[4]/div[1]/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/hj-template/div/hj-field-table/div/hj-field-table-row[2]/div/hj-field-group/div/div[2]/hj-field-group-row[2]/div/hj-field-cell/div/hj-field-control/div/div/span[1]/hj-template/div/hj-textbox/input').is_displayed() and
                                driver.find_element(By.XPATH,
                                                    '/html/body/div[1]/div[2]/div/div/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/div[2]/div[4]/div[1]/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/hj-template/div/hj-field-table/div/hj-field-table-row[2]/div/hj-field-group/div/div[2]/hj-field-group-row[2]/div/hj-field-cell/div/hj-field-control/div/div/span[1]/hj-template/div/hj-textbox/input').is_enabled()
            )
            qtd_bloq = self.navegador.find_element(By.XPATH,
                                                '/html/body/div[1]/div[2]/div/div/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/div[2]/div[4]/div[1]/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/hj-template/div/hj-field-table/div/hj-field-table-row[2]/div/hj-field-group/div/div[2]/hj-field-group-row[2]/div/hj-field-cell/div/hj-field-control/div/div/span[1]/hj-template/div/hj-textbox/input')
            qtd_bloq.send_keys(self.quantidades)

            motivos = WebDriverWait(self.navegador, 20).until(
                lambda driver: driver.find_element(By.XPATH,
                                                    '/html/body/div[1]/div[2]/div/div/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/div[2]/div[4]/div[1]/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/hj-template/div/hj-field-table/div/hj-field-table-row[2]/div/hj-field-group/div/div[2]/hj-field-group-row[3]/div/hj-field-cell/div/hj-field-control/div/div/span[1]/hj-template/div/hj-dropdownlist/span').is_displayed() and
                                driver.find_element(By.XPATH,
                                                    '/html/body/div[1]/div[2]/div/div/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/div[2]/div[4]/div[1]/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/hj-template/div/hj-field-table/div/hj-field-table-row[2]/div/hj-field-group/div/div[2]/hj-field-group-row[3]/div/hj-field-cell/div/hj-field-control/div/div/span[1]/hj-template/div/hj-dropdownlist/span').is_enabled()
            )
            motivos = self.navegador.find_element(By.XPATH,
                                                '/html/body/div[1]/div[2]/div/div/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/div[2]/div[4]/div[1]/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/hj-template/div/hj-field-table/div/hj-field-table-row[2]/div/hj-field-group/div/div[2]/hj-field-group-row[3]/div/hj-field-cell/div/hj-field-control/div/div/span[1]/hj-template/div/hj-dropdownlist/span')
            motivos.click()
        elif self.tipo == 3:
            click_desbloq = WebDriverWait(self.navegador, 20).until(
                lambda driver: driver.find_element(By.XPATH,
                                                    '/html/body/div[1]/div[2]/div/div/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/div[2]/div[3]/div[1]/hj-flex-container/div/hj-flex-grow/div/div/hj-grid/div[2]/div/div[2]/table/tbody/tr[2]/td[10]/a/hj-label').is_displayed() and
                                driver.find_element(By.XPATH,
                                                    '/html/body/div[1]/div[2]/div/div/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/div[2]/div[3]/div[1]/hj-flex-container/div/hj-flex-grow/div/div/hj-grid/div[2]/div/div[2]/table/tbody/tr[2]/td[10]/a/hj-label').is_enabled()
            )
            click_desbloq = self.navegador.find_element(By.XPATH,
                                                    '/html/body/div[1]/div[2]/div/div/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/div[2]/div[3]/div[1]/hj-flex-container/div/hj-flex-grow/div/div/hj-grid/div[2]/div/div[2]/table/tbody/tr[2]/td[10]/a/hj-label')
            click_desbloq.click()

            # Quantidade a bloquear
            qtd_bloq = WebDriverWait(self.navegador, 20).until(
                lambda driver: driver.find_element(By.XPATH,
                                                    '/html/body/div[1]/div[2]/div/div/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/div[2]/div[4]/div[1]/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/hj-template/div/hj-field-table/div/hj-field-table-row[2]/div/hj-field-group/div/div[2]/hj-field-group-row[2]/div/hj-field-cell/div/hj-field-control/div/div/span[1]/hj-template/div/hj-textbox/input').is_displayed() and
                                driver.find_element(By.XPATH,
                                                    '/html/body/div[1]/div[2]/div/div/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/div[2]/div[4]/div[1]/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/hj-template/div/hj-field-table/div/hj-field-table-row[2]/div/hj-field-group/div/div[2]/hj-field-group-row[2]/div/hj-field-cell/div/hj-field-control/div/div/span[1]/hj-template/div/hj-textbox/input').is_enabled()
            )
            qtd_bloq = self.navegador.find_element(By.XPATH,
                                                '/html/body/div[1]/div[2]/div/div/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/div[2]/div[4]/div[1]/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/hj-template/div/hj-field-table/div/hj-field-table-row[2]/div/hj-field-group/div/div[2]/hj-field-group-row[2]/div/hj-field-cell/div/hj-field-control/div/div/span[1]/hj-template/div/hj-textbox/input')
            qtd_bloq.send_keys(self.quantidades)

            motivos = WebDriverWait(self.navegador, 20).until(
                lambda driver: driver.find_element(By.XPATH,
                                                    '/html/body/div[1]/div[2]/div/div/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/div[2]/div[4]/div[1]/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/hj-template/div/hj-field-table/div/hj-field-table-row[2]/div/hj-field-group/div/div[2]/hj-field-group-row[3]/div/hj-field-cell/div/hj-field-control/div/div/span[1]/hj-template/div/hj-dropdownlist/span').is_displayed() and
                                driver.find_element(By.XPATH,
                                                    '/html/body/div[1]/div[2]/div/div/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/div[2]/div[4]/div[1]/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/hj-template/div/hj-field-table/div/hj-field-table-row[2]/div/hj-field-group/div/div[2]/hj-field-group-row[3]/div/hj-field-cell/div/hj-field-control/div/div/span[1]/hj-template/div/hj-dropdownlist/span').is_enabled()
            )
            motivos = self.navegador.find_element(By.XPATH,
                                                '/html/body/div[1]/div[2]/div/div/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/div[2]/div[4]/div[1]/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/hj-template/div/hj-field-table/div/hj-field-table-row[2]/div/hj-field-group/div/div[2]/hj-field-group-row[3]/div/hj-field-cell/div/hj-field-control/div/div/span[1]/hj-template/div/hj-dropdownlist/span')
            motivos.click()
            

        if self.tipo == 1:
            esc = self.navegador.find_elements(By.CSS_SELECTOR,
                                            'li.k-item')
            for x in esc:
                if "01 - Merc.Perdida" == x.text:
                    x.click()
                    break
        elif self.tipo == 2:
            esc = self.navegador.find_elements(By.CSS_SELECTOR,
                                            'li.k-item')
            for x in esc:
                if "101 - SALDO" == x.text:
                    x.click()
                    break
        elif self.tipo == 3:
            esc = self.navegador.find_elements(By.CSS_SELECTOR,
                                            'li.k-item')
            for x in esc:
                if "99 - Dep. Negociacao" == x.text:
                    x.click()
                    break


        feito = self.navegador.find_element(
            By.LINK_TEXT,
            'Desbloquear'
        )
        sleep(1)
        feito.click()

        sleep(1)

        ok4 = WebDriverWait(self.navegador, 20).until(
            lambda driver: driver.find_element(By.CLASS_NAME, 'hj-dlg-button').is_displayed() and
                            driver.find_element(By.CLASS_NAME, 'hj-dlg-button').is_enabled()
        )
        ok4 = self.navegador.find_element(By.CLASS_NAME, 'hj-dlg-button')
        ok4.click()
        return None
    
    def processo_bloquear_sem_consulta(self):

        bloquear = WebDriverWait(self.navegador, 20).until(
            lambda driver: driver.find_element(By.LINK_TEXT,
                                                'Bloqueio').is_displayed() and
                            driver.find_element(By.LINK_TEXT,
                                                'Bloqueio').is_enabled()
        )
        bloquear = self.navegador.find_element(By.LINK_TEXT,
                                            'Bloqueio')
        bloquear.click()
        sleep(1)

        estoque_cont = self.navegador.find_elements(By.CSS_SELECTOR,
                                                'input.k-textbox')
        
        estoque_cont[1].clear()
        sleep(0.5)
        estoque_cont[1].send_keys("99999")



        if self.tipo == 3:
            qtde_bloq = self.navegador.find_elements(By.CSS_SELECTOR,
                                                    'input.k-textbox')
            
            qtde_bloq[8].clear()
            sleep(0.5)
            qtde_bloq[8].send_keys(f"{self.quantidades}")

        elif self.tipo == 1 or self.tipo == 2:
            qtde_bloq = self.navegador.find_elements(By.CSS_SELECTOR,
                                                    'input.k-textbox')
            
            qtde_bloq[7].clear()
            sleep(0.5)
            qtde_bloq[7].send_keys(f"{self.quantidades}")


        if self.tipo == 2:
            motivos = self.navegador.find_elements(By.CSS_SELECTOR,
                                                'span.k-input')
            motivos[2].click()

            sleep(0.5)

            esc = self.navegador.find_elements(By.CSS_SELECTOR,
                            'li.k-item')

            for x in esc:
                if "101 - SALDO" == x.text:
                    x.click()
                    break
        if self.tipo == 3:
            motivos = self.navegador.find_elements(By.CSS_SELECTOR,
                                                'span.k-input')
            motivos[2].click()

            sleep(0.5)

            esc = self.navegador.find_elements(By.CSS_SELECTOR,
                            'li.k-item')
            for x in esc:
                if "99 - Dep. Negociacao" == x.text:
                    x.click()
                    break

        feito2 = WebDriverWait(self.navegador, 20).until(
            lambda driver: driver.find_element(By.LINK_TEXT,
                                                'Bloquear').is_displayed() and
                            driver.find_element(By.LINK_TEXT,
                                                'Bloquear').is_enabled()
        )
        feito2 = self.navegador.find_element(By.LINK_TEXT,
                                        'Bloquear')
        feito2.click()

        sleep(1.5)
        ok4 = WebDriverWait(self.navegador, 20).until(
            lambda driver: driver.find_element(By.CLASS_NAME, 'hj-dlg-button').is_displayed() and
                            driver.find_element(By.CLASS_NAME, 'hj-dlg-button').is_enabled()
        )
        ok4 = self.navegador.find_element(By.CLASS_NAME, 'hj-dlg-button')
        ok4.click()
        sleep(1)
        
        return None
    
    def processo_desbloquear_sem_consultar(self):

        sleep(1.5)
        desbloquear = WebDriverWait(self.navegador, 20).until(
            lambda driver: driver.find_element(By.LINK_TEXT,
                                                'Desbloqueio').is_displayed() and
                            driver.find_element(By.LINK_TEXT,
                                                'Desbloqueio').is_enabled()
        )
        desbloquear = self.navegador.find_element(By.LINK_TEXT,
                                                'Desbloqueio')
        desbloquear.click()
        
        sleep(1)
        if self.tipo == 1 or self.tipo == 2:
            click_desbloq = WebDriverWait(self.navegador, 20).until(
                lambda driver: driver.find_element(By.XPATH,
                                                    '/html/body/div[1]/div[2]/div/div/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/div[2]/div[3]/div[1]/hj-flex-container/div/hj-flex-grow/div/div/hj-grid/div[2]/div/div[2]/table/tbody/tr[1]/td[10]/a/hj-label').is_displayed() and
                                driver.find_element(By.XPATH,
                                                    '/html/body/div[1]/div[2]/div/div/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/div[2]/div[3]/div[1]/hj-flex-container/div/hj-flex-grow/div/div/hj-grid/div[2]/div/div[2]/table/tbody/tr[1]/td[10]/a/hj-label').is_enabled()
            )
            click_desbloq = self.navegador.find_element(By.XPATH,
                                                    '/html/body/div[1]/div[2]/div/div/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/div[2]/div[3]/div[1]/hj-flex-container/div/hj-flex-grow/div/div/hj-grid/div[2]/div/div[2]/table/tbody/tr[1]/td[10]/a/hj-label')
            click_desbloq.click()

            # Quantidade a bloquear
            qtd_bloq = WebDriverWait(self.navegador, 20).until(
                lambda driver: driver.find_element(By.XPATH,
                                                    '/html/body/div[1]/div[2]/div/div/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/div[2]/div[4]/div[1]/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/hj-template/div/hj-field-table/div/hj-field-table-row[2]/div/hj-field-group/div/div[2]/hj-field-group-row[2]/div/hj-field-cell/div/hj-field-control/div/div/span[1]/hj-template/div/hj-textbox/input').is_displayed() and
                                driver.find_element(By.XPATH,
                                                    '/html/body/div[1]/div[2]/div/div/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/div[2]/div[4]/div[1]/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/hj-template/div/hj-field-table/div/hj-field-table-row[2]/div/hj-field-group/div/div[2]/hj-field-group-row[2]/div/hj-field-cell/div/hj-field-control/div/div/span[1]/hj-template/div/hj-textbox/input').is_enabled()
            )
            qtd_bloq = self.navegador.find_element(By.XPATH,
                                                '/html/body/div[1]/div[2]/div/div/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/div[2]/div[4]/div[1]/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/hj-template/div/hj-field-table/div/hj-field-table-row[2]/div/hj-field-group/div/div[2]/hj-field-group-row[2]/div/hj-field-cell/div/hj-field-control/div/div/span[1]/hj-template/div/hj-textbox/input')
            qtd_bloq.send_keys(self.quantidades)

            motivos = WebDriverWait(self.navegador, 20).until(
                lambda driver: driver.find_element(By.XPATH,
                                                    '/html/body/div[1]/div[2]/div/div/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/div[2]/div[4]/div[1]/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/hj-template/div/hj-field-table/div/hj-field-table-row[2]/div/hj-field-group/div/div[2]/hj-field-group-row[3]/div/hj-field-cell/div/hj-field-control/div/div/span[1]/hj-template/div/hj-dropdownlist/span').is_displayed() and
                                driver.find_element(By.XPATH,
                                                    '/html/body/div[1]/div[2]/div/div/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/div[2]/div[4]/div[1]/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/hj-template/div/hj-field-table/div/hj-field-table-row[2]/div/hj-field-group/div/div[2]/hj-field-group-row[3]/div/hj-field-cell/div/hj-field-control/div/div/span[1]/hj-template/div/hj-dropdownlist/span').is_enabled()
            )
            motivos = self.navegador.find_element(By.XPATH,
                                                '/html/body/div[1]/div[2]/div/div/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/div[2]/div[4]/div[1]/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/hj-template/div/hj-field-table/div/hj-field-table-row[2]/div/hj-field-group/div/div[2]/hj-field-group-row[3]/div/hj-field-cell/div/hj-field-control/div/div/span[1]/hj-template/div/hj-dropdownlist/span')
            motivos.click()
        elif self.tipo == 3:
            click_desbloq = WebDriverWait(self.navegador, 20).until(
                lambda driver: driver.find_element(By.XPATH,
                                                    '/html/body/div[1]/div[2]/div/div/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/div[2]/div[3]/div[1]/hj-flex-container/div/hj-flex-grow/div/div/hj-grid/div[2]/div/div[2]/table/tbody/tr[2]/td[10]/a/hj-label').is_displayed() and
                                driver.find_element(By.XPATH,
                                                    '/html/body/div[1]/div[2]/div/div/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/div[2]/div[3]/div[1]/hj-flex-container/div/hj-flex-grow/div/div/hj-grid/div[2]/div/div[2]/table/tbody/tr[2]/td[10]/a/hj-label').is_enabled()
            )
            click_desbloq = self.navegador.find_element(By.XPATH,
                                                    '/html/body/div[1]/div[2]/div/div/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/div[2]/div[3]/div[1]/hj-flex-container/div/hj-flex-grow/div/div/hj-grid/div[2]/div/div[2]/table/tbody/tr[2]/td[10]/a/hj-label')
            click_desbloq.click()

            # Quantidade a bloquear
            qtd_bloq = WebDriverWait(self.navegador, 20).until(
                lambda driver: driver.find_element(By.XPATH,
                                                    '/html/body/div[1]/div[2]/div/div/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/div[2]/div[4]/div[1]/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/hj-template/div/hj-field-table/div/hj-field-table-row[2]/div/hj-field-group/div/div[2]/hj-field-group-row[2]/div/hj-field-cell/div/hj-field-control/div/div/span[1]/hj-template/div/hj-textbox/input').is_displayed() and
                                driver.find_element(By.XPATH,
                                                    '/html/body/div[1]/div[2]/div/div/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/div[2]/div[4]/div[1]/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/hj-template/div/hj-field-table/div/hj-field-table-row[2]/div/hj-field-group/div/div[2]/hj-field-group-row[2]/div/hj-field-cell/div/hj-field-control/div/div/span[1]/hj-template/div/hj-textbox/input').is_enabled()
            )
            qtd_bloq = self.navegador.find_element(By.XPATH,
                                                '/html/body/div[1]/div[2]/div/div/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/div[2]/div[4]/div[1]/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/hj-template/div/hj-field-table/div/hj-field-table-row[2]/div/hj-field-group/div/div[2]/hj-field-group-row[2]/div/hj-field-cell/div/hj-field-control/div/div/span[1]/hj-template/div/hj-textbox/input')
            qtd_bloq.send_keys(self.quantidades)

            motivos = WebDriverWait(self.navegador, 20).until(
                lambda driver: driver.find_element(By.XPATH,
                                                    '/html/body/div[1]/div[2]/div/div/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/div[2]/div[4]/div[1]/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/hj-template/div/hj-field-table/div/hj-field-table-row[2]/div/hj-field-group/div/div[2]/hj-field-group-row[3]/div/hj-field-cell/div/hj-field-control/div/div/span[1]/hj-template/div/hj-dropdownlist/span').is_displayed() and
                                driver.find_element(By.XPATH,
                                                    '/html/body/div[1]/div[2]/div/div/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/div[2]/div[4]/div[1]/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/hj-template/div/hj-field-table/div/hj-field-table-row[2]/div/hj-field-group/div/div[2]/hj-field-group-row[3]/div/hj-field-cell/div/hj-field-control/div/div/span[1]/hj-template/div/hj-dropdownlist/span').is_enabled()
            )
            motivos = self.navegador.find_element(By.XPATH,
                                                '/html/body/div[1]/div[2]/div/div/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/div[2]/div[4]/div[1]/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/hj-template/div/hj-field-table/div/hj-field-table-row[2]/div/hj-field-group/div/div[2]/hj-field-group-row[3]/div/hj-field-cell/div/hj-field-control/div/div/span[1]/hj-template/div/hj-dropdownlist/span')
            motivos.click()
            

        if self.tipo == 1:
            esc = self.navegador.find_elements(By.CSS_SELECTOR,
                                            'li.k-item')
            for x in esc:
                if "01 - Merc.Perdida" == x.text:
                    x.click()
                    break
        elif self.tipo == 2:
            esc = self.navegador.find_elements(By.CSS_SELECTOR,
                                            'li.k-item')
            for x in esc:
                if "101 - SALDO" == x.text:
                    x.click()
                    break
        elif self.tipo == 3:
            esc = self.navegador.find_elements(By.CSS_SELECTOR,
                                            'li.k-item')
            for x in esc:
                if "99 - Dep. Negociacao" == x.text:
                    x.click()
                    break


        feito = self.navegador.find_element(
            By.LINK_TEXT,
            'Desbloquear'
        )
        sleep(1)
        feito.click()

        sleep(1)

        ok4 = WebDriverWait(self.navegador, 20).until(
            lambda driver: driver.find_element(By.CLASS_NAME, 'hj-dlg-button').is_displayed() and
                            driver.find_element(By.CLASS_NAME, 'hj-dlg-button').is_enabled()
        )
        ok4 = self.navegador.find_element(By.CLASS_NAME, 'hj-dlg-button')
        ok4.click()
        return None