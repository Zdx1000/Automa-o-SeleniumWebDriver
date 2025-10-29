from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import pandas as pd
from utils.shared import historico_funcoes, registrar_progresso
from utils.retornar import cancelar_inputs
from utils.navegador import navegador_google
from time import sleep
from selenium.webdriver.support import expected_conditions as EC

def classArmazenagem():
    from main import tabela

    historico_funcoes.append(tabela)

    try:
        navegador = navegador_google()
    except:
        try:
            navegador.quit()
        except:
            pass
        return cancelar_inputs()

    try:
        # Login
        login = WebDriverWait(navegador, 20).until(
            lambda driver: driver.find_element(By.CLASS_NAME, 'actionButton').is_displayed() and
                            driver.find_element(By.CLASS_NAME, 'actionButton').is_enabled()
        )
        login = navegador.find_element(By.CLASS_NAME, 'actionButton')
        login.click()

        # Menu barra
        barra = WebDriverWait(navegador, 20).until(
            lambda driver: driver.find_element(By.ID, 'menuButtonToggle').is_displayed() and
                            driver.find_element(By.ID, 'menuButtonToggle').is_enabled()
        )
        barra = navegador.find_element(By.ID, 'menuButtonToggle')
        barra.click()

        # Menu supply
        supply = WebDriverWait(navegador, 20).until(
            lambda driver: driver.find_element(By.LINK_TEXT, 'Supply Chain Advantage').is_displayed() and
                            driver.find_element(By.LINK_TEXT, 'Supply Chain Advantage').is_enabled()
        )
        supply = navegador.find_element(By.LINK_TEXT, 'Supply Chain Advantage')
        supply.click()

            # Menu supply
        warehouse = WebDriverWait(navegador, 20).until(
            lambda driver: driver.find_element(By.LINK_TEXT, 'Warehouse Advantage').is_displayed() and
                            driver.find_element(By.LINK_TEXT, 'Warehouse Advantage').is_enabled()
        )
        warehouse = navegador.find_element(By.LINK_TEXT, 'Warehouse Advantage')
        warehouse.click()

        config = WebDriverWait(navegador, 20).until(
            lambda driver: driver.find_element(By.LINK_TEXT, 'Configuração Armazém').is_displayed() and
                            driver.find_element(By.LINK_TEXT, 'Configuração Armazém').is_enabled()
        )
        config = navegador.find_element(By.LINK_TEXT, 'Configuração Armazém')
        config.click()

        itens_ = WebDriverWait(navegador, 20).until(
            lambda driver: driver.find_element(By.LINK_TEXT, 'Itens').is_displayed() and
                            driver.find_element(By.LINK_TEXT, 'Itens').is_enabled()
        )
        itens_ = navegador.find_element(By.LINK_TEXT, 'Itens')
        itens_.click()

        class_ = WebDriverWait(navegador, 20).until(
            lambda driver: driver.find_element(By.LINK_TEXT, 'Itens sem Classe de Armazenagem').is_displayed() and
                            driver.find_element(By.LINK_TEXT, 'Itens sem Classe de Armazenagem').is_enabled()
        )
        class_ = navegador.find_element(By.LINK_TEXT, 'Itens sem Classe de Armazenagem')
        class_.click()

                # Menu supply
        consultar = WebDriverWait(navegador, 20).until(
            lambda driver: driver.find_element(By.LINK_TEXT, 'Consulta').is_displayed() and
                            driver.find_element(By.LINK_TEXT, 'Consulta').is_enabled()
        )
        consultar = navegador.find_element(By.LINK_TEXT, 'Consulta')
        consultar.click()

        try:
            file_path = 'Banco de dados.xlsx'
            file_path = pd.ExcelFile(file_path)
            file_path.sheet_names

            sheet_data = file_path.parse('classArmazenagem')
            qtde = file_path.parse('classArmazenagem')
            sheet_data.head()
            qtde.head()
            itens = sheet_data['Itens']
            classes = qtde['class']
        except:
            print(f"Erro  ao acessar o arquivo Banco de dados.xlsx!!!")
            try:
                navegador.quit()
            except:
                pass
            return cancelar_inputs()
        cont = 0
        for item, classe in zip(itens, classes):
            try:
                if cont == 0:
                    filtro = WebDriverWait(navegador, 40).until(
                        lambda driver: driver.find_element(By.CSS_SELECTOR,
                                                        'th[data-title="Item"] a.k-header-column-menu span.k-icon.k-i-more-vertical').is_displayed() and
                                    driver.find_element(By.CSS_SELECTOR,
                                                        'th[data-title="Item"] a.k-header-column-menu span.k-icon.k-i-more-vertical').is_enabled()
                    )
                    filtro = navegador.find_element(By.CSS_SELECTOR,
                                                    'th[data-title="Item"] a.k-header-column-menu span.k-icon.k-i-more-vertical')
                    filtro.click()
                else:
                    filtro = WebDriverWait(navegador, 40).until(
                        lambda driver: driver.find_element(By.CSS_SELECTOR,
                                                        'th[data-title="Item"] a.k-header-column-menu span.k-icon.k-i-filter').is_displayed() and
                                    driver.find_element(By.CSS_SELECTOR,
                                                        'th[data-title="Item"] a.k-header-column-menu span.k-icon.k-i-filter').is_enabled()
                    )
                    filtro = navegador.find_element(By.CSS_SELECTOR,
                                                    'th[data-title="Item"] a.k-header-column-menu span.k-icon.k-i-filter')
                    filtro.click()
                
                cont += 1
                print(f"Item: {item}, Classe: {classe} - {cont}/{len(itens)}")
            

                filtro_menu = WebDriverWait(navegador, 10).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, "li.k-filter-item span.k-link"))
                )
                filtro_menu.click()

                sleep(1)
                texto_para_inserir = int(item)
                navegador.execute_script("""
                    var campo = document.querySelector("input[data-bind='value:filters[0].value']");
                    campo.value = arguments[0];
                    campo.dispatchEvent(new Event('input', { bubbles: true }));
                    campo.dispatchEvent(new Event('change', { bubbles: true }));
                """, texto_para_inserir)
                sleep(1)

                filter_cl = WebDriverWait(navegador, 20).until(
                    lambda driver: driver.find_element(By.CSS_SELECTOR, 'button.k-button').is_displayed() and
                                driver.find_element(By.CSS_SELECTOR, 'button.k-button').is_enabled()
                )
                filter_cl = navegador.find_element(By.CSS_SELECTOR, 'button.k-button')
                filter_cl.click()
                while True:
                    try:
                        itens_list = WebDriverWait(navegador, 20).until(
                            lambda driver: driver.find_element(By.LINK_TEXT, f'{int(item)}').is_displayed() and
                                        driver.find_element(By.LINK_TEXT, f'{int(item)}').is_enabled()
                        )
                        itens_list = navegador.find_element(By.LINK_TEXT, f'{int(item)}')
                        itens_list.click()
                        break
                    except:
                        sleep(0.5)

                index_1 = WebDriverWait(navegador, 20).until(
                    lambda driver: next((
                        link for link in driver.find_elements(By.CSS_SELECTOR, 'a.hj-link')
                        if link.text.strip() == '1'
                    ), None)
                )
                index_1.click()

                dropdown_sem_classe = WebDriverWait(navegador, 20).until(
                    lambda driver: next((
                        span for span in driver.find_elements(By.CSS_SELECTOR, 'span.k-input')
                        if span.text.strip() == '<Nenhum>'
                    ), None)
                )
                dropdown_sem_classe.click()

                # ClassNome
                list_classes = WebDriverWait(navegador, 20).until(
                    lambda driver: [
                        li for li in driver.find_elements(By.CSS_SELECTOR, 'li.k-item')
                        if li.is_displayed()
                    ]
                )

                for classe_item in list_classes:
                    if classe_item.text.strip() == f'{classe}':
                        classe_item.click()
                        break


                altera = WebDriverWait(navegador, 20).until(
                    lambda driver: driver.find_element(By.LINK_TEXT, 'Alterar').is_displayed() and
                                    driver.find_element(By.LINK_TEXT, 'Alterar').is_enabled()
                )
                altera = navegador.find_element(By.LINK_TEXT, 'Alterar')
                altera.click()

                sleep(2)

                voltar = WebDriverWait(navegador, 20).until(
                    lambda driver: driver.find_element(By.CSS_SELECTOR, "a[data-hj-test-id='active-thread-previous-button']").is_displayed() and
                                driver.find_element(By.CSS_SELECTOR, "a[data-hj-test-id='active-thread-previous-button']").is_enabled()
                )
                voltar = navegador.find_element(By.CSS_SELECTOR, "a[data-hj-test-id='active-thread-previous-button']")
                voltar.click()
            except Exception as e:
                print(f"Erro ao processar item {item}: {e}")
                cont += 1

                file_path.close()
                navegador.quit()

                navegador = navegador_google()

                cont = 0
                try:
                    # Login
                    login = WebDriverWait(navegador, 20).until(
                        lambda driver: driver.find_element(By.CLASS_NAME, 'actionButton').is_displayed() and
                                        driver.find_element(By.CLASS_NAME, 'actionButton').is_enabled()
                    )
                    login = navegador.find_element(By.CLASS_NAME, 'actionButton')
                    login.click()

                    # Menu barra
                    barra = WebDriverWait(navegador, 20).until(
                        lambda driver: driver.find_element(By.ID, 'menuButtonToggle').is_displayed() and
                                        driver.find_element(By.ID, 'menuButtonToggle').is_enabled()
                    )
                    barra = navegador.find_element(By.ID, 'menuButtonToggle')
                    barra.click()

                    # Menu supply
                    supply = WebDriverWait(navegador, 20).until(
                        lambda driver: driver.find_element(By.LINK_TEXT, 'Supply Chain Advantage').is_displayed() and
                                        driver.find_element(By.LINK_TEXT, 'Supply Chain Advantage').is_enabled()
                    )
                    supply = navegador.find_element(By.LINK_TEXT, 'Supply Chain Advantage')
                    supply.click()

                        # Menu supply
                    warehouse = WebDriverWait(navegador, 20).until(
                        lambda driver: driver.find_element(By.LINK_TEXT, 'Warehouse Advantage').is_displayed() and
                                        driver.find_element(By.LINK_TEXT, 'Warehouse Advantage').is_enabled()
                    )
                    warehouse = navegador.find_element(By.LINK_TEXT, 'Warehouse Advantage')
                    warehouse.click()

                    config = WebDriverWait(navegador, 20).until(
                        lambda driver: driver.find_element(By.LINK_TEXT, 'Configuração Armazém').is_displayed() and
                                        driver.find_element(By.LINK_TEXT, 'Configuração Armazém').is_enabled()
                    )
                    config = navegador.find_element(By.LINK_TEXT, 'Configuração Armazém')
                    config.click()

                    itens_ = WebDriverWait(navegador, 20).until(
                        lambda driver: driver.find_element(By.LINK_TEXT, 'Itens').is_displayed() and
                                        driver.find_element(By.LINK_TEXT, 'Itens').is_enabled()
                    )
                    itens_ = navegador.find_element(By.LINK_TEXT, 'Itens')
                    itens_.click()

                    class_ = WebDriverWait(navegador, 20).until(
                        lambda driver: driver.find_element(By.LINK_TEXT, 'Itens sem Classe de Armazenagem').is_displayed() and
                                        driver.find_element(By.LINK_TEXT, 'Itens sem Classe de Armazenagem').is_enabled()
                    )
                    class_ = navegador.find_element(By.LINK_TEXT, 'Itens sem Classe de Armazenagem')
                    class_.click()

                            # Menu supply
                    consultar = WebDriverWait(navegador, 20).until(
                        lambda driver: driver.find_element(By.LINK_TEXT, 'Consulta').is_displayed() and
                                        driver.find_element(By.LINK_TEXT, 'Consulta').is_enabled()
                    )
                    consultar = navegador.find_element(By.LINK_TEXT, 'Consulta')
                    consultar.click()
                except:
                    print(f"Erro ao acessar inventário Rotativo!!!\n")
                    try:
                        navegador.quit()
                    except:
                        pass
                    return cancelar_inputs()

                try:
                    file_path = 'Banco de dados.xlsx'
                    file_path = pd.ExcelFile(file_path)
                    file_path.sheet_names

                    sheet_data = file_path.parse('classArmazenagem')
                    qtde = file_path.parse('classArmazenagem')
                    sheet_data.head()
                    qtde.head()
                    itens = sheet_data['Itens']
                    classes = qtde['class']
                except:
                    print(f"Erro  ao acessar o arquivo Banco de dados.xlsx!!!")
                    try:
                        navegador.quit()
                    except:
                        pass
                    return cancelar_inputs()
                
        file_path.close()
        navegador.quit()
    except Exception as e:
        print(f"Erro durante o login ou navegação inicial: {e}")
        cancelar_inputs()
        return