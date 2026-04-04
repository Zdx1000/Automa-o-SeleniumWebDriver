from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import pandas as pd
from utils.shared import historico_funcoes, registrar_progresso
from utils.retornar import cancelar_inputs
from utils.navegador import navegador_google
from time import sleep
from utils.bloqueadao import BloqueioDAO

def bloqueio():
    from main import tabela

    historico_funcoes.append(tabela)
    try:
        while True:
            print(
                "\033[96m\n╔══════════════════════════════════════════════╗"
                "\n║           Selecione o tipo de bloqueio       ║"
                "\n╚══════════════════════════════════════════════╝\033[0m"
            )
            print(
                "  [1] Suspenso em vendas\n"
                "  [2] Saldo\n"
                "  [3] Negociação\n"
                "────────────────────────────────────────────\n"
                "  [F8] Voltar ao menu principal\n"
            )
            try:
                escolha2 = int(input("Digite a opção desejada: "))
                if 0 < escolha2 < 4:
                    break
                print("\033[91mOpção inválida. Escolha 1, 2 ou 3.\033[0m")
                sleep(1.2)
            except ValueError:
                print("\033[91mEntrada inválida. Informe apenas números.\033[0m")
                sleep(1.2)
            except Exception:
                print("\033[91mNão foi possível ler a opção. Tente novamente.\033[0m")
                sleep(1.2)
        try:
            navegador = navegador_google()
        except:
            try:
                navegador.quit()
            except:
                pass
            return cancelar_inputs()

        cont = 0
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

        try:
            file_path = 'Banco de dados.xlsx'
            file_path = pd.ExcelFile(file_path)
            file_path.sheet_names

            sheet_data = file_path.parse('Bloqueio por Item')
            qtde = file_path.parse('Bloqueio por Item')
            sheet_data.head()
            qtde.head()
            itens2 = sheet_data['Itens']
            quantidades2 = qtde['Qtde']
        except Exception:
            print("Verifique o arquivo para consulta...")
            tabela

        for item_s, quantidade_2 in zip(itens2, quantidades2):
            
            try:
                BloqueioDAO(navegador, item_s, quantidade_2, tipo=escolha2).processo_bloquear()
            except Exception as e:
                print(f"Erro ao processar o item {item_s}: {e}")
                continue

            cont += 1

            porcentagem = (cont / len(itens2)) * 100
            print(f"Confirmado com sucesso: {cont}/{len(itens2)} ({porcentagem:.1f}%) - {item_s}")

            if escolha2 == 1:
                registrar_progresso(
                    text=f"Bloqueio realizado com sucesso no Suspenso em vendas: {item_s} -> Qtde: ",
                    endereco=quantidade_2, sucesso=True)
            elif escolha2 == 2:
                registrar_progresso(
                    text=f"Bloqueio realizado com sucesso no Suspenso em Saldo: {item_s} -> Qtde: ",
                    endereco=quantidade_2, sucesso=True)
            elif escolha2 == 3:
                registrar_progresso(
                    text=f"Bloqueio realizado com sucesso no Suspenso em Negociação: {item_s} -> Qtde: ",
                    endereco=quantidade_2, sucesso=True)


        file_path.close()
        navegador.quit()
        cancelar_inputs()
    except:
        print(f'''Erro ao iniciar o sistema, Verifique os dados dos itens....''', 1)
        cancelar_inputs()