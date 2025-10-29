from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
from utils.shared import historico_funcoes, registrar_progresso
from utils.retornar import cancelar_inputs
from utils.navegador import navegador_google
from time import sleep


def Cancelamento_de_pedido_de_ajuste_contabil():
    from main import tabela

    historico_funcoes.append(tabela)
    print(f'''
    ╔════════════════════════════════════════════════════════╗
    ║       Cancelamento de pedido de ajuste contábil        ║
    ╚════════════════════════════════════════════════════════╝
    ''')
    print(f"\n[F8] Para voltar ao menu principal\n")

    matricula = input(f"Matrícula do colaborador responsável: ")
    print(
        f''''Para melhor adptação ao WMS Digitar a DATA [exemplo]: 01/01/1999''',
        1)
    data_inicial_ = input(f"Data inicial DD/MM/AAAA: ")
    data_final_ = input(f"Data final DD/MM/AAAA: ")

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

        cancelamento_p = WebDriverWait(navegador, 20).until(
            lambda driver: driver.find_element(By.LINK_TEXT, 'CANCELAMENTO Pedidos Ajustes').is_displayed() and
                           driver.find_element(By.LINK_TEXT, 'CANCELAMENTO Pedidos Ajustes').is_enabled()
        )
        cancelamento_p = navegador.find_element(By.LINK_TEXT, 'CANCELAMENTO Pedidos Ajustes')
        cancelamento_p.click()

        cancelamento_Ajuste = WebDriverWait(navegador, 20).until(
            lambda driver: driver.find_element(By.LINK_TEXT, 'Cancelamento de AJUSTE CONTÁBIL').is_displayed() and
                           driver.find_element(By.LINK_TEXT, 'Cancelamento de AJUSTE CONTÁBIL').is_enabled()
        )
        cancelamento_Ajuste = navegador.find_element(By.LINK_TEXT, 'Cancelamento de AJUSTE CONTÁBIL')
        cancelamento_Ajuste.click()
    except:
        print(f"Erro ao acessar Cancelamento de AJUSTE CONTÁBIL!!!\n")
        try:
            navegador.quit()
        except:
            pass
        return cancelar_inputs()

    try:
        data_inicial = WebDriverWait(navegador, 20).until(
            lambda driver: driver.find_element(By.CSS_SELECTOR, 'input.k-input').is_displayed() and
                           driver.find_element(By.CSS_SELECTOR, 'input.k-input').is_enabled()
        )
        data_inicial = navegador.find_elements(By.CSS_SELECTOR, 'input.k-input')
        data_inicial[0].clear()
        data_inicial[0].send_keys(f'{data_inicial_}')

        data_final = WebDriverWait(navegador, 20).until(
            lambda driver: driver.find_element(By.CSS_SELECTOR, 'input.k-input').is_displayed() and
                           driver.find_element(By.CSS_SELECTOR, 'input.k-input').is_enabled()
        )
        data_final = navegador.find_elements(By.CSS_SELECTOR, 'input.k-input')
        data_final[1].clear()
        data_final[1].send_keys(f'{data_final_}')

        consultar = WebDriverWait(navegador, 20).until(
            lambda driver: driver.find_element(By.LINK_TEXT, 'Consulta').is_displayed() and
                           driver.find_element(By.LINK_TEXT, 'Consulta').is_enabled()
        )
        consultar = navegador.find_element(By.LINK_TEXT, 'Consulta')
        cont = 0
        consultar.click()
    except:
        print(f"Erro ao conultar o valor desejado!!!\n")
        try:
            navegador.quit()
        except:
            pass
        return cancelar_inputs()

    try:
        file_path = 'Banco de dados.xlsx'
        file_path = pd.ExcelFile(file_path)
        file_path.sheet_names

        sheet_data = file_path.parse('Cancelamento de ajuste Contabil')
        sheet_data.head()
        itens = sheet_data['Itens']
        motivos = sheet_data['MOTIVO']
    except:
        print(f"Erro  ao acessar o arquivo Banco de dados.xlsx!!!")
        try:
            navegador.quit()
        except:
            pass
        return cancelar_inputs()

    for item, motivos_ in zip(itens, motivos):
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

            matricula_3 = WebDriverWait(navegador, 5).until(
                lambda driver: driver.find_element(By.XPATH,
                                                   '/html/body/div[1]/div[2]/div/div/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/div[2]/div[3]/div[1]/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/hj-template[1]/div/hj-field-table/div/hj-field-table-row/div/hj-field-group/div/div/hj-field-group-row[11]/div/hj-field-cell/div/hj-field-control/div/div/span[1]/hj-template/div/hj-textbox/input').is_displayed() and
                               driver.find_element(By.XPATH,
                                                   '/html/body/div[1]/div[2]/div/div/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/div[2]/div[3]/div[1]/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/hj-template[1]/div/hj-field-table/div/hj-field-table-row/div/hj-field-group/div/div/hj-field-group-row[11]/div/hj-field-cell/div/hj-field-control/div/div/span[1]/hj-template/div/hj-textbox/input').is_enabled()
            )
            matricula_3 = navegador.find_element(By.XPATH,
                                               '/html/body/div[1]/div[2]/div/div/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/div[2]/div[3]/div[1]/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/hj-template[1]/div/hj-field-table/div/hj-field-table-row/div/hj-field-group/div/div/hj-field-group-row[11]/div/hj-field-cell/div/hj-field-control/div/div/span[1]/hj-template/div/hj-textbox/input')
            matricula_3.clear()
            matricula_3.send_keys(matricula)

            matricula_2 = WebDriverWait(navegador, 20).until(
                lambda driver: driver.find_element(By.XPATH,
                                                   '/html/body/div[1]/div[2]/div/div/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/div[2]/div[3]/div[1]/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/hj-template[1]/div/hj-field-table/div/hj-field-table-row/div/hj-field-group/div/div/hj-field-group-row[12]/div/hj-field-cell/div/hj-field-control/div/div/span[1]/hj-template/div/hj-textbox/input').is_displayed() and
                               driver.find_element(By.XPATH,
                                                   '/html/body/div[1]/div[2]/div/div/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/div[2]/div[3]/div[1]/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/hj-template[1]/div/hj-field-table/div/hj-field-table-row/div/hj-field-group/div/div/hj-field-group-row[12]/div/hj-field-cell/div/hj-field-control/div/div/span[1]/hj-template/div/hj-textbox/input').is_enabled()
            )
            matricula_2 = navegador.find_element(By.XPATH,
                                                 '/html/body/div[1]/div[2]/div/div/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/div[2]/div[3]/div[1]/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/hj-template[1]/div/hj-field-table/div/hj-field-table-row/div/hj-field-group/div/div/hj-field-group-row[12]/div/hj-field-cell/div/hj-field-control/div/div/span[1]/hj-template/div/hj-textbox/input')
            matricula_2.clear()
            matricula_2.send_keys(matricula)

            desbloqueio = WebDriverWait(navegador, 20).until(
                lambda driver: driver.find_element(By.XPATH,
                                                   '/html/body/div[1]/div[2]/div/div/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/div[2]/div[3]/div[1]/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/hj-template[1]/div/hj-field-table/div/hj-field-table-row/div/hj-field-group/div/div/hj-field-group-row[14]/div/hj-field-cell/div/hj-field-control/div/div/span[1]/hj-template/div/hj-dropdownlist/span/span/span[1]').is_displayed() and
                               driver.find_element(By.XPATH,
                                                   '/html/body/div[1]/div[2]/div/div/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/div[2]/div[3]/div[1]/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/hj-template[1]/div/hj-field-table/div/hj-field-table-row/div/hj-field-group/div/div/hj-field-group-row[14]/div/hj-field-cell/div/hj-field-control/div/div/span[1]/hj-template/div/hj-dropdownlist/span/span/span[1]').is_enabled()
            )
            desbloqueio = navegador.find_element(By.XPATH,
                                                 '/html/body/div[1]/div[2]/div/div/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/div[2]/div[3]/div[1]/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/hj-template[1]/div/hj-field-table/div/hj-field-table-row/div/hj-field-group/div/div/hj-field-group-row[14]/div/hj-field-cell/div/hj-field-control/div/div/span[1]/hj-template/div/hj-dropdownlist/span/span/span[1]')
            desbloqueio.click()

            option = navegador.find_elements(By.CSS_SELECTOR, 'li.k-item')

            for opcao in option:
                if "Nao" == opcao.text:
                    opcao.click()
                    break

            motivo_2 = WebDriverWait(navegador, 20).until(
                lambda driver: driver.find_element(By.XPATH,
                                                   '/html/body/div[1]/div[2]/div/div/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/div[2]/div[3]/div[1]/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/hj-template[1]/div/hj-field-table/div/hj-field-table-row/div/hj-field-group/div/div/hj-field-group-row[16]/div/hj-field-cell/div/hj-field-control/div/div/span[1]/hj-template/div/hj-dropdownlist/span/span/span[1]').is_displayed() and
                               driver.find_element(By.XPATH,
                                                   '/html/body/div[1]/div[2]/div/div/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/div[2]/div[3]/div[1]/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/hj-template[1]/div/hj-field-table/div/hj-field-table-row/div/hj-field-group/div/div/hj-field-group-row[16]/div/hj-field-cell/div/hj-field-control/div/div/span[1]/hj-template/div/hj-dropdownlist/span/span/span[1]').is_enabled()
            )
            motivo_2 = navegador.find_element(By.XPATH,
                                              '/html/body/div[1]/div[2]/div/div/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/div[2]/div[3]/div[1]/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/hj-template[1]/div/hj-field-table/div/hj-field-table-row/div/hj-field-group/div/div/hj-field-group-row[16]/div/hj-field-cell/div/hj-field-control/div/div/span[1]/hj-template/div/hj-dropdownlist/span/span/span[1]')
            motivo_2.click()

            motivos = navegador.find_elements(
                By.CSS_SELECTOR,
                'li.k-item'
            )
            for motivo in motivos:
                if 100 == motivos_:
                    if '100 - Divergência encontrada' == motivo.accessible_name:
                        motivo.click()
                        break
                if 3 == motivos_:
                    if '3 - Erro de Movimentação SME' == motivo.accessible_name:
                        motivo.click()
                        break
                if 2 == motivos_:
                    if '2 - Erro de Movimentação' == motivo.accessible_name:
                        motivo.click()
                        break

            cancelar_pedido = WebDriverWait(navegador, 20).until(
                lambda driver: driver.find_element(By.LINK_TEXT,
                                                   'Cancelar Pedido de Ajuste').is_displayed() and
                               driver.find_element(By.LINK_TEXT, 'Cancelar Pedido de Ajuste').is_enabled()
            )
            cancelar_pedido = navegador.find_element(By.LINK_TEXT, 'Cancelar Pedido de Ajuste')
            cancelar_pedido.click()

            while True:
                try:
                    cancelar_pedido = WebDriverWait(navegador, 20).until(
                        lambda driver: driver.find_element(By.LINK_TEXT,
                                                           'Cancelar Pedido de Ajuste').is_displayed() and
                                       driver.find_element(By.LINK_TEXT, 'Cancelar Pedido de Ajuste').is_enabled()
                    )
                    cancelar_pedido = navegador.find_element(By.LINK_TEXT, 'Cancelar Pedido de Ajuste')
                    cancelar_pedido.click()
                    break
                except:
                    sleep(0.5)
                    pass

            while True:
                try:
                    ok4 = WebDriverWait(navegador, 20).until(
                        lambda driver: driver.find_element(By.CLASS_NAME, 'hj-dlg-button').is_displayed() and
                                       driver.find_element(By.CLASS_NAME, 'hj-dlg-button').is_enabled()
                    )
                    ok4 = navegador.find_element(By.CLASS_NAME, 'hj-dlg-button')
                    ok4.click()
                    break
                except:
                    pass
                
            cont += 1
            porcentagem = (cont / len(itens)) * 100
            
            if motivos_ == 100:
                print(f"Cancelado com sucesso: {cont}/{len(itens)} ({porcentagem:.1f}%) - {item} - [100 - Divergência encontrada]")
                registrar_progresso(text="Ordem cancelada com sucesso no 100 - Divergência encontrada: ", endereco=item, sucesso=True)
            elif motivos_ == 3:
                print(f"Cancelado com sucesso: {cont}/{len(itens)} ({porcentagem:.1f}%) - {item} - [3 - Erro de Movimentação SME]")
                registrar_progresso(text="Ordem cancelada com sucesso no 3 - Erro de Movimentação SME: ",
                                    endereco=item, sucesso=True)
            elif motivos_ == 2:
                print(f"Cancelado com sucesso: {cont}/{len(itens)} ({porcentagem:.1f}%) - {item} - [2 - Erro de Movimentação]")
                registrar_progresso(text="Ordem cancelada com sucesso no 2 - Erro de Movimentação: ",
                                    endereco=item, sucesso=True)

        except:
            cor_erro = "\033[91m"
            reset = "\033[0m"
            
            cont += 1
            porcentagem = (cont / len(itens)) * 100
            
            if motivos_ == 100:
                print(f"{cor_erro}Erro ao cancelar: {cont}/{len(itens)} ({porcentagem:.1f}%) - {item} - [100 - Divergência encontrada]{reset}")
                registrar_progresso(text="Ordem erro ao cancelar no 100 - Divergência encontrada: ",
                                    endereco=item, sucesso=False)
            elif motivos_ == 3:
                print(f"{cor_erro}Erro ao cancelar: {cont}/{len(itens)} ({porcentagem:.1f}%) - {item} - [3 - Erro de Movimentação SME]{reset}")
                registrar_progresso(text="Ordem erro ao cancelar no 3 - Erro de Movimentação SME: ",
                                    endereco=item, sucesso=False)
            elif motivos_ == 2:
                print(f"{cor_erro}Erro ao cancelar: {cont}/{len(itens)} ({porcentagem:.1f}%) - {item} - [2 - Erro de Movimentação]{reset}")
                registrar_progresso(text="Ordem erro ao cancelar no 2 - Erro de Movimentação: ",
                                    endereco=item, sucesso=False)
                
    file_path.close()
    try:
        navegador.quit()
    except:
        pass
    cancelar_inputs()