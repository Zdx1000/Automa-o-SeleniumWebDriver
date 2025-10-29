from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import pandas as pd
from utils.shared import historico_funcoes, registrar_progresso
from utils.retornar import cancelar_inputs
from utils.navegador import navegador_google
from time import sleep


def Verificacao():
    from main import tabela

    historico_funcoes.append(tabela)

    print(f'''
    ╔════════════════════════════════════════════════════════╗
    ║           Contagem Verificação Fila de prioridade          ║
    ╚════════════════════════════════════════════════════════╝


    [1] 10 - Normal
    [2] 20 - Normal
    [3] 30 - Normal
    [4] 50 - Prioridade
    [5] 60 - Prioridade
    [6] 70 - Prioridade
    [7] 80 - Prioridade
    [8] 90 - Prioridade
    ''')
    print(f"\n[F8] Para voltar ao menu principal\n")
    try:
        while True:
            prioridade_select = int(input("Escolha uma opção: "))
            if prioridade_select > 0 and prioridade_select < 9:
                break
            else:
                print(f"Seleciona uma das opções!!")

    except Exception:
        print(f"Seleciona uma das opções!!")
        return cancelar_inputs
    try:
        navegador = navegador_google()
    except:
        try:
            navegador.quit()
        except:
            pass
        return cancelar_inputs()
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

        advantage = WebDriverWait(navegador, 20).until(
            lambda driver: driver.find_element(By.LINK_TEXT, 'Advantage Dashboard').is_displayed() and
                           driver.find_element(By.LINK_TEXT, 'Advantage Dashboard').is_enabled()
        )
        advantage = navegador.find_element(By.LINK_TEXT, 'Advantage Dashboard')
        advantage.click()

        inventario = WebDriverWait(navegador, 20).until(
            lambda driver: driver.find_element(By.LINK_TEXT, 'Inventário Rotativo').is_displayed() and
                           driver.find_element(By.LINK_TEXT, 'Inventário Rotativo').is_enabled()
        )
        inventario = navegador.find_element(By.LINK_TEXT, 'Inventário Rotativo')
        inventario.click()

        verificacao = WebDriverWait(navegador, 20).until(
            lambda driver: driver.find_element(By.LINK_TEXT, 'Geração Verificação').is_displayed() and
                           driver.find_element(By.LINK_TEXT, 'Geração Verificação').is_enabled()
        )
        verificacao = navegador.find_element(By.LINK_TEXT, 'Geração Verificação')
        verificacao.click()

        por_item = WebDriverWait(navegador, 20).until(
            lambda driver: driver.find_element(By.LINK_TEXT, 'Por Item').is_displayed() and
                           driver.find_element(By.LINK_TEXT, 'Por Item').is_enabled()
        )
        por_item = navegador.find_element(By.LINK_TEXT, 'Por Item')
        por_item.click()
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

        sheet_data = file_path.parse('Gerar Verificação')
        sheet_data.head()
        itens_verificacao = sheet_data['Itens']
    except:
        print(f"Erro  ao acessar o arquivo Banco de dados.xlsx!!!")
        try:
            navegador.quit()
        except:
            pass
        return cancelar_inputs()

    for item_verificacao in itens_verificacao:
        try:
            item_dg = WebDriverWait(navegador, 20).until(
                lambda driver: driver.find_element(By.CSS_SELECTOR, "input.k-textbox").is_displayed() and
                               driver.find_element(By.CSS_SELECTOR, "input.k-textbox").is_enabled()
            )
            item_dg = navegador.find_element(By.CSS_SELECTOR, "input.k-textbox")
            item_dg.clear()
            item_dg.send_keys(item_verificacao)

            gerar_verificacao = WebDriverWait(navegador, 20).until(
                lambda driver: driver.find_element(By.LINK_TEXT, 'Gerar').is_displayed() and
                               driver.find_element(By.LINK_TEXT, 'Gerar').is_enabled()
            )
            gerar_verificacao = navegador.find_element(By.LINK_TEXT, 'Gerar')
            gerar_verificacao.click()

            clak_1 = WebDriverWait(navegador, 20).until(
                lambda driver: driver.find_element(By.CSS_SELECTOR, 'a.hj-link').is_displayed() and
                                driver.find_element(By.CSS_SELECTOR, 'a.hj-link').is_enabled()
            )
            clak_1 = navegador.find_element(By.CSS_SELECTOR, 'a.hj-link')
            clak_1.click()

            prioridade = WebDriverWait(navegador, 20).until(
                lambda driver: driver.find_element(By.XPATH,
                                                   '/html/body/div[1]/div[2]/div/div/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/div[2]/div[3]/div[1]/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/hj-template/div/hj-field-table/div/hj-field-table-row[2]/div/hj-field-group/div/div[2]/hj-field-group-row[3]/div/hj-field-cell/div/hj-field-control/div/div/span[1]/hj-template/div/hj-dropdownlist/span').is_displayed() and
                               driver.find_element(By.XPATH,
                                                   '/html/body/div[1]/div[2]/div/div/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/div[2]/div[3]/div[1]/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/hj-template/div/hj-field-table/div/hj-field-table-row[2]/div/hj-field-group/div/div[2]/hj-field-group-row[3]/div/hj-field-cell/div/hj-field-control/div/div/span[1]/hj-template/div/hj-dropdownlist/span').is_enabled()
            )
            prioridade = navegador.find_element(By.XPATH,
                                                '/html/body/div[1]/div[2]/div/div/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/div[2]/div[3]/div[1]/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/hj-template/div/hj-field-table/div/hj-field-table-row[2]/div/hj-field-group/div/div[2]/hj-field-group-row[3]/div/hj-field-cell/div/hj-field-control/div/div/span[1]/hj-template/div/hj-dropdownlist/span')
            prioridade.click()

            lista_suspensa = navegador.find_element(By.CSS_SELECTOR, "div.k-list-container")

            navegador.execute_script("arguments[0].click();", lista_suspensa)

            if prioridade_select == 1:
                opcao = navegador.find_element(By.XPATH, "//li[text()='10 - Normal']")
                navegador.execute_script("arguments[0].click();", opcao)
            elif prioridade_select == 2:
                opcao = navegador.find_element(By.XPATH, "//li[text()='20 - Normal']")
                navegador.execute_script("arguments[0].click();", opcao)
            elif prioridade_select == 3:
                opcao = navegador.find_element(By.XPATH, "//li[text()='30 - Normal']")
                navegador.execute_script("arguments[0].click();", opcao)
            elif prioridade_select == 4:
                opcao = navegador.find_element(By.XPATH, "//li[text()='50 - Prioridade']")
                navegador.execute_script("arguments[0].click();", opcao)
            elif prioridade_select == 5:
                opcao = navegador.find_element(By.XPATH, "//li[text()='60 - Prioridade']")
                navegador.execute_script("arguments[0].click();", opcao)
            elif prioridade_select == 6:
                opcao = navegador.find_element(By.XPATH, "//li[text()='70 - Prioridade']")
                navegador.execute_script("arguments[0].click();", opcao)
            elif prioridade_select == 7:
                opcao = navegador.find_element(By.XPATH, "//li[text()='80 - Prioridade']")
                navegador.execute_script("arguments[0].click();", opcao)
            elif prioridade_select == 8:
                opcao = navegador.find_element(By.XPATH, "//li[text()='90 - Prioridade']")
                navegador.execute_script("arguments[0].click();", opcao)

            alterar = WebDriverWait(navegador, 20).until(
                lambda driver: driver.find_element(By.LINK_TEXT, 'Alterar').is_displayed() and
                                driver.find_element(By.LINK_TEXT, 'Alterar').is_enabled()
            )
            alterar = navegador.find_element(By.LINK_TEXT, 'Alterar')
            alterar.click()
            sleep(1)

            voltar2_ = WebDriverWait(navegador, 20).until(
                lambda driver: driver.find_element(By.CSS_SELECTOR, "a[data-hj-test-id='active-thread-previous-button']").is_displayed() and
                               driver.find_element(By.CSS_SELECTOR, "a[data-hj-test-id='active-thread-previous-button']").is_enabled()
            )
            voltar2_ = navegador.find_element(By.CSS_SELECTOR, "a[data-hj-test-id='active-thread-previous-button']")

            for Quantidade_voltar in range(1, 4):
                sleep(1)
                voltar2_.click()

            cont += 1
            porcentagem = (cont / len(itens_verificacao)) * 100
            print(f"Verificação gerada com sucesso: {cont}/{len(itens_verificacao)} ({porcentagem:.1f}%) - {item_verificacao}")
            
            sleep(1)
            registrar_progresso(text="Verificação gerada com sucesso: ", endereco=item_verificacao, sucesso=True)
        except:
            cont += 1
            porcentagem = (cont / len(itens_verificacao)) * 100
            print(f"Erro ao gerar verificação: {cont}/{len(itens_verificacao)} ({porcentagem:.1f}%) - {item_verificacao}")
            
            registrar_progresso(text="Verificação não gerado: ", endereco=item_verificacao, sucesso=False)

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

                advantage = WebDriverWait(navegador, 20).until(
                    lambda driver: driver.find_element(By.LINK_TEXT, 'Advantage Dashboard').is_displayed() and
                                   driver.find_element(By.LINK_TEXT, 'Advantage Dashboard').is_enabled()
                )
                advantage = navegador.find_element(By.LINK_TEXT, 'Advantage Dashboard')
                advantage.click()

                inventario = WebDriverWait(navegador, 20).until(
                    lambda driver: driver.find_element(By.LINK_TEXT, 'Inventário Rotativo').is_displayed() and
                                   driver.find_element(By.LINK_TEXT, 'Inventário Rotativo').is_enabled()
                )
                inventario = navegador.find_element(By.LINK_TEXT, 'Inventário Rotativo')
                inventario.click()

                verificacao = WebDriverWait(navegador, 20).until(
                    lambda driver: driver.find_element(By.LINK_TEXT, 'Geração Verificação').is_displayed() and
                                   driver.find_element(By.LINK_TEXT, 'Geração Verificação').is_enabled()
                )
                verificacao = navegador.find_element(By.LINK_TEXT, 'Geração Verificação')
                verificacao.click()

                por_item = WebDriverWait(navegador, 20).until(
                    lambda driver: driver.find_element(By.LINK_TEXT, 'Por Item').is_displayed() and
                                   driver.find_element(By.LINK_TEXT, 'Por Item').is_enabled()
                )
                por_item = navegador.find_element(By.LINK_TEXT, 'Por Item')
                por_item.click()
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

                sheet_data = file_path.parse('Gerar Verificação')
                sheet_data.head()
                itens_verificacao = sheet_data['Itens']
            except:
                print(f"Erro  ao acessar o arquivo Banco de dados.xlsx!!!")
                try:
                    navegador.quit()
                except:
                    pass
                return cancelar_inputs()

    file_path.close()
    navegador.quit()