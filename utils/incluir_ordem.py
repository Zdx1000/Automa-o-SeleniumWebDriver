from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import pandas as pd
from utils.retornar import cancelar_inputs
from utils.navegador import navegador_google
from time import sleep


def incluir_item_ordem():
    print(f'''
    ╔════════════════════════════════════════════════════════╗
    ║                 Incluir item na ordem                  ║
    ╚════════════════════════════════════════════════════════╝
    ''')

    print(f'''
          Index dos armazéns:
          ------------------------------------------
          1 - [01001] Uberlândia - CADUDI
          2 - [01604] Martins distribuidora
          ''')
    try:
        armazem = int(input("Digite o código do armazém: ").strip())
        if armazem != 1 and armazem != 2:
            print("Código de armazém inválido. Tente novamente.")
            return cancelar_inputs()
    except ValueError:
        print("Entrada inválida. Digite um número para o código do armazém.")
        return cancelar_inputs()

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

        sheet_data = file_path.parse('Incluir Item da Ordem')
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

                if armazem == 2:

                    armazem = WebDriverWait(navegador, 20).until(
                        lambda driver: driver.find_element(By.CLASS_NAME, 'k-input').is_displayed() and
                                    driver.find_element(By.CLASS_NAME, 'k-input').is_enabled()
                    )

                    

                    armazem = navegador.find_element(By.CLASS_NAME, 'k-input')
                    armazem.click()

                    sleep(1)

                    armazem_list = navegador.find_elements(By.CSS_SELECTOR, 'li.k-item')
                    for armazem_option in armazem_list:
                        if 'MARTINS DISTRIBUIDOR' == armazem_option.text:
                            armazem_option.click()
                            break

                consultar = WebDriverWait(navegador, 20).until(
                    lambda driver: driver.find_element(By.LINK_TEXT, 'Consulta').is_displayed() and
                                driver.find_element(By.LINK_TEXT, 'Consulta').is_enabled()
                )
                consultar = navegador.find_element(By.LINK_TEXT, 'Consulta')
                consultar.click()

                sleep(2) # Preciso deixar automatico

                UOM = navegador.find_elements(By.TAG_NAME, 'hj-label')

                for UOM_option in UOM:
                    if "UOM" in UOM_option.text:
                        UOM_option.click()
                        break

                sleep(1)

                headers = navegador.find_elements(By.CSS_SELECTOR, 'th.k-header')
                uom_index = None
                for header in headers:
                    if "UOM" in header.text:
                        uom_index = header.get_attribute('data-index')
                        break
                

                valor_coluna_hash = 0
                rows = navegador.find_elements(By.CSS_SELECTOR, 'tr[data-uid]')
                for row in rows:
                    cells = row.find_elements(By.TAG_NAME, 'td')
                    if len(cells) > 7 and cells[7].text == "EE":
                        valor_coluna_hash = cells[0].text
                        break

                valor_UOM = navegador.find_elements(By.CSS_SELECTOR, "a.hj-link")

                for index_OUM in valor_UOM:
                    if valor_coluna_hash == index_OUM.text:
                        index_OUM.click()
                        break
                
                sleep(2)
                norma_rc = navegador.find_elements(By.CLASS_NAME, "k-input")
                norma_rc[6].click()

                option_list_norma = navegador.find_elements(By.CSS_SELECTOR, 'li.k-item')
                for option in option_list_norma:
                    if "Sim" in option.text:
                        option.click()
                        break
                
                sleep(2)

                alterar = WebDriverWait(navegador, 20).until(
                    lambda driver: driver.find_element(By.LINK_TEXT, 'Alterar').is_displayed() and
                                driver.find_element(By.LINK_TEXT, 'Alterar').is_enabled()
                )
                alterar = navegador.find_element(By.LINK_TEXT, 'Alterar')
                alterar.click()

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
