from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import pandas as pd
from utils.shared import historico_funcoes, registrar_progresso
from utils.retornar import cancelar_inputs
from utils.navegador import navegador_google
from time import sleep
from utils.bloqueadao import BloqueioDAO



def Bloqueado_avancado():
    from main import tabela

    historico_funcoes.append(tabela)

    print('''
╔════════════════════════════════════════════════════════╗
║                 Tratativa do Bloqueado                 ║
╚════════════════════════════════════════════════════════╝
''')

    print('''
╔════════════════════════════════════════════════════════════════════════════╗
║                                                                          ║
║                  Muito CUIDADO ao utilizar esta função!                  ║
║                                                                          ║
║      Certifique-se de que todos os dados estão corretos antes de prosseguir. ║
║                                                                          ║
║               Analise todos os itens novamente, se possível!             ║
║                                                                          ║
║ Em caso de erro, as consequências serão em ampla escala, dependendo dos dados. ║
║                                                                          ║
║ ═══════════════════════════════════════════════════════════════════════════ ║
║                                                                          ║
║                           Apenas colaboradores AUTORIZADOS               ║
║                                                                          ║
╚════════════════════════════════════════════════════════════════════════════╝
''')

    print("\n[F8] Para voltar ao menu principal\n")
    print("\nPressione Enter para continuar...\n")
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

            if Estoque_ == 0:
                Nome_estoque = "Sem modificacação"

            elif Estoque_ > 0:
                Nome_estoque = f"Bloqueado com sucesso!!"
                sleep(0.5)

                try:
                    BloqueioDAO(navegador, item_, Estoque_, tipo=1).processo_bloquear()
                except Exception as e:
                    print(f"Erro ao processar o item {item_}: {e}")
                    continue

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

                Estoque_ = (Estoque_ * -1)

                try:
                    BloqueioDAO(navegador, item_, Estoque_, tipo=1).processo_desbloquear_sem_consultar()
                except Exception as e:
                    print(f"Erro ao processar o item {item_}: {e}")
                    continue

                Nome_estoque = f"Desbloqueado com sucesso!!"

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

                try:
                    BloqueioDAO(navegador, item_, Negociacao_, tipo=3).processo_bloquear()
                except Exception as e:
                    print(f"Erro ao processar o item {item_}: {e}")
                    continue

                Nome_negociacao = f"Bloqueado com sucesso!!"

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
                Negociacao_ = (Negociacao_ * -1)

                try:
                    BloqueioDAO(navegador, item_, Negociacao_, tipo=3).processo_desbloquear_sem_consultar()
                except Exception as e:
                    print(f"Erro ao processar o item {item_}: {e}")
                    continue

                Nome_negociacao = f"Desbloqueado com sucesso!!"

                sleep(0.3)
            if Saldo_ == 0:
                Nome_saldo = "Sem modificação"
                sleep(2)
                voltar2_ = WebDriverWait(navegador, 20).until(
                    lambda driver: driver.find_element(By.CSS_SELECTOR,
                                                    "a[data-hj-test-id='active-thread-previous-button']").is_displayed() and
                                driver.find_element(By.CSS_SELECTOR,
                                                    "a[data-hj-test-id='active-thread-previous-button']").is_enabled()
                )
                voltar2_ = navegador.find_element(By.CSS_SELECTOR, "a[data-hj-test-id='active-thread-previous-button']")
                voltar2_.click()

            elif Saldo_ > 0:
                Nome_saldo = f"Bloqueado com sucesso!!"
                try:
                    BloqueioDAO(navegador, item_, Saldo_, tipo=2).processo_bloquear()
                except Exception as e:
                    print(f"Erro ao processar o item {item_}: {e}")
                    continue


            elif Saldo_ < 0:
                Nome_saldo = f"Desbloqueado com sucesso!!"
                Saldo_ = (Saldo_ * -1)

                try:
                    BloqueioDAO(navegador, item_, Saldo_, tipo=2).processo_desbloquear()
                except Exception as e:
                    print(f"Erro ao processar o item {item_}: {e}")
                    continue


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
