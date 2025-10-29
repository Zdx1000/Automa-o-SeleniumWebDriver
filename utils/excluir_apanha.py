from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import pandas as pd
from utils.retornar import cancelar_inputs
from utils.navegador import navegador_google
from time import sleep


def excluir_apanha():
    print(f'''
    ╔════════════════════════════════════════════════════════╗
    ║                   Excluir apanha vazia                 ║
    ╚════════════════════════════════════════════════════════╝
    ''')

    input(f"Precione Enter para continuar...")

    try:
        navegador = navegador_google()
    except:
        try:
            navegador.quit()
        except:
            pass
        return cancelar_inputs()

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

    wa = WebDriverWait(navegador, 20).until(
        lambda driver: driver.find_element(By.LINK_TEXT, 'Warehouse Advantage').is_displayed() and
                       driver.find_element(By.LINK_TEXT, 'Warehouse Advantage').is_enabled()
    )
    wa = navegador.find_element(By.LINK_TEXT, 'Warehouse Advantage')
    wa.click()

    config = WebDriverWait(navegador, 20).until(
        lambda driver: driver.find_element(By.LINK_TEXT, 'Configuração Armazém').is_displayed() and
                       driver.find_element(By.LINK_TEXT, 'Configuração Armazém').is_enabled()
    )
    config = navegador.find_element(By.LINK_TEXT, 'Configuração Armazém')
    config.click()

    config_itens = WebDriverWait(navegador, 20).until(
        lambda driver: driver.find_element(By.LINK_TEXT, 'Itens').is_displayed() and
                       driver.find_element(By.LINK_TEXT, 'Itens').is_enabled()
    )
    config_itens = navegador.find_element(By.LINK_TEXT, 'Itens')
    config_itens.click()

    itens = WebDriverWait(navegador, 20).until(
        lambda driver: driver.find_element(By.LINK_TEXT, 'Itens').is_displayed() and
                       driver.find_element(By.LINK_TEXT, 'Itens').is_enabled()
    )
    itens = navegador.find_elements(By.LINK_TEXT, 'Itens')
    itens[1].click()

    cont = 0
    try:
        file_path = 'Banco de dados.xlsx'
        file_path = pd.ExcelFile(file_path)
        file_path.sheet_names

        sheet_data = file_path.parse('Exluir Endereço')
        sheet_data.head()
        itens_apanha = sheet_data['Itens']
    except:
        print(f"Erro  ao acessar o arquivo Banco de dados.xlsx!!!")
        try:
            navegador.quit()
        except:
            pass
        return cancelar_inputs()

    try:

        for Item in itens_apanha:

            try:
                item_consulta = WebDriverWait(navegador, 20).until(
                    lambda driver: driver.find_element(By.CSS_SELECTOR, 'input.k-textbox').is_displayed() and
                                driver.find_element(By.CSS_SELECTOR, 'input.k-textbox').is_enabled()
                )
                item_consulta = navegador.find_element(By.CSS_SELECTOR, 'input.k-textbox')
                item_consulta.clear()
                item_consulta.send_keys(Item)

                consultar = WebDriverWait(navegador, 20).until(
                    lambda driver: driver.find_element(By.LINK_TEXT, 'Consulta').is_displayed() and
                                driver.find_element(By.LINK_TEXT, 'Consulta').is_enabled()
                )
                consultar = navegador.find_element(By.LINK_TEXT, 'Consulta')
                consultar.click()

                endsep = WebDriverWait(navegador, 20).until(
                    lambda driver: driver.find_element(By.LINK_TEXT, 'End. Sep.').is_displayed() and
                                driver.find_element(By.LINK_TEXT, 'End. Sep.').is_enabled()
                )
                endsep = navegador.find_element(By.LINK_TEXT, 'End. Sep.')
                endsep.click()

                while True:
                    try:
                        excluir = WebDriverWait(navegador, 1).until(
                            lambda driver: driver.find_element(By.LINK_TEXT, 'Excluir').is_displayed() and
                                        driver.find_element(By.LINK_TEXT, 'Excluir').is_enabled()
                        )
                        excluir = navegador.find_elements(By.LINK_TEXT, 'Excluir')
                        
                        confirmacao = None
                        for exclui in excluir:
                            try:
                                confirmacao = WebDriverWait(navegador, 1).until(
                                    lambda driver: driver.find_element(By.CSS_SELECTOR, 'button.k-button')
                                    if driver.find_element(By.CSS_SELECTOR, 'button.k-button').is_displayed() and
                                    driver.find_element(By.CSS_SELECTOR, 'button.k-button').is_enabled()
                                    else False
                                )
                                confirmacao.click()
                                break
                            except:
                                pass

                            exclui.click()
                            sleep(1)
                            
                        if len(excluir) == 1 or confirmacao:
                            break
                    except:
                        sleep(0.3)
                cont += 1
                porcentagem = (cont / len(itens_apanha)) * 100
                print(f"Item {cont}/{len(itens_apanha)} ({porcentagem:.1f}%) - {Item}")
                try:
                    voltar2_ = WebDriverWait(navegador, 20).until(
                        lambda driver: driver.find_element(By.CSS_SELECTOR,
                                                        "a[data-hj-test-id='active-thread-previous-button']").is_displayed() and
                                    driver.find_element(By.CSS_SELECTOR,
                                                        "a[data-hj-test-id='active-thread-previous-button']").is_enabled()
                    )
                    voltar2_ = navegador.find_element(By.CSS_SELECTOR, "a[data-hj-test-id='active-thread-previous-button']")

                    for Quantidade_voltar in range(1, 3):
                        sleep(1)
                        voltar2_.click()
                except:
                    pass
            except:

                cont += 1

                porcentagem = (cont / len(itens_apanha)) * 100
                print(f"Confirmado com Erro: {cont}/{len(itens_apanha)} ({porcentagem:.1f}%) - {Item}")
                file_path.close()
                navegador.quit()

                try:
                    navegador = navegador_google()
                except:
                    try:
                        navegador.quit()
                    except:
                        pass
                    return cancelar_inputs()

                try:
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

                    wa = WebDriverWait(navegador, 20).until(
                        lambda driver: driver.find_element(By.LINK_TEXT, 'Warehouse Advantage').is_displayed() and
                                    driver.find_element(By.LINK_TEXT, 'Warehouse Advantage').is_enabled()
                    )
                    wa = navegador.find_element(By.LINK_TEXT, 'Warehouse Advantage')
                    wa.click()

                    config = WebDriverWait(navegador, 20).until(
                        lambda driver: driver.find_element(By.LINK_TEXT, 'Configuração Armazém').is_displayed() and
                                    driver.find_element(By.LINK_TEXT, 'Configuração Armazém').is_enabled()
                    )
                    config = navegador.find_element(By.LINK_TEXT, 'Configuração Armazém')
                    config.click()

                    config_itens = WebDriverWait(navegador, 20).until(
                        lambda driver: driver.find_element(By.LINK_TEXT, 'Itens').is_displayed() and
                                    driver.find_element(By.LINK_TEXT, 'Itens').is_enabled()
                    )
                    config_itens = navegador.find_element(By.LINK_TEXT, 'Itens')
                    config_itens.click()

                    itens = WebDriverWait(navegador, 20).until(
                        lambda driver: driver.find_element(By.LINK_TEXT, 'Itens').is_displayed() and
                                    driver.find_element(By.LINK_TEXT, 'Itens').is_enabled()
                    )
                    itens = navegador.find_elements(By.LINK_TEXT, 'Itens')
                    itens[1].click()

                except:
                    print(f"Erro ao acessar Fechamento de pedido de ajuste!!!\n")
                    try:
                        navegador.quit()
                    except:
                        pass
                    return cancelar_inputs()
                    
    except:
        file_path.close()
        navegador.quit()
        cancelar_inputs()
    file_path.close()
    navegador.quit()
    cancelar_inputs()
