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
            tipo_campo = WebDriverWait(navegador, 20).until(
                lambda driver: driver.find_element(By.XPATH,
                                                   "/html/body/div[1]/div[2]/div/div/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/div[2]/div[3]/div[1]/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/hj-template[1]/div/hj-field-table/div/hj-field-table-row/div/hj-field-group/div/div/hj-field-group-row[5]/div/hj-field-cell/div/hj-field-control/div/div/span[1]/hj-template/div/hj-dropdownlist/span/span").is_displayed() and
                               driver.find_element(By.XPATH,
                                                   "/html/body/div[1]/div[2]/div/div/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/div[2]/div[3]/div[1]/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/hj-template[1]/div/hj-field-table/div/hj-field-table-row/div/hj-field-group/div/div/hj-field-group-row[5]/div/hj-field-cell/div/hj-field-control/div/div/span[1]/hj-template/div/hj-dropdownlist/span/span").is_enabled()
            )
            tipo_campo = navegador.find_element(By.XPATH,
                                                "/html/body/div[1]/div[2]/div/div/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/div[2]/div[3]/div[1]/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/hj-template[1]/div/hj-field-table/div/hj-field-table-row/div/hj-field-group/div/div/hj-field-group-row[5]/div/hj-field-cell/div/hj-field-control/div/div/span[1]/hj-template/div/hj-dropdownlist/span/span")
            tipo_campo.click()

            if tipo_ajuste == "1":

                sleep(1)
                tipo_ = WebDriverWait(navegador, 20).until(
                    lambda driver: driver.find_element(By.CSS_SELECTOR, "div.k-animation-container ul.k-list li[data-offset-index='3']").is_displayed() and
                                   driver.find_element(By.CSS_SELECTOR, "div.k-animation-container ul.k-list li[data-offset-index='3']").is_enabled()
                )
                tipo_ = navegador.find_element(By.CSS_SELECTOR, "div.k-animation-container ul.k-list li[data-offset-index='3']")
                tipo_.click()

            if tipo_ajuste == "2":

                sleep(1)
                tipo_ = WebDriverWait(navegador, 20).until(
                    lambda driver: driver.find_element(By.CSS_SELECTOR,
                                                       "div.k-animation-container ul.k-list li[data-offset-index='5']").is_displayed() and
                                   driver.find_element(By.CSS_SELECTOR,
                                                       "div.k-animation-container ul.k-list li[data-offset-index='5']").is_enabled()
                )
                tipo_ = navegador.find_element(By.CSS_SELECTOR,
                                               "div.k-animation-container ul.k-list li[data-offset-index='5']")
                tipo_.click()

            clck1 = WebDriverWait(navegador, 20).until(
                lambda driver: driver.find_element(By.XPATH,
                                                   "/html/body/div[1]/div[2]/div/div/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/div[2]/div[3]/div[1]/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/hj-template[1]/div/hj-field-table/div/hj-field-table-row/div/hj-field-group/div/div/hj-field-group-row[6]/div/hj-field-cell/div/hj-field-control/div/div/span[1]/hj-template/div/hj-dropdownlist/span").is_displayed() and
                               driver.find_element(By.XPATH,
                                                   "/html/body/div[1]/div[2]/div/div/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/div[2]/div[3]/div[1]/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/hj-template[1]/div/hj-field-table/div/hj-field-table-row/div/hj-field-group/div/div/hj-field-group-row[6]/div/hj-field-cell/div/hj-field-control/div/div/span[1]/hj-template/div/hj-dropdownlist/span").is_enabled()
            )
            clck1 = navegador.find_element(By.XPATH,
                                           "/html/body/div[1]/div[2]/div/div/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/div[2]/div[3]/div[1]/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/hj-template[1]/div/hj-field-table/div/hj-field-table-row/div/hj-field-group/div/div/hj-field-group-row[6]/div/hj-field-cell/div/hj-field-control/div/div/span[1]/hj-template/div/hj-dropdownlist/span")
            clck1.click()

            if tipo_ajuste == "1":
                motivo = WebDriverWait(navegador, 20).until(
                    lambda driver: driver.find_element(By.XPATH, "//li[text()='123 - AJ CONT EST ENTRADA']").is_displayed() and
                                   driver.find_element(By.XPATH, "//li[text()='123 - AJ CONT EST ENTRADA']").is_enabled()
                )

                motivo = navegador.find_element(By.XPATH, "//li[text()='123 - AJ CONT EST ENTRADA']")
                navegador.execute_script("arguments[0].click();", motivo)


            if tipo_ajuste == "2":

                motivo = WebDriverWait(navegador, 20).until(
                    lambda driver: driver.find_element(By.XPATH, "//li[text()='127 - AJ CONT EST SAIDA']").is_displayed() and
                                   driver.find_element(By.XPATH, "//li[text()='127 - AJ CONT EST SAIDA']").is_enabled()
                )
                motivo = navegador.find_element(By.XPATH,"//li[text()='127 - AJ CONT EST SAIDA']")
                navegador.execute_script("arguments[0].click();", motivo)

            cod_merc = WebDriverWait(navegador, 20).until(
                lambda driver: driver.find_element(By.XPATH,
                                                   "/html/body/div[1]/div[2]/div/div/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/div[2]/div[3]/div[1]/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/hj-template[1]/div/hj-field-table/div/hj-field-table-row/div/hj-field-group/div/div/hj-field-group-row[7]/div/hj-field-cell/div/hj-field-control/div/div/span[1]/hj-template/div/hj-textbox/input").is_displayed() and
                               driver.find_element(By.XPATH,
                                                   "/html/body/div[1]/div[2]/div/div/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/div[2]/div[3]/div[1]/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/hj-template[1]/div/hj-field-table/div/hj-field-table-row/div/hj-field-group/div/div/hj-field-group-row[7]/div/hj-field-cell/div/hj-field-control/div/div/span[1]/hj-template/div/hj-textbox/input").is_enabled()
            )
            cod_merc = navegador.find_element(By.XPATH,
                                              "/html/body/div[1]/div[2]/div/div/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/div[2]/div[3]/div[1]/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/hj-template[1]/div/hj-field-table/div/hj-field-table-row/div/hj-field-group/div/div/hj-field-group-row[7]/div/hj-field-cell/div/hj-field-control/div/div/span[1]/hj-template/div/hj-textbox/input")
            cod_merc.clear()
            cod_merc.send_keys(item)

            quantidade_ajuste = WebDriverWait(navegador, 20).until(
                lambda driver: driver.find_element(By.XPATH,
                                                   "/html/body/div[1]/div[2]/div/div/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/div[2]/div[3]/div[1]/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/hj-template[1]/div/hj-field-table/div/hj-field-table-row/div/hj-field-group/div/div/hj-field-group-row[9]/div/hj-field-cell/div/hj-field-control/div/div/span[1]/hj-template/div/hj-textbox/input").is_displayed() and
                               driver.find_element(By.XPATH,
                                                   "/html/body/div[1]/div[2]/div/div/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/div[2]/div[3]/div[1]/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/hj-template[1]/div/hj-field-table/div/hj-field-table-row/div/hj-field-group/div/div/hj-field-group-row[9]/div/hj-field-cell/div/hj-field-control/div/div/span[1]/hj-template/div/hj-textbox/input").is_enabled()
            )
            quantidade_ajuste = navegador.find_element(By.XPATH,
                                                       "/html/body/div[1]/div[2]/div/div/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/div[2]/div[3]/div[1]/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/hj-template[1]/div/hj-field-table/div/hj-field-table-row/div/hj-field-group/div/div/hj-field-group-row[9]/div/hj-field-cell/div/hj-field-control/div/div/span[1]/hj-template/div/hj-textbox/input")
            quantidade_ajuste.clear()
            quantidade_ajuste.send_keys(quantidade)

            custo = WebDriverWait(navegador, 20).until(
                lambda driver: driver.find_element(By.XPATH,
                                                   "/html/body/div[1]/div[2]/div/div/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/div[2]/div[3]/div[1]/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/hj-template[1]/div/hj-field-table/div/hj-field-table-row/div/hj-field-group/div/div/hj-field-group-row[11]/div/hj-field-cell/div/hj-field-control/div/div[1]/span[1]/hj-template/div/hj-dropdownlist/span").is_displayed() and
                               driver.find_element(By.XPATH,
                                                   "/html/body/div[1]/div[2]/div/div/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/div[2]/div[3]/div[1]/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/hj-template[1]/div/hj-field-table/div/hj-field-table-row/div/hj-field-group/div/div/hj-field-group-row[11]/div/hj-field-cell/div/hj-field-control/div/div[1]/span[1]/hj-template/div/hj-dropdownlist/span").is_enabled()
            )
            custo = navegador.find_element(By.XPATH,
                                           "/html/body/div[1]/div[2]/div/div/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/div[2]/div[3]/div[1]/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/hj-template[1]/div/hj-field-table/div/hj-field-table-row/div/hj-field-group/div/div/hj-field-group-row[11]/div/hj-field-cell/div/hj-field-control/div/div[1]/span[1]/hj-template/div/hj-dropdownlist/span")
            custo.click()

            if centro_custo == "1":
                custo_tipo = WebDriverWait(navegador, 20).until(
                    lambda driver: driver.find_element(By.XPATH, "//li[text()='30212 - Separação Carga Grossa']").is_displayed() and
                                   driver.find_element(By.XPATH, "//li[text()='30212 - Separação Carga Grossa']").is_enabled()
                )
                custo_tipo = navegador.find_element(By.XPATH, "//li[text()='30212 - Separação Carga Grossa']")
                custo_tipo.click()
            if centro_custo == "2":
                custo_tipo = WebDriverWait(navegador, 20).until(
                    lambda driver: driver.find_element(By.XPATH, "//li[text()='30213 - Separação Carga Fracionada']").is_displayed() and
                                   driver.find_element(By.XPATH, "//li[text()='30213 - Separação Carga Fracionada']").is_enabled()
                )
                custo_tipo = navegador.find_element(By.XPATH, "//li[text()='30213 - Separação Carga Fracionada']")
                custo_tipo.click()

            solicitante = WebDriverWait(navegador, 20).until(
                lambda driver: driver.find_element(By.XPATH,
                                                   "/html/body/div[1]/div[2]/div/div/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/div[2]/div[3]/div[1]/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/hj-template[1]/div/hj-field-table/div/hj-field-table-row/div/hj-field-group/div/div/hj-field-group-row[12]/div/hj-field-cell/div/hj-field-control/div/div[1]/span[1]/hj-template/div/hj-textbox/input").is_displayed() and
                               driver.find_element(By.XPATH,
                                                   "/html/body/div[1]/div[2]/div/div/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/div[2]/div[3]/div[1]/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/hj-template[1]/div/hj-field-table/div/hj-field-table-row/div/hj-field-group/div/div/hj-field-group-row[12]/div/hj-field-cell/div/hj-field-control/div/div[1]/span[1]/hj-template/div/hj-textbox/input").is_enabled()
            )
            solicitante = navegador.find_element(By.XPATH,
                                                 "/html/body/div[1]/div[2]/div/div/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/div[2]/div[3]/div[1]/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/hj-template[1]/div/hj-field-table/div/hj-field-table-row/div/hj-field-group/div/div/hj-field-group-row[12]/div/hj-field-cell/div/hj-field-control/div/div[1]/span[1]/hj-template/div/hj-textbox/input")
            solicitante.clear()
            solicitante.send_keys(matricula)

            obs = WebDriverWait(navegador, 20).until(
                lambda driver: driver.find_element(By.XPATH,
                                                   "/html/body/div[1]/div[2]/div/div/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/div[2]/div[3]/div[1]/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/hj-template[1]/div/hj-field-table/div/hj-field-table-row/div/hj-field-group/div/div/hj-field-group-row[13]/div/hj-field-cell/div/hj-field-control/div/div/span[1]/hj-template/div/hj-multiline-textbox/textarea").is_displayed() and
                               driver.find_element(By.XPATH,
                                                   "/html/body/div[1]/div[2]/div/div/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/div[2]/div[3]/div[1]/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/hj-template[1]/div/hj-field-table/div/hj-field-table-row/div/hj-field-group/div/div/hj-field-group-row[13]/div/hj-field-cell/div/hj-field-control/div/div/span[1]/hj-template/div/hj-multiline-textbox/textarea").is_enabled()
            )
            obs = navegador.find_element(By.XPATH,
                                         "/html/body/div[1]/div[2]/div/div/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/div[2]/div[3]/div[1]/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/hj-template[1]/div/hj-field-table/div/hj-field-table-row/div/hj-field-group/div/div/hj-field-group-row[13]/div/hj-field-cell/div/hj-field-control/div/div/span[1]/hj-template/div/hj-multiline-textbox/textarea")
            obs.clear()
            obs.send_keys(documento)

            incluir = WebDriverWait(navegador, 20).until(
                lambda driver: driver.find_element(By.LINK_TEXT,
                                                   "Incluir Pedido").is_displayed() and
                               driver.find_element(By.LINK_TEXT,
                                                   "Incluir Pedido").is_enabled()
            )
            incluir = navegador.find_element(By.LINK_TEXT,"Incluir Pedido")
            incluir.click()

            confirmar = WebDriverWait(navegador, 20).until(
                lambda driver: driver.find_element(By.LINK_TEXT,
                                                   "Confirmar Inclusão").is_displayed() and
                               driver.find_element(By.LINK_TEXT,
                                                   "Confirmar Inclusão").is_enabled()
            )
            confirmar = navegador.find_element(By.LINK_TEXT,"Confirmar Inclusão")
            confirmar.click()

            ok4 = WebDriverWait(navegador, 20).until(
                lambda driver: driver.find_element(By.CLASS_NAME, 'hj-dlg-button').is_displayed() and
                               driver.find_element(By.CLASS_NAME, 'hj-dlg-button').is_enabled()
            )
            ok4 = navegador.find_element(By.CLASS_NAME, 'hj-dlg-button')
            ok4.click()

            cont += 1

            porcentagem = (cont / len(itens)) * 100
            print(f"Confirmado com sucesso: {cont}/{len(itens)} ({porcentagem:.1f}%) - {item}")

            registrar_progresso(
                text=f"Item incluso: {item} Qtde: {quantidade} inclusa com sucesso no Documento: ",
                endereco=documento, sucesso=True)
        except:
            cont += 1

            porcentagem = (cont / len(itens)) * 100
            print(f"ERRO ao incluir: {cont}/{len(itens)} ({porcentagem:.1f}%) - {item}")

            registrar_progresso(
                text=f"Item incluso: {item} Qtde: {quantidade} Erro ao incluir no Documento: ",
                endereco=documento, sucesso=False)
    file_path.close()
    navegador.quit()
    cancelar_inputs()