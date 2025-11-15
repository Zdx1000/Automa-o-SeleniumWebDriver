from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import pandas as pd
from utils.shared import historico_funcoes, registrar_progresso
from utils.retornar import cancelar_inputs
from utils.navegador import navegador_google
from time import sleep


def desbloqueio():
    from main import tabela

    historico_funcoes.append(tabela)

    while True:
        print(f'''
╔════════════════════════════════════════════════════════╗
║                 Desbloqueio por itens                  ║
╚════════════════════════════════════════════════════════╝

        [1] Suspenso em vendas
        [2] Saldo
        [3] Negociação
        ''')
        print(f"\n[F8] Para voltar ao menu principal\n")

        try:
            escolha = int(input("Escolha: "))
            if escolha > 0 and escolha < 4:
                break
            else:
                print(f'''Escolha umas da opções existentes!!!''')
                return cancelar_inputs
        except:
            print(f'''Escolha umas da opções existentes!!!''')

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

        # SGEM
        sgem = WebDriverWait(navegador, 20).until(
            lambda driver: driver.find_element(By.LINK_TEXT,
                                               'S.G.E.M').is_displayed() and
                           driver.find_element(By.LINK_TEXT,
                                               'S.G.E.M').is_enabled()
        )
        sgem = navegador.find_element(By.LINK_TEXT, 'S.G.E.M')
        sgem.click()

        # Consultas
        consultas = WebDriverWait(navegador, 20).until(
            lambda driver: driver.find_element(By.LINK_TEXT,
                                               'Consultas').is_displayed() and
                           driver.find_element(By.LINK_TEXT,
                                               'Consultas').is_enabled()
        )
        consultas = navegador.find_element(By.LINK_TEXT, 'Consultas')
        consultas.click()

        # Consultar Itens
        consultar_itens = WebDriverWait(navegador, 20).until(
            lambda driver: driver.find_element(By.LINK_TEXT,
                                               'Consultar Itens').is_displayed() and
                           driver.find_element(By.LINK_TEXT,
                                               'Consultar Itens').is_enabled()
        )
        consultar_itens = navegador.find_element(By.LINK_TEXT,
                                                 'Consultar Itens')
        consultar_itens.click()
    except:
        print(f"Erro ao acessar Consultar por item!!!\n")
        try:
            navegador.quit()
        except:
            pass
        return cancelar_inputs()

    try:
        file_path = 'Banco de dados.xlsx'
        file_path = pd.ExcelFile(file_path)
        file_path.sheet_names

        sheet_data = file_path.parse('Desbloqueio por Item')
        qtde = file_path.parse('Desbloqueio por Item')
        sheet_data.head()
        qtde.head()
        itens1 = sheet_data['Itens']
        quantidades1 = qtde['Qtde']
    except:
        print(f"Erro  ao acessar o arquivo Banco de dados.xlsx!!!")
        try:
            navegador.quit()
        except:
            pass

        return cancelar_inputs()

    for item_, quantidade_ in zip(itens1, quantidades1):
        try:
            while True:
                try:
                    consus = WebDriverWait(navegador, 20).until(
                        lambda driver: driver.find_element(By.CSS_SELECTOR, 'input.k-textbox').is_displayed() and
                                       driver.find_element(By.CSS_SELECTOR, 'input.k-textbox').is_enabled()
                    )
                    consus = navegador.find_element(By.CSS_SELECTOR, 'input.k-textbox')
                    consus.send_keys(item_)
                    break
                except:
                    pass

            # Consultar
            consultar = WebDriverWait(navegador, 20).until(
                lambda driver: driver.find_element(By.LINK_TEXT,
                                                   'Consultar').is_displayed() and
                               driver.find_element(By.LINK_TEXT,
                                                   'Consultar').is_enabled()
            )
            consultar = navegador.find_element(By.LINK_TEXT, 'Consultar')
            consultar.click()

            sleep(1.5)
            desbloquear = WebDriverWait(navegador, 20).until(
                lambda driver: driver.find_element(By.LINK_TEXT,
                                                   'Desbloqueio').is_displayed() and
                               driver.find_element(By.LINK_TEXT,
                                                   'Desbloqueio').is_enabled()
            )
            desbloquear = navegador.find_element(By.LINK_TEXT,
                                                 'Desbloqueio')
            desbloquear.click()

            sleep(1)
            if escolha == 1 or escolha == 2:
                click_desbloq = WebDriverWait(navegador, 20).until(
                    lambda driver: driver.find_element(By.XPATH,
                                                       '/html/body/div[1]/div[2]/div/div/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/div[2]/div[3]/div[1]/hj-flex-container/div/hj-flex-grow/div/div/hj-grid/div[2]/div/div[2]/table/tbody/tr[1]/td[10]/a/hj-label').is_displayed() and
                                   driver.find_element(By.XPATH,
                                                       '/html/body/div[1]/div[2]/div/div/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/div[2]/div[3]/div[1]/hj-flex-container/div/hj-flex-grow/div/div/hj-grid/div[2]/div/div[2]/table/tbody/tr[1]/td[10]/a/hj-label').is_enabled()
                )
                click_desbloq = navegador.find_element(By.XPATH,
                                                       '/html/body/div[1]/div[2]/div/div/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/div[2]/div[3]/div[1]/hj-flex-container/div/hj-flex-grow/div/div/hj-grid/div[2]/div/div[2]/table/tbody/tr[1]/td[10]/a/hj-label')
                click_desbloq.click()

                # Quantidade a bloquear
                qtd_bloq = WebDriverWait(navegador, 20).until(
                    lambda driver: driver.find_element(By.XPATH,
                                                       '/html/body/div[1]/div[2]/div/div/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/div[2]/div[4]/div[1]/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/hj-template/div/hj-field-table/div/hj-field-table-row[2]/div/hj-field-group/div/div[2]/hj-field-group-row[2]/div/hj-field-cell/div/hj-field-control/div/div/span[1]/hj-template/div/hj-textbox/input').is_displayed() and
                                   driver.find_element(By.XPATH,
                                                       '/html/body/div[1]/div[2]/div/div/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/div[2]/div[4]/div[1]/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/hj-template/div/hj-field-table/div/hj-field-table-row[2]/div/hj-field-group/div/div[2]/hj-field-group-row[2]/div/hj-field-cell/div/hj-field-control/div/div/span[1]/hj-template/div/hj-textbox/input').is_enabled()
                )
                qtd_bloq = navegador.find_element(By.XPATH,
                                                  '/html/body/div[1]/div[2]/div/div/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/div[2]/div[4]/div[1]/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/hj-template/div/hj-field-table/div/hj-field-table-row[2]/div/hj-field-group/div/div[2]/hj-field-group-row[2]/div/hj-field-cell/div/hj-field-control/div/div/span[1]/hj-template/div/hj-textbox/input')
                qtd_bloq.send_keys(quantidade_)

                motivos = WebDriverWait(navegador, 20).until(
                    lambda driver: driver.find_element(By.XPATH,
                                                       '/html/body/div[1]/div[2]/div/div/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/div[2]/div[4]/div[1]/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/hj-template/div/hj-field-table/div/hj-field-table-row[2]/div/hj-field-group/div/div[2]/hj-field-group-row[3]/div/hj-field-cell/div/hj-field-control/div/div/span[1]/hj-template/div/hj-dropdownlist/span').is_displayed() and
                                   driver.find_element(By.XPATH,
                                                       '/html/body/div[1]/div[2]/div/div/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/div[2]/div[4]/div[1]/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/hj-template/div/hj-field-table/div/hj-field-table-row[2]/div/hj-field-group/div/div[2]/hj-field-group-row[3]/div/hj-field-cell/div/hj-field-control/div/div/span[1]/hj-template/div/hj-dropdownlist/span').is_enabled()
                )
                motivos = navegador.find_element(By.XPATH,
                                                 '/html/body/div[1]/div[2]/div/div/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/div[2]/div[4]/div[1]/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/hj-template/div/hj-field-table/div/hj-field-table-row[2]/div/hj-field-group/div/div[2]/hj-field-group-row[3]/div/hj-field-cell/div/hj-field-control/div/div/span[1]/hj-template/div/hj-dropdownlist/span')
                motivos.click()
            elif escolha == 3:
                click_desbloq = WebDriverWait(navegador, 20).until(
                    lambda driver: driver.find_element(By.XPATH,
                                                       '/html/body/div[1]/div[2]/div/div/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/div[2]/div[3]/div[1]/hj-flex-container/div/hj-flex-grow/div/div/hj-grid/div[2]/div/div[2]/table/tbody/tr[2]/td[10]/a/hj-label').is_displayed() and
                                   driver.find_element(By.XPATH,
                                                       '/html/body/div[1]/div[2]/div/div/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/div[2]/div[3]/div[1]/hj-flex-container/div/hj-flex-grow/div/div/hj-grid/div[2]/div/div[2]/table/tbody/tr[2]/td[10]/a/hj-label').is_enabled()
                )
                click_desbloq = navegador.find_element(By.XPATH,
                                                       '/html/body/div[1]/div[2]/div/div/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/div[2]/div[3]/div[1]/hj-flex-container/div/hj-flex-grow/div/div/hj-grid/div[2]/div/div[2]/table/tbody/tr[2]/td[10]/a/hj-label')
                click_desbloq.click()

                # Quantidade a bloquear
                qtd_bloq = WebDriverWait(navegador, 20).until(
                    lambda driver: driver.find_element(By.XPATH,
                                                       '/html/body/div[1]/div[2]/div/div/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/div[2]/div[4]/div[1]/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/hj-template/div/hj-field-table/div/hj-field-table-row[2]/div/hj-field-group/div/div[2]/hj-field-group-row[2]/div/hj-field-cell/div/hj-field-control/div/div/span[1]/hj-template/div/hj-textbox/input').is_displayed() and
                                   driver.find_element(By.XPATH,
                                                       '/html/body/div[1]/div[2]/div/div/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/div[2]/div[4]/div[1]/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/hj-template/div/hj-field-table/div/hj-field-table-row[2]/div/hj-field-group/div/div[2]/hj-field-group-row[2]/div/hj-field-cell/div/hj-field-control/div/div/span[1]/hj-template/div/hj-textbox/input').is_enabled()
                )
                qtd_bloq = navegador.find_element(By.XPATH,
                                                  '/html/body/div[1]/div[2]/div/div/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/div[2]/div[4]/div[1]/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/hj-template/div/hj-field-table/div/hj-field-table-row[2]/div/hj-field-group/div/div[2]/hj-field-group-row[2]/div/hj-field-cell/div/hj-field-control/div/div/span[1]/hj-template/div/hj-textbox/input')
                qtd_bloq.send_keys(quantidade_)

                motivos = WebDriverWait(navegador, 20).until(
                    lambda driver: driver.find_element(By.XPATH,
                                                       '/html/body/div[1]/div[2]/div/div/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/div[2]/div[4]/div[1]/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/hj-template/div/hj-field-table/div/hj-field-table-row[2]/div/hj-field-group/div/div[2]/hj-field-group-row[3]/div/hj-field-cell/div/hj-field-control/div/div/span[1]/hj-template/div/hj-dropdownlist/span').is_displayed() and
                                   driver.find_element(By.XPATH,
                                                       '/html/body/div[1]/div[2]/div/div/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/div[2]/div[4]/div[1]/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/hj-template/div/hj-field-table/div/hj-field-table-row[2]/div/hj-field-group/div/div[2]/hj-field-group-row[3]/div/hj-field-cell/div/hj-field-control/div/div/span[1]/hj-template/div/hj-dropdownlist/span').is_enabled()
                )
                motivos = navegador.find_element(By.XPATH,
                                                 '/html/body/div[1]/div[2]/div/div/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/div[2]/div[4]/div[1]/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/hj-template/div/hj-field-table/div/hj-field-table-row[2]/div/hj-field-group/div/div[2]/hj-field-group-row[3]/div/hj-field-cell/div/hj-field-control/div/div/span[1]/hj-template/div/hj-dropdownlist/span')
                motivos.click()
                

            if escolha == 1:
                esc = navegador.find_elements(By.CSS_SELECTOR,
                                              'li.k-item')
                for x in esc:
                    if "01 - Merc.Perdida" == x.text:
                        x.click()
                        break
            elif escolha == 2:
                esc = navegador.find_elements(By.CSS_SELECTOR,
                                              'li.k-item')
                for x in esc:
                    if "101 - SALDO" == x.text:
                        x.click()
                        break
            elif escolha == 3:
                esc = navegador.find_elements(By.CSS_SELECTOR,
                                              'li.k-item')
                for x in esc:
                    if "99 - Dep. Negociacao" == x.text:
                        x.click()
                        break

            if escolha == 1:
                print(
                    f"Item:[{item_}] Qtde:[{quantidade_}] Desbloqueado com sucesso!! [Suspenso em vendas]")

                registrar_progresso(text=f"Desbloqueio realizado com sucesso no Suspenso em vendas: {item_} -> Qtde: ", endereco=quantidade_, sucesso=True)
            elif escolha == 2:
                print(
                    f"Item:[{item_}] Qtde:[{quantidade_}] Desbloqueado com sucesso!! [Suspenso em Saldo]")
                registrar_progresso(text=f"Desbloqueio realizado com sucesso no Suspenso em Saldo: {item_} -> Qtde: ", endereco=quantidade_, sucesso=True)
            elif escolha == 3:
                print(
                    f"Item:[{item_}] Qtde:[{quantidade_}] Desbloqueado com sucesso!! [Suspenso em Negociação]")
                registrar_progresso(text=f"Desbloqueio realizado com sucesso no Suspenso em Negociação: {item_} -> Qtde: ", endereco=quantidade_, sucesso=True)

            feito = navegador.find_element(
                By.LINK_TEXT,
                'Desbloquear'
            )
            sleep(1)
            feito.click()

            sleep(1)

            ok4 = WebDriverWait(navegador, 20).until(
                lambda driver: driver.find_element(By.CLASS_NAME, 'hj-dlg-button').is_displayed() and
                               driver.find_element(By.CLASS_NAME, 'hj-dlg-button').is_enabled()
            )
            ok4 = navegador.find_element(By.CLASS_NAME, 'hj-dlg-button')
            ok4.click()
            
        except:
            if escolha == 1:
                print(
                    f"Item:[{item_}] Qtde:[{quantidade_}] Erro ao Desbloqueado com sucesso!! [Suspenso em vendas]")
                registrar_progresso(
                    text=f"Erro ao Desbloqueio no Suspenso em vendas: {item_} -> Qtde: ",
                    endereco=quantidade_, sucesso=False)
            elif escolha == 2:
                print(
                    f"Item:[{item_}] Qtde:[{quantidade_}] Erro ao Desbloqueado com sucesso!! [Suspenso em Saldo]")
                registrar_progresso(
                    text=f"Erro ao Desbloqueio no Suspenso em Saldo: {item_} -> Qtde: ",
                    endereco=quantidade_, sucesso=False)
            elif escolha == 3:
                print(
                    f"Item:[{item_}] Qtde:[{quantidade_}] Erro ao Desbloqueado com sucesso!! [Suspenso em Negociação]")
                registrar_progresso(
                    text=f"Erro ao Desbloqueio no Suspenso em Negociação: {item_} -> Qtde: ",
                    endereco=quantidade_, sucesso=False)

            file_path.close()
            navegador.quit()
            sleep(2)

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

                # SGEM
                sgem = WebDriverWait(navegador, 20).until(
                    lambda driver: driver.find_element(By.LINK_TEXT,
                                                       'S.G.E.M').is_displayed() and
                                   driver.find_element(By.LINK_TEXT,
                                                       'S.G.E.M').is_enabled()
                )
                sgem = navegador.find_element(By.LINK_TEXT, 'S.G.E.M')
                sgem.click()

                # Consultas
                consultas = WebDriverWait(navegador, 20).until(
                    lambda driver: driver.find_element(By.LINK_TEXT,
                                                       'Consultas').is_displayed() and
                                   driver.find_element(By.LINK_TEXT,
                                                       'Consultas').is_enabled()
                )
                consultas = navegador.find_element(By.LINK_TEXT, 'Consultas')
                consultas.click()

                # Consultar Itens
                consultar_itens = WebDriverWait(navegador, 20).until(
                    lambda driver: driver.find_element(By.LINK_TEXT,
                                                       'Consultar Itens').is_displayed() and
                                   driver.find_element(By.LINK_TEXT,
                                                       'Consultar Itens').is_enabled()
                )
                consultar_itens = navegador.find_element(By.LINK_TEXT,
                                                         'Consultar Itens')
                consultar_itens.click()
            except:
                print(f"Erro ao acessar Consultar por item!!!\n")
                try:
                    navegador.quit()
                except:
                    pass
                return cancelar_inputs()

            try:
                file_path = 'Banco de dados.xlsx'
                file_path = pd.ExcelFile(file_path)
                file_path.sheet_names

                sheet_data = file_path.parse('Desbloqueio por Item')
                qtde = file_path.parse('Desbloqueio por Item')
                sheet_data.head()
                qtde.head()
                itens1 = sheet_data['Itens']
                quantidades1 = qtde['Qtde']

            except:
                print(f"Erro  ao acessar o arquivo Banco de dados.xlsx!!!")
                try:
                    navegador.quit()
                except:
                    pass

                return cancelar_inputs()
    file_path.close()
    navegador.quit()
    cancelar_inputs()
