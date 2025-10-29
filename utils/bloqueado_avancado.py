from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import pandas as pd
from utils.shared import historico_funcoes, registrar_progresso
from utils.retornar import cancelar_inputs
from utils.navegador import navegador_google
from time import sleep



def Bloqueado_avancado():
    from main import tabela

    historico_funcoes.append(tabela)

    print(f'''
╔════════════════════════════════════════════════════════╗
║                 Tratativa do Bloqueado                 ║
╚════════════════════════════════════════════════════════╝
''')

    print(
                              f'''╔════════════════════════════════════════════════════════════════════════════╗\n║''')
    print(f'''                  Muito CUIDADO ao ultilizar esta função!                   ║     \n║                                                                            ║''',0.8)
    print(f'''║      Certifique-se que todos os dados estão corretos antes de proceguir    ║    ''',0.8)
    print(f'''║               Analíse todos os itens novamente, se possível!               ║    ''',0.8)
    print(f'''║ Em caso de Erro as consequência  serão e ampla escala a depender dos dados ║    \n║                                          ══════════════════════════════════║''',0.8)
    print(f'''║                                         ║ Apenas colaboradores AUTORIZADOS ║    ''',0.8)
    print(f'''╚════════════════════════════════════════════════════════════════════════════╝''')

    print(f"\n[F8] Para voltar ao menu principal\n")

    print(f"\nPrecione enter para continuar....\n")
    input("")

    navegador = navegador_google()

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

        sheet_data = file_path.parse('Tratativa do Bloqueado avançado')
        Estoque = file_path.parse('Tratativa do Bloqueado avançado')
        Negociacao = file_path.parse('Tratativa do Bloqueado avançado')
        Saldo = file_path.parse('Tratativa do Bloqueado avançado')
        sheet_data.head()
        Estoque.head()
        Negociacao.head()
        Saldo.head()
        itens1 = sheet_data['Itens']
        Estoque1 = Estoque['Estoque']
        Negociacao1 = Negociacao['Negociação']
        Saldo1 = Saldo['Saldo']
    except:
        print(f"Erro  ao acessar o arquivo Banco de dados.xlsx!!!")
        try:
            navegador.quit()
        except:
            pass

        return cancelar_inputs()


    for item_, Estoque_, Negociacao_, Saldo_ in zip(itens1, Estoque1, Negociacao1, Saldo1):
        try:
            while True:
                try:
                    consus = WebDriverWait(navegador, 20).until(
                        lambda driver: driver.find_element(By.CSS_SELECTOR, 'input.k-textbox').is_displayed() and
                                       driver.find_element(By.CSS_SELECTOR, 'input.k-textbox').is_enabled()
                    )
                    consus = navegador.find_element(By.CSS_SELECTOR, 'input.k-textbox')
                    consus.clear()
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

            if Estoque_ == 0:
                Nome_estoque = "Sem modificacação"

            elif Estoque_ > 0:
                Nome_estoque = f"Bloqueado com sucesso!!"
                sleep(0.3)

                bloquear = WebDriverWait(navegador, 20).until(
                    lambda driver: driver.find_element(By.LINK_TEXT,
                                                       'Bloqueio').is_displayed() and
                                   driver.find_element(By.LINK_TEXT,
                                                       'Bloqueio').is_enabled()
                )
                bloquear = navegador.find_element(By.LINK_TEXT,
                                                  'Bloqueio')
                bloquear.click()

                estoque_cont = WebDriverWait(navegador, 20).until(
                    lambda driver: driver.find_element(By.XPATH,
                                                       '/html/body/div[1]/div[2]/div/div/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/div[2]/div[3]/div[1]/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/hj-template/div/hj-field-table/div/hj-field-table-row[1]/div/hj-field-group/div/div/hj-field-group-row[1]/div/hj-field-cell[1]/div/hj-field-control/div/div/span[1]/hj-template/div/hj-textbox/input').is_displayed() and
                                   driver.find_element(By.XPATH,
                                                       '/html/body/div[1]/div[2]/div/div/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/div[2]/div[3]/div[1]/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/hj-template/div/hj-field-table/div/hj-field-table-row[1]/div/hj-field-group/div/div/hj-field-group-row[1]/div/hj-field-cell[1]/div/hj-field-control/div/div/span[1]/hj-template/div/hj-textbox/input').is_enabled()
                )
                estoque_cont = navegador.find_element(By.XPATH,
                                                      '/html/body/div[1]/div[2]/div/div/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/div[2]/div[3]/div[1]/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/hj-template/div/hj-field-table/div/hj-field-table-row[1]/div/hj-field-group/div/div/hj-field-group-row[1]/div/hj-field-cell[1]/div/hj-field-control/div/div/span[1]/hj-template/div/hj-textbox/input')
                estoque_cont.send_keys("99999")
                sleep(0.3)

                qtde_bloq = WebDriverWait(navegador, 20).until(
                    lambda driver: driver.find_element(By.XPATH,
                                                       '/html/body/div[1]/div[2]/div/div/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/div[2]/div[3]/div[1]/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/hj-template/div/hj-field-table/div/hj-field-table-row[2]/div/hj-field-group/div/div[2]/hj-field-group-row[1]/div/hj-field-cell/div/hj-field-control/div/div/span[1]/hj-template/div/hj-textbox/input').is_displayed() and
                                   driver.find_element(By.XPATH,
                                                       '/html/body/div[1]/div[2]/div/div/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/div[2]/div[3]/div[1]/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/hj-template/div/hj-field-table/div/hj-field-table-row[2]/div/hj-field-group/div/div[2]/hj-field-group-row[1]/div/hj-field-cell/div/hj-field-control/div/div/span[1]/hj-template/div/hj-textbox/input').is_enabled()
                )
                qtde_bloq = navegador.find_element(By.XPATH,
                                                   '/html/body/div[1]/div[2]/div/div/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/div[2]/div[3]/div[1]/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/hj-template/div/hj-field-table/div/hj-field-table-row[2]/div/hj-field-group/div/div[2]/hj-field-group-row[1]/div/hj-field-cell/div/hj-field-control/div/div/span[1]/hj-template/div/hj-textbox/input')
                qtde_bloq.clear()
                qtde_bloq.send_keys(f"{Estoque_}")

                motivos = WebDriverWait(navegador, 20).until(
                    lambda driver: driver.find_element(By.XPATH,
                                                       '/html/body/div[1]/div[2]/div/div/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/div[2]/div[3]/div[1]/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/hj-template/div/hj-field-table/div/hj-field-table-row[2]/div/hj-field-group/div/div[2]/hj-field-group-row[3]/div/hj-field-cell/div/hj-field-control/div/div/span[1]/hj-template/div/hj-dropdownlist/span').is_displayed() and
                                   driver.find_element(By.XPATH,
                                                       '/html/body/div[1]/div[2]/div/div/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/div[2]/div[3]/div[1]/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/hj-template/div/hj-field-table/div/hj-field-table-row[2]/div/hj-field-group/div/div[2]/hj-field-group-row[3]/div/hj-field-cell/div/hj-field-control/div/div/span[1]/hj-template/div/hj-dropdownlist/span').is_enabled()
                )
                motivos = navegador.find_element(By.XPATH,
                                                 '/html/body/div[1]/div[2]/div/div/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/div[2]/div[3]/div[1]/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/hj-template/div/hj-field-table/div/hj-field-table-row[2]/div/hj-field-group/div/div[2]/hj-field-group-row[3]/div/hj-field-cell/div/hj-field-control/div/div/span[1]/hj-template/div/hj-dropdownlist/span')
                motivos.click()

                esc = navegador.find_elements(By.CSS_SELECTOR,
                                              'li.k-item')
                for x in esc:
                    if "01 - Merc.Perdida" == x.text:
                        x.click()
                        break


                feito2 = WebDriverWait(navegador, 20).until(
                    lambda driver: driver.find_element(By.LINK_TEXT,
                                                       'Bloquear').is_displayed() and
                                   driver.find_element(By.LINK_TEXT,
                                                       'Bloquear').is_enabled()
                )
                feito2 = navegador.find_element(By.LINK_TEXT,
                                                  'Bloquear')
                feito2.click()
                sleep(0.3)

                ok4 = WebDriverWait(navegador, 20).until(
                    lambda driver: driver.find_element(By.CLASS_NAME, 'hj-dlg-button').is_displayed() and
                                   driver.find_element(By.CLASS_NAME, 'hj-dlg-button').is_enabled()
                )
                ok4 = navegador.find_element(By.CLASS_NAME, 'hj-dlg-button')
                ok4.click()
                sleep(0.3)

                while True:
                    try:
                        consus = WebDriverWait(navegador, 20).until(
                            lambda driver: driver.find_element(By.CSS_SELECTOR,
                                                               'input.k-textbox').is_displayed() and
                                           driver.find_element(By.CSS_SELECTOR, 'input.k-textbox').is_enabled()
                        )
                        consus = navegador.find_element(By.CSS_SELECTOR, 'input.k-textbox')
                        consus.clear()
                        consus.send_keys(item_)
                        break
                    except:
                        pass
                sleep(0.3)

                # Consultar
                consultar = WebDriverWait(navegador, 20).until(
                    lambda driver: driver.find_element(By.LINK_TEXT,
                                                       'Consultar').is_displayed() and
                                   driver.find_element(By.LINK_TEXT,
                                                       'Consultar').is_enabled()
                )
                consultar = navegador.find_element(By.LINK_TEXT, 'Consultar')
                consultar.click()


            elif Estoque_ < 0:
                Nome_estoque = f"Desbloqueado com sucesso!!"
                desbloquear = WebDriverWait(navegador, 20).until(
                    lambda driver: driver.find_element(By.LINK_TEXT,
                                                       'Desbloqueio').is_displayed() and
                                   driver.find_element(By.LINK_TEXT,
                                                       'Desbloqueio').is_enabled()
                )
                desbloquear = navegador.find_element(By.LINK_TEXT,
                                                     'Desbloqueio')
                desbloquear.click()
                sleep(0.3)
                Estoque_ = (Estoque_ * -1)
                click_desbloq = WebDriverWait(navegador, 20).until(
                    lambda driver: driver.find_element(By.XPATH,
                                                       '/html/body/div[1]/div[2]/div/div/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/div[2]/div[3]/div[1]/hj-flex-container/div/hj-flex-grow/div/div/hj-grid/div[2]/div/div[2]/table/tbody/tr[1]/td[10]/a/hj-label').is_displayed() and
                                   driver.find_element(By.XPATH,
                                                       '/html/body/div[1]/div[2]/div/div/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/div[2]/div[3]/div[1]/hj-flex-container/div/hj-flex-grow/div/div/hj-grid/div[2]/div/div[2]/table/tbody/tr[1]/td[10]/a/hj-label').is_enabled()
                )
                click_desbloq = navegador.find_element(By.XPATH,
                                                       '/html/body/div[1]/div[2]/div/div/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/div[2]/div[3]/div[1]/hj-flex-container/div/hj-flex-grow/div/div/hj-grid/div[2]/div/div[2]/table/tbody/tr[1]/td[10]/a/hj-label')
                click_desbloq.click()
                sleep(0.3)

                # Quantidade a bloquear
                qtd_bloq = WebDriverWait(navegador, 20).until(
                    lambda driver: driver.find_element(By.XPATH,
                                                       '/html/body/div[1]/div[2]/div/div/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/div[2]/div[4]/div[1]/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/hj-template/div/hj-field-table/div/hj-field-table-row[2]/div/hj-field-group/div/div[2]/hj-field-group-row[2]/div/hj-field-cell/div/hj-field-control/div/div/span[1]/hj-template/div/hj-textbox/input').is_displayed() and
                                   driver.find_element(By.XPATH,
                                                       '/html/body/div[1]/div[2]/div/div/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/div[2]/div[4]/div[1]/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/hj-template/div/hj-field-table/div/hj-field-table-row[2]/div/hj-field-group/div/div[2]/hj-field-group-row[2]/div/hj-field-cell/div/hj-field-control/div/div/span[1]/hj-template/div/hj-textbox/input').is_enabled()
                )
                qtd_bloq = navegador.find_element(By.XPATH,
                                                  '/html/body/div[1]/div[2]/div/div/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/div[2]/div[4]/div[1]/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/hj-template/div/hj-field-table/div/hj-field-table-row[2]/div/hj-field-group/div/div[2]/hj-field-group-row[2]/div/hj-field-cell/div/hj-field-control/div/div/span[1]/hj-template/div/hj-textbox/input')
                qtd_bloq.send_keys(Estoque_)
                sleep(0.3)

                motivos = WebDriverWait(navegador, 20).until(
                    lambda driver: driver.find_element(By.XPATH,
                                                       '/html/body/div[1]/div[2]/div/div/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/div[2]/div[4]/div[1]/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/hj-template/div/hj-field-table/div/hj-field-table-row[2]/div/hj-field-group/div/div[2]/hj-field-group-row[3]/div/hj-field-cell/div/hj-field-control/div/div/span[1]/hj-template/div/hj-dropdownlist/span').is_displayed() and
                                   driver.find_element(By.XPATH,
                                                       '/html/body/div[1]/div[2]/div/div/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/div[2]/div[4]/div[1]/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/hj-template/div/hj-field-table/div/hj-field-table-row[2]/div/hj-field-group/div/div[2]/hj-field-group-row[3]/div/hj-field-cell/div/hj-field-control/div/div/span[1]/hj-template/div/hj-dropdownlist/span').is_enabled()
                )
                motivos = navegador.find_element(By.XPATH,
                                                 '/html/body/div[1]/div[2]/div/div/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/div[2]/div[4]/div[1]/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/hj-template/div/hj-field-table/div/hj-field-table-row[2]/div/hj-field-group/div/div[2]/hj-field-group-row[3]/div/hj-field-cell/div/hj-field-control/div/div/span[1]/hj-template/div/hj-dropdownlist/span')
                motivos.click()

                esc = navegador.find_elements(By.CSS_SELECTOR,
                                              'li.k-item')
                for x in esc:
                    if "01 - Merc.Perdida" == x.text:
                        x.click()
                        break

                sleep(0.3)

                feito = WebDriverWait(navegador, 20).until(
                    lambda driver: driver.find_element(By.LINK_TEXT,
                                                       'Desbloquear').is_displayed() and
                                   driver.find_element(By.LINK_TEXT,
                                                       'Desbloquear').is_enabled()
                )
                feito = navegador.find_element(By.LINK_TEXT,
                                                'Desbloquear')
                feito.click()
                sleep(0.3)

                ok4 = WebDriverWait(navegador, 20).until(
                    lambda driver: driver.find_element(By.CLASS_NAME, 'hj-dlg-button').is_displayed() and
                                   driver.find_element(By.CLASS_NAME, 'hj-dlg-button').is_enabled()
                )
                ok4 = navegador.find_element(By.CLASS_NAME, 'hj-dlg-button')
                ok4.click()
                sleep(0.3)

                while True:
                    try:
                        consus = WebDriverWait(navegador, 20).until(
                            lambda driver: driver.find_element(By.CSS_SELECTOR,
                                                               'input.k-textbox').is_displayed() and
                                           driver.find_element(By.CSS_SELECTOR, 'input.k-textbox').is_enabled()
                        )
                        consus = navegador.find_element(By.CSS_SELECTOR, 'input.k-textbox')
                        consus.clear()
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
                sleep(0.3)

            if Negociacao_ == 0:
                Nome_negociacao = "Sem modificação"

            elif Negociacao_ > 0:
                Nome_negociacao = f"Bloqueado com sucesso!!"

                bloquear = WebDriverWait(navegador, 20).until(
                    lambda driver: driver.find_element(By.LINK_TEXT,
                                                       'Bloqueio').is_displayed() and
                                   driver.find_element(By.LINK_TEXT,
                                                       'Bloqueio').is_enabled()
                )
                bloquear = navegador.find_element(By.LINK_TEXT,
                                                  'Bloqueio')
                bloquear.click()
                sleep(0.3)

                estoque_cont = WebDriverWait(navegador, 20).until(
                    lambda driver: driver.find_element(By.XPATH,
                                                       '/html/body/div[1]/div[2]/div/div/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/div[2]/div[3]/div[1]/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/hj-template/div/hj-field-table/div/hj-field-table-row[1]/div/hj-field-group/div/div/hj-field-group-row[1]/div/hj-field-cell[1]/div/hj-field-control/div/div/span[1]/hj-template/div/hj-textbox/input').is_displayed() and
                                   driver.find_element(By.XPATH,
                                                       '/html/body/div[1]/div[2]/div/div/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/div[2]/div[3]/div[1]/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/hj-template/div/hj-field-table/div/hj-field-table-row[1]/div/hj-field-group/div/div/hj-field-group-row[1]/div/hj-field-cell[1]/div/hj-field-control/div/div/span[1]/hj-template/div/hj-textbox/input').is_enabled()
                )
                estoque_cont = navegador.find_element(By.XPATH,
                                                      '/html/body/div[1]/div[2]/div/div/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/div[2]/div[3]/div[1]/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/hj-template/div/hj-field-table/div/hj-field-table-row[1]/div/hj-field-group/div/div/hj-field-group-row[1]/div/hj-field-cell[1]/div/hj-field-control/div/div/span[1]/hj-template/div/hj-textbox/input')
                estoque_cont.send_keys("99999")
                sleep(0.3)

                qtde_bloq = WebDriverWait(navegador, 20).until(
                    lambda driver: driver.find_element(By.XPATH,
                                                       '/html/body/div[1]/div[2]/div/div/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/div[2]/div[3]/div[1]/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/hj-template/div/hj-field-table/div/hj-field-table-row[2]/div/hj-field-group/div/div[2]/hj-field-group-row[2]/div/hj-field-cell/div/hj-field-control/div/div/span[1]/hj-template/div/hj-textbox/input').is_displayed() and
                                   driver.find_element(By.XPATH,
                                                       '/html/body/div[1]/div[2]/div/div/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/div[2]/div[3]/div[1]/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/hj-template/div/hj-field-table/div/hj-field-table-row[2]/div/hj-field-group/div/div[2]/hj-field-group-row[2]/div/hj-field-cell/div/hj-field-control/div/div/span[1]/hj-template/div/hj-textbox/input').is_enabled()
                )
                qtde_bloq = navegador.find_element(By.XPATH,
                                                   '/html/body/div[1]/div[2]/div/div/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/div[2]/div[3]/div[1]/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/hj-template/div/hj-field-table/div/hj-field-table-row[2]/div/hj-field-group/div/div[2]/hj-field-group-row[2]/div/hj-field-cell/div/hj-field-control/div/div/span[1]/hj-template/div/hj-textbox/input')
                qtde_bloq.clear()
                qtde_bloq.send_keys(f"{Negociacao_}")

                motivos = WebDriverWait(navegador, 20).until(
                    lambda driver: driver.find_element(By.XPATH,
                                                       '/html/body/div[1]/div[2]/div/div/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/div[2]/div[3]/div[1]/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/hj-template/div/hj-field-table/div/hj-field-table-row[2]/div/hj-field-group/div/div[2]/hj-field-group-row[3]/div/hj-field-cell/div/hj-field-control/div/div/span[1]/hj-template/div/hj-dropdownlist/span').is_displayed() and
                                   driver.find_element(By.XPATH,
                                                       '/html/body/div[1]/div[2]/div/div/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/div[2]/div[3]/div[1]/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/hj-template/div/hj-field-table/div/hj-field-table-row[2]/div/hj-field-group/div/div[2]/hj-field-group-row[3]/div/hj-field-cell/div/hj-field-control/div/div/span[1]/hj-template/div/hj-dropdownlist/span').is_enabled()
                )
                motivos = navegador.find_element(By.XPATH,
                                                 '/html/body/div[1]/div[2]/div/div/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/div[2]/div[3]/div[1]/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/hj-template/div/hj-field-table/div/hj-field-table-row[2]/div/hj-field-group/div/div[2]/hj-field-group-row[3]/div/hj-field-cell/div/hj-field-control/div/div/span[1]/hj-template/div/hj-dropdownlist/span')
                motivos.click()
                sleep(0.3)

                esc = navegador.find_elements(By.CSS_SELECTOR,
                                              'li.k-item')
                for x in esc:
                    if "99 - Dep. Negociacao" == x.text:
                        x.click()
                        break

                sleep(0.3)

                feito2 = WebDriverWait(navegador, 20).until(
                    lambda driver: driver.find_element(By.LINK_TEXT,
                                                       'Bloquear').is_displayed() and
                                   driver.find_element(By.LINK_TEXT,
                                                       'Bloquear').is_enabled()
                )
                feito2 = navegador.find_element(By.LINK_TEXT,
                                                'Bloquear')
                feito2.click()

                sleep(0.3)
                ok4 = WebDriverWait(navegador, 20).until(
                    lambda driver: driver.find_element(By.CLASS_NAME, 'hj-dlg-button').is_displayed() and
                                   driver.find_element(By.CLASS_NAME, 'hj-dlg-button').is_enabled()
                )
                ok4 = navegador.find_element(By.CLASS_NAME, 'hj-dlg-button')
                ok4.click()
                sleep(0.3)

                while True:
                    try:
                        consus = WebDriverWait(navegador, 20).until(
                            lambda driver: driver.find_element(By.CSS_SELECTOR,
                                                               'input.k-textbox').is_displayed() and
                                           driver.find_element(By.CSS_SELECTOR, 'input.k-textbox').is_enabled()
                        )
                        consus = navegador.find_element(By.CSS_SELECTOR, 'input.k-textbox')
                        consus.clear()
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
                sleep(0.3)

            elif Negociacao_ < 0:
                Nome_negociacao = f"Desbloqueado com sucesso!!"
                desbloquear = WebDriverWait(navegador, 20).until(
                    lambda driver: driver.find_element(By.LINK_TEXT,
                                                       'Desbloqueio').is_displayed() and
                                   driver.find_element(By.LINK_TEXT,
                                                       'Desbloqueio').is_enabled()
                )
                desbloquear = navegador.find_element(By.LINK_TEXT,
                                                     'Desbloqueio')
                desbloquear.click()
                Negociacao_ = (Negociacao_ * -1)
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
                qtd_bloq.send_keys(Negociacao_)
                sleep(0.3)

                motivos = WebDriverWait(navegador, 20).until(
                    lambda driver: driver.find_element(By.XPATH,
                                                       '/html/body/div[1]/div[2]/div/div/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/div[2]/div[4]/div[1]/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/hj-template/div/hj-field-table/div/hj-field-table-row[2]/div/hj-field-group/div/div[2]/hj-field-group-row[3]/div/hj-field-cell/div/hj-field-control/div/div/span[1]/hj-template/div/hj-dropdownlist/span').is_displayed() and
                                   driver.find_element(By.XPATH,
                                                       '/html/body/div[1]/div[2]/div/div/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/div[2]/div[4]/div[1]/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/hj-template/div/hj-field-table/div/hj-field-table-row[2]/div/hj-field-group/div/div[2]/hj-field-group-row[3]/div/hj-field-cell/div/hj-field-control/div/div/span[1]/hj-template/div/hj-dropdownlist/span').is_enabled()
                )
                motivos = navegador.find_element(By.XPATH,
                                                 '/html/body/div[1]/div[2]/div/div/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/div[2]/div[4]/div[1]/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/hj-template/div/hj-field-table/div/hj-field-table-row[2]/div/hj-field-group/div/div[2]/hj-field-group-row[3]/div/hj-field-cell/div/hj-field-control/div/div/span[1]/hj-template/div/hj-dropdownlist/span')
                motivos.click()

                esc = navegador.find_elements(By.CSS_SELECTOR,
                                              'li.k-item')
                for x in esc:
                    if "99 - Dep. Negociacao" == x.text:
                        x.click()
                        break
                sleep(0.3)


                feito = WebDriverWait(navegador, 20).until(
                    lambda driver: driver.find_element(By.LINK_TEXT,
                                                       'Desbloquear').is_displayed() and
                                   driver.find_element(By.LINK_TEXT,
                                                       'Desbloquear').is_enabled()
                )
                feito = navegador.find_element(By.LINK_TEXT,
                                               'Desbloquear')
                feito.click()

                sleep(0.3)
                ok4 = WebDriverWait(navegador, 20).until(
                    lambda driver: driver.find_element(By.CLASS_NAME, 'hj-dlg-button').is_displayed() and
                                   driver.find_element(By.CLASS_NAME, 'hj-dlg-button').is_enabled()
                )
                ok4 = navegador.find_element(By.CLASS_NAME, 'hj-dlg-button')
                ok4.click()
                sleep(0.3)

                while True:
                    try:
                        consus = WebDriverWait(navegador, 20).until(
                            lambda driver: driver.find_element(By.CSS_SELECTOR,
                                                               'input.k-textbox').is_displayed() and
                                           driver.find_element(By.CSS_SELECTOR, 'input.k-textbox').is_enabled()
                        )
                        consus = navegador.find_element(By.CSS_SELECTOR, 'input.k-textbox')
                        consus.clear()
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

                sleep(0.3)
            if Saldo_ == 0:
                Nome_saldo = "Sem modificação"
                sleep(2)
                voltar = WebDriverWait(navegador, 20).until(
                    lambda driver: driver.find_element(By.XPATH,
                                                       "/html/body/div[1]/div[2]/div/div/div/hj-flex-container/div/hj-flex-shrink/div/div/div[1]/a[1]/span/i[2]").is_displayed() and
                                   driver.find_element(By.XPATH,
                                                       "/html/body/div[1]/div[2]/div/div/div/hj-flex-container/div/hj-flex-shrink/div/div/div[1]/a[1]/span/i[2]").is_enabled()
                )
                voltar = navegador.find_element(By.XPATH,
                                                "/html/body/div[1]/div[2]/div/div/div/hj-flex-container/div/hj-flex-shrink/div/div/div[1]/a[1]/span/i[2]")
                voltar.click()

            elif Saldo_ > 0:
                Nome_saldo = f"Bloqueado com sucesso!!"
                bloquear = WebDriverWait(navegador, 20).until(
                    lambda driver: driver.find_element(By.LINK_TEXT,
                                                       'Bloqueio').is_displayed() and
                                   driver.find_element(By.LINK_TEXT,
                                                       'Bloqueio').is_enabled()
                )
                bloquear = navegador.find_element(By.LINK_TEXT,
                                                  'Bloqueio')
                bloquear.click()
                sleep(0.3)

                estoque_cont = WebDriverWait(navegador, 20).until(
                    lambda driver: driver.find_element(By.XPATH,
                                                       '/html/body/div[1]/div[2]/div/div/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/div[2]/div[3]/div[1]/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/hj-template/div/hj-field-table/div/hj-field-table-row[1]/div/hj-field-group/div/div/hj-field-group-row[1]/div/hj-field-cell[1]/div/hj-field-control/div/div/span[1]/hj-template/div/hj-textbox/input').is_displayed() and
                                   driver.find_element(By.XPATH,
                                                       '/html/body/div[1]/div[2]/div/div/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/div[2]/div[3]/div[1]/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/hj-template/div/hj-field-table/div/hj-field-table-row[1]/div/hj-field-group/div/div/hj-field-group-row[1]/div/hj-field-cell[1]/div/hj-field-control/div/div/span[1]/hj-template/div/hj-textbox/input').is_enabled()
                )
                estoque_cont = navegador.find_element(By.XPATH,
                                                      '/html/body/div[1]/div[2]/div/div/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/div[2]/div[3]/div[1]/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/hj-template/div/hj-field-table/div/hj-field-table-row[1]/div/hj-field-group/div/div/hj-field-group-row[1]/div/hj-field-cell[1]/div/hj-field-control/div/div/span[1]/hj-template/div/hj-textbox/input')
                estoque_cont.send_keys("99999")

                qtde_bloq = WebDriverWait(navegador, 20).until(
                    lambda driver: driver.find_element(By.XPATH,
                                                       '/html/body/div[1]/div[2]/div/div/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/div[2]/div[3]/div[1]/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/hj-template/div/hj-field-table/div/hj-field-table-row[2]/div/hj-field-group/div/div[2]/hj-field-group-row[1]/div/hj-field-cell/div/hj-field-control/div/div/span[1]/hj-template/div/hj-textbox/input').is_displayed() and
                                   driver.find_element(By.XPATH,
                                                       '/html/body/div[1]/div[2]/div/div/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/div[2]/div[3]/div[1]/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/hj-template/div/hj-field-table/div/hj-field-table-row[2]/div/hj-field-group/div/div[2]/hj-field-group-row[1]/div/hj-field-cell/div/hj-field-control/div/div/span[1]/hj-template/div/hj-textbox/input').is_enabled()
                )
                qtde_bloq = navegador.find_element(By.XPATH,
                                                   '/html/body/div[1]/div[2]/div/div/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/div[2]/div[3]/div[1]/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/hj-template/div/hj-field-table/div/hj-field-table-row[2]/div/hj-field-group/div/div[2]/hj-field-group-row[1]/div/hj-field-cell/div/hj-field-control/div/div/span[1]/hj-template/div/hj-textbox/input')
                qtde_bloq.clear()
                qtde_bloq.send_keys(f"{Saldo_}")
                sleep(0.3)

                motivos = WebDriverWait(navegador, 20).until(
                    lambda driver: driver.find_element(By.XPATH,
                                                       '/html/body/div[1]/div[2]/div/div/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/div[2]/div[3]/div[1]/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/hj-template/div/hj-field-table/div/hj-field-table-row[2]/div/hj-field-group/div/div[2]/hj-field-group-row[3]/div/hj-field-cell/div/hj-field-control/div/div/span[1]/hj-template/div/hj-dropdownlist/span').is_displayed() and
                                   driver.find_element(By.XPATH,
                                                       '/html/body/div[1]/div[2]/div/div/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/div[2]/div[3]/div[1]/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/hj-template/div/hj-field-table/div/hj-field-table-row[2]/div/hj-field-group/div/div[2]/hj-field-group-row[3]/div/hj-field-cell/div/hj-field-control/div/div/span[1]/hj-template/div/hj-dropdownlist/span').is_enabled()
                )
                motivos = navegador.find_element(By.XPATH,
                                                 '/html/body/div[1]/div[2]/div/div/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/div[2]/div[3]/div[1]/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/hj-template/div/hj-field-table/div/hj-field-table-row[2]/div/hj-field-group/div/div[2]/hj-field-group-row[3]/div/hj-field-cell/div/hj-field-control/div/div/span[1]/hj-template/div/hj-dropdownlist/span')
                motivos.click()

                esc = navegador.find_elements(By.CSS_SELECTOR,
                                              'li.k-item')
                for x in esc:
                    if "101 - SALDO" == x.text:
                        x.click()
                        break
                sleep(0.3)

                feito2 = WebDriverWait(navegador, 20).until(
                    lambda driver: driver.find_element(By.LINK_TEXT,
                                                       'Bloquear').is_displayed() and
                                   driver.find_element(By.LINK_TEXT,
                                                       'Bloquear').is_enabled()
                )
                feito2 = navegador.find_element(By.LINK_TEXT,
                                                'Bloquear')
                feito2.click()
                sleep(0.3)

                ok4 = WebDriverWait(navegador, 20).until(
                    lambda driver: driver.find_element(By.CLASS_NAME, 'hj-dlg-button').is_displayed() and
                                   driver.find_element(By.CLASS_NAME, 'hj-dlg-button').is_enabled()
                )
                ok4 = navegador.find_element(By.CLASS_NAME, 'hj-dlg-button')
                ok4.click()
                sleep(0.3)


            elif Saldo_ < 0:
                Nome_saldo = f"Desbloqueado com sucesso!!"
                desbloquear = WebDriverWait(navegador, 20).until(
                    lambda driver: driver.find_element(By.LINK_TEXT,
                                                       'Desbloqueio').is_displayed() and
                                   driver.find_element(By.LINK_TEXT,
                                                       'Desbloqueio').is_enabled()
                )
                desbloquear = navegador.find_element(By.LINK_TEXT,
                                                     'Desbloqueio')
                desbloquear.click()

                Saldo_ = (Saldo_ * -1)
                click_desbloq = WebDriverWait(navegador, 20).until(
                    lambda driver: driver.find_element(By.XPATH,
                                                       '/html/body/div[1]/div[2]/div/div/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/div[2]/div[3]/div[1]/hj-flex-container/div/hj-flex-grow/div/div/hj-grid/div[2]/div/div[2]/table/tbody/tr[1]/td[10]/a/hj-label').is_displayed() and
                                   driver.find_element(By.XPATH,
                                                       '/html/body/div[1]/div[2]/div/div/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/div[2]/div[3]/div[1]/hj-flex-container/div/hj-flex-grow/div/div/hj-grid/div[2]/div/div[2]/table/tbody/tr[1]/td[10]/a/hj-label').is_enabled()
                )
                click_desbloq = navegador.find_element(By.XPATH,
                                                       '/html/body/div[1]/div[2]/div/div/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/div[2]/div[3]/div[1]/hj-flex-container/div/hj-flex-grow/div/div/hj-grid/div[2]/div/div[2]/table/tbody/tr[1]/td[10]/a/hj-label')
                click_desbloq.click()
                sleep(0.3)

                # Quantidade a bloquear
                qtd_bloq = WebDriverWait(navegador, 20).until(
                    lambda driver: driver.find_element(By.XPATH,
                                                       '/html/body/div[1]/div[2]/div/div/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/div[2]/div[4]/div[1]/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/hj-template/div/hj-field-table/div/hj-field-table-row[2]/div/hj-field-group/div/div[2]/hj-field-group-row[2]/div/hj-field-cell/div/hj-field-control/div/div/span[1]/hj-template/div/hj-textbox/input').is_displayed() and
                                   driver.find_element(By.XPATH,
                                                       '/html/body/div[1]/div[2]/div/div/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/div[2]/div[4]/div[1]/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/hj-template/div/hj-field-table/div/hj-field-table-row[2]/div/hj-field-group/div/div[2]/hj-field-group-row[2]/div/hj-field-cell/div/hj-field-control/div/div/span[1]/hj-template/div/hj-textbox/input').is_enabled()
                )
                qtd_bloq = navegador.find_element(By.XPATH,
                                                  '/html/body/div[1]/div[2]/div/div/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/div[2]/div[4]/div[1]/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/hj-template/div/hj-field-table/div/hj-field-table-row[2]/div/hj-field-group/div/div[2]/hj-field-group-row[2]/div/hj-field-cell/div/hj-field-control/div/div/span[1]/hj-template/div/hj-textbox/input')
                qtd_bloq.send_keys(Saldo_)

                motivos = WebDriverWait(navegador, 20).until(
                    lambda driver: driver.find_element(By.XPATH,
                                                       '/html/body/div[1]/div[2]/div/div/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/div[2]/div[4]/div[1]/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/hj-template/div/hj-field-table/div/hj-field-table-row[2]/div/hj-field-group/div/div[2]/hj-field-group-row[3]/div/hj-field-cell/div/hj-field-control/div/div/span[1]/hj-template/div/hj-dropdownlist/span').is_displayed() and
                                   driver.find_element(By.XPATH,
                                                       '/html/body/div[1]/div[2]/div/div/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/div[2]/div[4]/div[1]/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/hj-template/div/hj-field-table/div/hj-field-table-row[2]/div/hj-field-group/div/div[2]/hj-field-group-row[3]/div/hj-field-cell/div/hj-field-control/div/div/span[1]/hj-template/div/hj-dropdownlist/span').is_enabled()
                )
                motivos = navegador.find_element(By.XPATH,
                                                 '/html/body/div[1]/div[2]/div/div/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/div[2]/div[4]/div[1]/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/hj-template/div/hj-field-table/div/hj-field-table-row[2]/div/hj-field-group/div/div[2]/hj-field-group-row[3]/div/hj-field-cell/div/hj-field-control/div/div/span[1]/hj-template/div/hj-dropdownlist/span')
                motivos.click()
                sleep(0.3)

                esc = navegador.find_elements(By.CSS_SELECTOR,
                                              'li.k-item')
                for x in esc:
                    if "101 - SALDO" == x.text:
                        x.click()
                        break

                feito = WebDriverWait(navegador, 20).until(
                    lambda driver: driver.find_element(By.LINK_TEXT,
                                                       'Desbloquear').is_displayed() and
                                   driver.find_element(By.LINK_TEXT,
                                                       'Desbloquear').is_enabled()
                )
                feito = navegador.find_element(By.LINK_TEXT,
                                               'Desbloquear')
                feito.click()
                sleep(0.3)
                ok4 = WebDriverWait(navegador, 20).until(
                    lambda driver: driver.find_element(By.CLASS_NAME, 'hj-dlg-button').is_displayed() and
                                   driver.find_element(By.CLASS_NAME, 'hj-dlg-button').is_enabled()
                )
                ok4 = navegador.find_element(By.CLASS_NAME, 'hj-dlg-button')
                ok4.click()
                sleep(0.3)


            print(
                f"Item:[{item_}] Suspenso em Vendas: [ {Estoque_} | {Nome_estoque} ], Negociação: [ {Negociacao_} | {Nome_negociacao} ], Saldo: [ {Saldo_} | {Nome_saldo} ]")

            registrar_progresso(
                text=f"Tratativa Bloqueado do Item: [ {item_} ] Suspenso em Vendas: [ {Estoque_} ], Negociação: [ {Negociacao_} ], Saldo: [ {Saldo_} ] ",
                endereco="", sucesso=True)
        except:

            print(
                f"Item:[{item_}] Suspenso em Vendas: [ {Estoque_} | Erro ], Negociação: [ {Negociacao_} | Erro ], Saldo: [ {Saldo_} | Erro ]")

            registrar_progresso(
                text=f"Tratativa Bloqueado do Item: [ {item_} ] Suspenso em Vendas: [ {Estoque_} | Erro ], Negociação: [ {Negociacao_} | Erro ], Saldo: [ {Saldo_} | Erro ] ",
                endereco="", sucesso=False)

            file_path.close()
            navegador.quit()

            navegador = navegador_google()

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

                sheet_data = file_path.parse('Tratativa do Bloqueado avançado')
                Estoque = file_path.parse('Tratativa do Bloqueado avançado')
                Negociacao = file_path.parse('Tratativa do Bloqueado avançado')
                Saldo = file_path.parse('Tratativa do Bloqueado avançado')
                sheet_data.head()
                Estoque.head()
                Negociacao.head()
                Saldo.head()
                itens1 = sheet_data['Itens']
                Estoque1 = Estoque['Estoque']
                Negociacao1 = Negociacao['Negociação']
                Saldo1 = Saldo['Saldo']

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
