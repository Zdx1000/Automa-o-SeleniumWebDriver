from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
from utils.shared import historico_funcoes, registrar_progresso
from utils.retornar import cancelar_inputs
from utils.navegador import navegador_google
from time import sleep


def inclusao_pedidos_ajustes():
    from main import tabela

    historico_funcoes.append(tabela)
    print(f'''
    ╔════════════════════════════════════════════════════════╗
    ║          Inclusão de pedido de ajuste contábil         ║
    ╚════════════════════════════════════════════════════════╝
    ''')

    print(f"\n[0] Escreva 0 para retornar\n")

    print(f"Insira o N° da Uz\n")
    documento = input(f"> ")
    if documento == "0":
        cancelar_inputs()

    print(f"Matrícula do solicitante\n")
    matricula = input(f"> ")
    if matricula == "0":
        cancelar_inputs()

    print(f'''
╔════════════════════════════════════════════╗
║               Tipo de ajuste               ║
╚════════════════════════════════════════════╝
    [1] 4 - AJUSTE SOBRA ESTOQUE
    [2] 8 - AJUSTE FALTA ESTOQUE
    ''')

    print(f"Escolha uma opção\n")
    tipo_ajuste = input(f"> ")
    if tipo_ajuste == "0":
        cancelar_inputs()

    print(f'''
╔════════════════════════════════════════════╗
║               Centro de custo              ║
╚════════════════════════════════════════════╝
    [1] 30212 - Separação Carga Grossa
    [2] 30213 - Separação Carga Fracionada
    ''')

    print(f"Escolha uma opção\n")
    centro_custo = input(f"> ")
    if centro_custo == "0":
        cancelar_inputs()

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

        slr = WebDriverWait(navegador, 20).until(
            lambda driver: driver.find_element(By.LINK_TEXT, 'S.L.R').is_displayed() and
                           driver.find_element(By.LINK_TEXT, 'S.L.R').is_enabled()
        )
        slr = navegador.find_element(By.LINK_TEXT, 'S.L.R')
        slr.click()

        inclusao = WebDriverWait(navegador, 20).until(
            lambda driver: driver.find_element(By.LINK_TEXT, 'INCLUSÃO Pedidos Ajustes').is_displayed() and
                           driver.find_element(By.LINK_TEXT, 'INCLUSÃO Pedidos Ajustes').is_enabled()
        )
        inclusao = navegador.find_element(By.LINK_TEXT, 'INCLUSÃO Pedidos Ajustes')
        inclusao.click()

        confirmacao = WebDriverWait(navegador, 20).until(
            lambda driver: driver.find_element(By.LINK_TEXT, 'Confirmação de AJUSTE CONTÁBIL').is_displayed() and
                           driver.find_element(By.LINK_TEXT, 'Confirmação de AJUSTE CONTÁBIL').is_enabled()
        )
        confirmacao = navegador.find_element(By.LINK_TEXT, 'Confirmação de AJUSTE CONTÁBIL')
        confirmacao.click()

        documento_origem = WebDriverWait(navegador, 20).until(
            lambda driver: driver.find_element(By.CSS_SELECTOR, "div.searchLike-control-textbox-container input").is_displayed() and
                           driver.find_element(By.CSS_SELECTOR, "div.searchLike-control-textbox-container input").is_enabled()
        )
        documento_origem = navegador.find_element(By.CSS_SELECTOR, "div.searchLike-control-textbox-container input")
        documento_origem.clear()
        documento_origem.send_keys(documento)


        consultar = WebDriverWait(navegador, 20).until(
            lambda driver: driver.find_element(By.LINK_TEXT, 'Consulta').is_displayed() and
                           driver.find_element(By.LINK_TEXT, 'Consulta').is_enabled()
        )
        consultar = navegador.find_element(By.LINK_TEXT, 'Consulta')
        consultar.click()

        incluir = WebDriverWait(navegador, 20).until(
            lambda driver: driver.find_element(By.LINK_TEXT,
                                               "Incluir Pedido AJUSTE").is_displayed() and
                           driver.find_element(By.LINK_TEXT,
                                               "Incluir Pedido AJUSTE").is_enabled()
        )
        incluir = navegador.find_element(By.LINK_TEXT, "Incluir Pedido AJUSTE")
        incluir.click()
    except:
        print(f"Erro ao acessar Inclusão de pedido de ajuste!!!\n")
        try:
            navegador.quit()
        except:
            pass
        return cancelar_inputs()

    try:
        file_path = 'Banco de dados.xlsx'
        file_path = pd.ExcelFile(file_path)
        file_path.sheet_names

        sheet_data = file_path.parse('Inclusão pedido de ajuste')
        qtde = file_path.parse('Inclusão pedido de ajuste')
        sheet_data.head()
        qtde.head()
        itens = sheet_data['Itens para inclusão']
        quantidades = qtde['Qtde']
    except:
        print(f"Erro  ao acessar o arquivo Banco de dados.xlsx!!!")
        try:
            navegador.quit()
        except:
            pass
        return cancelar_inputs()

    for item, quantidade in zip(itens, quantidades):
        try:
            sleep(2)
            #Atomatizar o tempo de espera para os elementos carregarem
            tipo_campo = navegador.find_elements(By.CSS_SELECTOR,
                                                "span.k-input")
            tipo_campo[9].click()

            sleep(1)

            if tipo_ajuste == "1":

                sleep(0.2)
                tipo_ = navegador.find_elements(By.CSS_SELECTOR, "li.k-item")
                for tipo in tipo_:
                    if tipo.accessible_name == "4 - AJUSTE SOBRA ESTOQUE":
                        tipo.click()
                        break

            if tipo_ajuste == "2":

                sleep(0.2)
                tipo_ = navegador.find_elements(By.CSS_SELECTOR, "li.k-item")
                for tipo in tipo_:
                    if tipo.accessible_name == "8 - AJUSTE FALTA ESTOQUE":
                        tipo.click()
                        break

            motivo_campo = navegador.find_elements(By.CSS_SELECTOR,
                                                "span.k-input")
            motivo_campo[10].click()

            sleep(1)
            if tipo_ajuste == "1":

                sleep(0.2)
                tipo_ = navegador.find_elements(By.CSS_SELECTOR, "li.k-item")
                for tipo in tipo_:
                    if tipo.accessible_name == "123 - AJ CONT EST ENTRADA":
                        tipo.click()
                        break

            if tipo_ajuste == "2":

                sleep(0.2)
                tipo_ = navegador.find_elements(By.CSS_SELECTOR, "li.k-item")
                for tipo in tipo_:
                    if tipo.accessible_name == "127 - AJ CONT EST SAIDA":
                        tipo.click()
                        break


            cod_merc = navegador.find_elements(By.CSS_SELECTOR,
                                              "input.k-textbox")
            cod_merc[4].clear()
            cod_merc[4].send_keys(item)

            sleep(0.5)

            quantidade_ajuste = navegador.find_elements(By.CSS_SELECTOR,
                                              "input.k-textbox")
            quantidade_ajuste[5].clear()
            quantidade_ajuste[5].send_keys(quantidade)

            custo = navegador.find_elements(By.CSS_SELECTOR,
                                                "span.k-input")
            custo[12].click()

            sleep(1)

            if centro_custo == "1":
                tipo_ = navegador.find_elements(By.CSS_SELECTOR, "li.k-item")
                for tipo in tipo_:
                    if tipo.accessible_name == "30212 - Separação Carga Grossa":
                        tipo.click()
                        break
            if centro_custo == "2":
                tipo_ = navegador.find_elements(By.CSS_SELECTOR, "li.k-item")
                for tipo in tipo_:
                    if tipo.accessible_name == "30213 - Separação Carga Fracionada":
                        tipo.click()
                        break

            solicitante = navegador.find_elements(By.CSS_SELECTOR,
                                              "input.k-textbox")
            solicitante[6].clear()
            solicitante[6].send_keys(matricula)

            sleep(0.2)

            obs = navegador.find_elements(By.CSS_SELECTOR,
                                              "textarea.k-textbox")
            obs[1].clear()
            obs[1].send_keys(documento)

            incluir = WebDriverWait(navegador, 20).until(
                lambda driver: driver.find_element(By.LINK_TEXT,
                                                   "Incluir Pedido").is_displayed() and
                               driver.find_element(By.LINK_TEXT,
                                                   "Incluir Pedido").is_enabled()
            )
            incluir = navegador.find_element(By.LINK_TEXT,"Incluir Pedido")
            incluir.click()

            sleep(0.5)

            confirmar = WebDriverWait(navegador, 20).until(
                lambda driver: driver.find_element(By.LINK_TEXT,
                                                   "Confirmar Inclusão").is_displayed() and
                               driver.find_element(By.LINK_TEXT,
                                                   "Confirmar Inclusão").is_enabled()
            )
            confirmar = navegador.find_element(By.LINK_TEXT,"Confirmar Inclusão")
            confirmar.click()

            sleep(1)

            ok4 = WebDriverWait(navegador, 20).until(
                lambda driver: driver.find_element(By.CSS_SELECTOR, 'button.k-button').is_displayed() and
                               driver.find_element(By.CSS_SELECTOR, 'button.k-button').is_enabled()
            )
            ok4 = navegador.find_element(By.CSS_SELECTOR, 'button.k-button')
            ok4.click()

            cont += 1

            sleep(0.5)

            porcentagem = (cont / len(itens)) * 100
            print(f"Confirmado com sucesso: {cont}/{len(itens)} ({porcentagem:.1f}%) - {item}")

            registrar_progresso(
                text=f"Item incluso: {item} Qtde: {quantidade} inclusa com sucesso no Documento: ",
                endereco=documento, sucesso=True)
        except:
            cont += 1
            sleep(0.5)
            porcentagem = (cont / len(itens)) * 100
            print(f"ERRO ao incluir: {cont}/{len(itens)} ({porcentagem:.1f}%) - {item}")

            registrar_progresso(
                text=f"Item incluso: {item} Qtde: {quantidade} Erro ao incluir no Documento: ",
                endereco=documento, sucesso=False)
            
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

                slr = WebDriverWait(navegador, 20).until(
                    lambda driver: driver.find_element(By.LINK_TEXT, 'S.L.R').is_displayed() and
                                driver.find_element(By.LINK_TEXT, 'S.L.R').is_enabled()
                )
                slr = navegador.find_element(By.LINK_TEXT, 'S.L.R')
                slr.click()

                inclusao = WebDriverWait(navegador, 20).until(
                    lambda driver: driver.find_element(By.LINK_TEXT, 'INCLUSÃO Pedidos Ajustes').is_displayed() and
                                driver.find_element(By.LINK_TEXT, 'INCLUSÃO Pedidos Ajustes').is_enabled()
                )
                inclusao = navegador.find_element(By.LINK_TEXT, 'INCLUSÃO Pedidos Ajustes')
                inclusao.click()

                confirmacao = WebDriverWait(navegador, 20).until(
                    lambda driver: driver.find_element(By.LINK_TEXT, 'Confirmação de AJUSTE CONTÁBIL').is_displayed() and
                                driver.find_element(By.LINK_TEXT, 'Confirmação de AJUSTE CONTÁBIL').is_enabled()
                )
                confirmacao = navegador.find_element(By.LINK_TEXT, 'Confirmação de AJUSTE CONTÁBIL')
                confirmacao.click()

                documento_origem = WebDriverWait(navegador, 20).until(
                    lambda driver: driver.find_element(By.CSS_SELECTOR, "div.searchLike-control-textbox-container input").is_displayed() and
                                driver.find_element(By.CSS_SELECTOR, "div.searchLike-control-textbox-container input").is_enabled()
                )
                documento_origem = navegador.find_element(By.CSS_SELECTOR, "div.searchLike-control-textbox-container input")
                documento_origem.clear()
                documento_origem.send_keys(documento)


                consultar = WebDriverWait(navegador, 20).until(
                    lambda driver: driver.find_element(By.LINK_TEXT, 'Consulta').is_displayed() and
                                driver.find_element(By.LINK_TEXT, 'Consulta').is_enabled()
                )
                consultar = navegador.find_element(By.LINK_TEXT, 'Consulta')
                consultar.click()

                incluir = WebDriverWait(navegador, 20).until(
                    lambda driver: driver.find_element(By.LINK_TEXT,
                                                    "Incluir Pedido AJUSTE").is_displayed() and
                                driver.find_element(By.LINK_TEXT,
                                                    "Incluir Pedido AJUSTE").is_enabled()
                )
                incluir = navegador.find_element(By.LINK_TEXT, "Incluir Pedido AJUSTE")
                incluir.click()

                sleep(2)
            except:
                print(f"Erro ao acessar Inclusão de pedido de ajuste!!!\n")
                try:
                    navegador.quit()
                except:
                    pass
                return cancelar_inputs()

            try:
                file_path = 'Banco de dados.xlsx'
                file_path = pd.ExcelFile(file_path)
                file_path.sheet_names

                sheet_data = file_path.parse('Inclusão pedido de ajuste')
                qtde = file_path.parse('Inclusão pedido de ajuste')
                sheet_data.head()
                qtde.head()
                itens = sheet_data['Itens para inclusão']
                quantidades = qtde['Qtde']
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