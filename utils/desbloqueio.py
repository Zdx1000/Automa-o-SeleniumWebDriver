from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import pandas as pd
from utils.shared import historico_funcoes, registrar_progresso
from utils.retornar import cancelar_inputs
from utils.navegador import navegador_google
from time import sleep
from utils.bloqueadao import BloqueioDAO


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

            try:
                BloqueioDAO(navegador, item_, quantidade_, tipo=escolha).processo_desbloquear()
            except Exception as e:
                print(f"Erro ao processar o item {item_}: {e}")
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
