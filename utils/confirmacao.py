from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
from utils.shared import historico_funcoes, registrar_progresso
from utils.retornar import cancelar_inputs
from utils.navegador import navegador_google
from time import sleep


def confirmacao_de_pedido_ajuste():
    from main import tabela

    historico_funcoes.append(tabela)
    print(f'''
    ╔════════════════════════════════════════════════════════╗
    ║       Confirmação de pedidos de ajustes contánil       ║
    ╚════════════════════════════════════════════════════════╝
    ''')

    data_inicial__ = input(f"Data inicial DD/MM/AAAA: ")
    data_final__ = input(f"Data final DD/MM/AAAA: ")

    matricula_ = input(f"\nMatricula do usuário solicitante:\n> ")

    centro_custo = input(f"Qual centro de custo [30212 / 30213]: ").strip()

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

        datas = WebDriverWait(navegador, 20).until(
            lambda driver: driver.find_element(By.CSS_SELECTOR, "input.k-input").is_displayed() and
                           driver.find_element(By.CSS_SELECTOR, "input.k-input").is_enabled()
        )

        datas = navegador.find_elements(By.CSS_SELECTOR, "input.k-input")
        conts = 0

        numerador = 0
        for dt in datas:
            numerador += 1
            if numerador == 1:
                dt.clear()
                dt.send_keys(f"{data_inicial__}")
            if numerador == 2:
                dt.clear()
                dt.send_keys(f"{data_final__}")

        consultar = WebDriverWait(navegador, 20).until(
            lambda driver: driver.find_element(By.LINK_TEXT, 'Consulta').is_displayed() and
                           driver.find_element(By.LINK_TEXT, 'Consulta').is_enabled()
        )
        consultar = navegador.find_element(By.LINK_TEXT, 'Consulta')
        consultar.click()
    except:
        print(f"Erro ao acessar Fechamento de pedido de ajuste!!!\n")
        try:
            navegador.quit()
        except:
            pass
        return cancelar_inputs()

    try:
        file_path = 'Banco de dados.xlsx'
        file_path = pd.ExcelFile(file_path)
        file_path.sheet_names

        sheet_data = file_path.parse('Confirmação de ajuste Contabil')
        sheet_data.head()
        itens = sheet_data['Itens']
    except:
        print(f"Erro  ao acessar o arquivo Banco de dados.xlsx!!!")
        try:
            navegador.quit()
        except:
            pass
        return cancelar_inputs()

    for item in itens:
        try:
            sleep(3)
            if cont == 0:
                filtro = WebDriverWait(navegador, 40).until(
                    lambda driver: driver.find_element(By.CSS_SELECTOR,
                                                    'th[data-title="Cód. Merc."] a.k-header-column-menu span.k-icon.k-i-more-vertical').is_displayed() and
                                driver.find_element(By.CSS_SELECTOR,
                                                    'th[data-title="Cód. Merc."] a.k-header-column-menu span.k-icon.k-i-more-vertical').is_enabled()
                )
                filtro = navegador.find_element(By.CSS_SELECTOR,
                                                'th[data-title="Cód. Merc."] a.k-header-column-menu span.k-icon.k-i-more-vertical')
                filtro.click()
            else:
                filtro = WebDriverWait(navegador, 40).until(
                    lambda driver: driver.find_element(By.CSS_SELECTOR,
                                                    'th[data-title="Cód. Merc."] a.k-header-column-menu span.k-icon.k-i-filter').is_displayed() and
                                driver.find_element(By.CSS_SELECTOR,
                                                    'th[data-title="Cód. Merc."] a.k-header-column-menu span.k-icon.k-i-filter').is_enabled()
                )
                filtro = navegador.find_element(By.CSS_SELECTOR,
                                                'th[data-title="Cód. Merc."] a.k-header-column-menu span.k-icon.k-i-filter')
                filtro.click()
        
            sleep(1)

            filtro_menu = WebDriverWait(navegador, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "li.k-filter-item span.k-link"))
            )
            filtro_menu.click()

            sleep(1)
            texto_para_inserir = item
            navegador.execute_script("""
                var campo = document.querySelector("input[data-bind='value:filters[0].value']");
                campo.value = arguments[0];
                campo.dispatchEvent(new Event('input', { bubbles: true }));
                campo.dispatchEvent(new Event('change', { bubbles: true }));
            """, texto_para_inserir)
            sleep(0.5)

            filter_cl = WebDriverWait(navegador, 20).until(
                lambda driver: driver.find_element(By.CSS_SELECTOR, 'button.k-button').is_displayed() and
                               driver.find_element(By.CSS_SELECTOR, 'button.k-button').is_enabled()
            )
            filter_cl = navegador.find_element(By.CSS_SELECTOR, 'button.k-button')
            filter_cl.click()
            sleep(2)
            contat = 0
            while True:
                try:
                    aberto = navegador.find_element(By.LINK_TEXT, "Aberto")
                    aberto.click()
                    break
                except:
                    contat += 1
                    if contat == 10:
                        break
                    sleep(1)
                    pass

            sleep(0.5)

            xpath_input_matricula = (
                '/html/body/div[1]/div[2]/div/div/div/hj-flex-container/div/hj-flex-grow/div/'
                'hj-flex-scroll/div/div[2]/div[3]/div[1]/div/hj-flex-container/div/hj-flex-grow/'
                'div/hj-flex-scroll/div/hj-template[1]/div/hj-field-table/div/hj-field-table-row/'
                'div/hj-field-group/div/div/hj-field-group-row[11]/div/hj-field-cell/div/'
                'hj-field-control/div/div/span[1]/hj-template/div/hj-textbox/input'
            )

            elemento_input = WebDriverWait(navegador, 20).until(
                EC.element_to_be_clickable((By.XPATH, xpath_input_matricula))
            )

            elemento_input.clear()
            elemento_input.send_keys(matricula_)

            sleep(0.5)
            xpath_input = (
                '/html/body/div[1]/div[2]/div/div/div/hj-flex-container/div/hj-flex-grow/div/'
                'hj-flex-scroll/div/div[2]/div[3]/div[1]/div/hj-flex-container/div/hj-flex-grow/'
                'div/hj-flex-scroll/div/hj-template[1]/div/hj-field-table/div/hj-field-table-row/'
                'div/hj-field-group/div/div/hj-field-group-row[12]/div/hj-field-cell/div/'
                'hj-field-control/div/div/span[1]/hj-template/div/hj-textbox/input'
            )

            elemento_input2 = WebDriverWait(navegador, 20).until(
                EC.element_to_be_clickable((By.XPATH, xpath_input))
            )

            elemento_input2.clear()
            elemento_input2.send_keys(matricula_)

            sleep(0.5)


            if centro_custo == "30213":
                custo = WebDriverWait(navegador, 20).until(
                    lambda driver: driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/div[2]/div[3]/div[1]/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/hj-template[1]/div/hj-field-table/div/hj-field-table-row/div/hj-field-group/div/div/hj-field-group-row[10]/div/hj-field-cell/div/hj-field-control/div/div/span[1]/hj-template/div/hj-dropdownlist/span/span/span[1]').is_displayed() and
                                   driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/div[2]/div[3]/div[1]/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/hj-template[1]/div/hj-field-table/div/hj-field-table-row/div/hj-field-group/div/div/hj-field-group-row[10]/div/hj-field-cell/div/hj-field-control/div/div/span[1]/hj-template/div/hj-dropdownlist/span/span/span[1]').is_enabled()
                )
                custo = navegador.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/div[2]/div[3]/div[1]/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/hj-template[1]/div/hj-field-table/div/hj-field-table-row/div/hj-field-group/div/div/hj-field-group-row[10]/div/hj-field-cell/div/hj-field-control/div/div/span[1]/hj-template/div/hj-dropdownlist/span/span/span[1]')
                custo.click()


                sleep(0.5)

                custo_tipo = WebDriverWait(navegador, 20).until(
                    lambda driver: driver.find_element(By.XPATH,
                                                       "//li[text()='30213 - Separação Carga Fracionada']").is_displayed() and
                                   driver.find_element(By.XPATH,
                                                       "//li[text()='30213 - Separação Carga Fracionada']").is_enabled()
                )
                custo_tipo = navegador.find_element(By.XPATH, "//li[text()='30213 - Separação Carga Fracionada']")
                custo_tipo.click()

                sleep(0.5)

            fechar_pedido = WebDriverWait(navegador, 5).until(
                lambda driver: driver.find_element(By.LINK_TEXT, 'Fechar Pedido de Ajuste').is_displayed() and
                               driver.find_element(By.LINK_TEXT, 'Fechar Pedido de Ajuste').is_enabled()
            )
            fechar_pedido = navegador.find_element(By.LINK_TEXT, 'Fechar Pedido de Ajuste')
            fechar_pedido.click()

            while True:
                elements = navegador.find_elements(By.CSS_SELECTOR, 'button.k-button.primary')
                if elements:
                    descartar = WebDriverWait(navegador, 5).until(
                        lambda driver: driver.find_element(By.CSS_SELECTOR, 'button.k-button.primary').is_displayed() and
                                       driver.find_element(By.CSS_SELECTOR, 'button.k-button.primary').is_enabled()
                    )
                    descartar = navegador.find_element(By.CSS_SELECTOR, 'button.k-button.primary')
                    descartar.click()

                    voltar2_ = WebDriverWait(navegador, 20).until(
                        lambda driver: driver.find_element(By.CSS_SELECTOR,
                                                           "a[data-hj-test-id='active-thread-previous-button']").is_displayed() and
                                       driver.find_element(By.CSS_SELECTOR,
                                                           "a[data-hj-test-id='active-thread-previous-button']").is_enabled()
                    )
                    voltar2_ = navegador.find_element(By.CSS_SELECTOR,
                                                      "a[data-hj-test-id='active-thread-previous-button']")
                    voltar2_.click()
                    cont += 1

                    print(
                        f"[{cont}] -> [{item}] - ITEM FORA DO MIX [Erro]!!!")
                    registrar_progresso(
                        text=f"Confirmado com ERRO [Fora do Mix]: ",
                        endereco=item, sucesso=True)

                    break
                else:
                    try:
                        fechar_pedido_2 = WebDriverWait(navegador, 20).until(
                            lambda driver: driver.find_element(By.LINK_TEXT, 'Fechar Pedido de Ajuste').is_displayed() and
                                           driver.find_element(By.LINK_TEXT, 'Fechar Pedido de Ajuste').is_enabled()
                        )
                        fechar_pedido_2 = navegador.find_element(By.LINK_TEXT, 'Fechar Pedido de Ajuste')
                        fechar_pedido_2.click()

                        conclusao = WebDriverWait(navegador, 20).until(
                            lambda driver: driver.find_element(By.XPATH,
                                                               '/html/body/div[1]/div[2]/hj-information-dialog/div/div/hj-flex-container/div/hj-flex-shrink[2]/div/div/hj-button/button').is_displayed() and
                                           driver.find_element(By.XPATH,
                                                               '/html/body/div[1]/div[2]/hj-information-dialog/div/div/hj-flex-container/div/hj-flex-shrink[2]/div/div/hj-button/button').is_enabled()
                        )
                        conclusao = navegador.find_element(By.XPATH,
                                                           '/html/body/div[1]/div[2]/hj-information-dialog/div/div/hj-flex-container/div/hj-flex-shrink[2]/div/div/hj-button/button')
                        conclusao.click()
                        cont += 1

                        porcentagem = (cont / len(itens)) * 100
                        print(f"Confirmado com sucesso: {cont}/{len(itens)} ({porcentagem:.1f}%) - {item}")

                        registrar_progresso(
                            text=f"Confirmado com sucesso: ",
                            endereco=item, sucesso=True)
                        break
                    except:
                        sleep(0.5)
                        pass
        except Exception as e:
            conts += 1

            porcentagem = (cont / len(itens)) * 100
            print(f"Confirmado com Erro: {cont}/{len(itens)} ({porcentagem:.1f}%) - {item}")

            registrar_progresso(
                text=f"Erro ao confirmar: ",
                endereco=item, sucesso=False)
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
                    lambda driver: driver.find_element(By.LINK_TEXT,
                                                       'Confirmação de AJUSTE CONTÁBIL').is_displayed() and
                                   driver.find_element(By.LINK_TEXT, 'Confirmação de AJUSTE CONTÁBIL').is_enabled()
                )
                confirmacao = navegador.find_element(By.LINK_TEXT, 'Confirmação de AJUSTE CONTÁBIL')
                confirmacao.click()

                datas = WebDriverWait(navegador, 20).until(
                    lambda driver: driver.find_element(By.CSS_SELECTOR, "input.k-input").is_displayed() and
                                   driver.find_element(By.CSS_SELECTOR, "input.k-input").is_enabled()
                )

                datas = navegador.find_elements(By.CSS_SELECTOR, "input.k-input")

                numerador = 0
                for dt in datas:
                    numerador += 1
                    if numerador == 1:
                        dt.clear()
                        dt.send_keys(f"{data_inicial__}")
                    if numerador == 2:
                        dt.clear()
                        dt.send_keys(f"{data_final__}")

                consultar = WebDriverWait(navegador, 20).until(
                    lambda driver: driver.find_element(By.LINK_TEXT, 'Consulta').is_displayed() and
                                   driver.find_element(By.LINK_TEXT, 'Consulta').is_enabled()
                )
                consultar = navegador.find_element(By.LINK_TEXT, 'Consulta')
                consultar.click()
            except:
                print(f"Erro ao acessar Fechamento de pedido de ajuste!!!\n")
                try:
                    navegador.quit()
                except:
                    pass
                return cancelar_inputs()
            
    file_path.close()
    navegador.quit()
    cancelar_inputs()
