from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import pandas as pd
from utils.shared import historico_funcoes, registrar_progresso
from utils.retornar import cancelar_inputs
from utils.navegador import navegador_google

def fechar_com_divergencia():
    from main import tabela

    historico_funcoes.append(tabela)
    print(f'''
    ╔════════════════════════════════════════════════════════╗
    ║           Fechamento de ordens com divergência         ║
    ╚════════════════════════════════════════════════════════╝
    ''')
    print(f"\n[F8] Para voltar ao menu principal\n")
    try:
        while True:
            matricula = int(input(f"Matrícula do colaborador responsável: "))
            if matricula > 999:
                break
            else:
                print(f"Escreva uma Matrícula válida!!")
    except Exception:
        print(f"Escreva uma Matrícula válida!!")
        return cancelar_inputs

    try:
        navegador = navegador_google()

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

        manutemcao = WebDriverWait(navegador, 20).until(
            lambda driver: driver.find_element(By.LINK_TEXT, 'Manutenção Ordens').is_displayed() and
                           driver.find_element(By.LINK_TEXT, 'Manutenção Ordens').is_enabled()
        )
        manutemcao = navegador.find_element(By.LINK_TEXT, 'Manutenção Ordens')
        manutemcao.click()

        diverge = WebDriverWait(navegador, 20).until(
            lambda driver: driver.find_element(By.LINK_TEXT, 'Fechamento Ordem c/ DIVERGÊNCIA').is_displayed() and
                           driver.find_element(By.LINK_TEXT, 'Fechamento Ordem c/ DIVERGÊNCIA').is_enabled()
        )
        diverge = navegador.find_element(By.LINK_TEXT, 'Fechamento Ordem c/ DIVERGÊNCIA')
        diverge.click()
    except:
        print(f"Erro ao acessar Fechamento de Ordem c/ DIVERGÊNCIA!!!\n")
        try:
            navegador.quit()
        except:
            pass
        return cancelar_inputs()

    try:
        file_path = 'Banco de dados.xlsx'
        file_path = pd.ExcelFile(file_path)
        file_path.sheet_names

        sheet_data = file_path.parse('Fechamento com divergência')
        sheet_data.head()
        ordens = sheet_data['Ordens'].astype(str).str.replace(r'\.0$', '', regex=True)

    except:
        print(f"Erro  ao acessar o arquivo Banco de dados.xlsx!!!")
        try:
            navegador.quit()
        except:
            pass
        return cancelar_inputs()

    cont = 0

    for ordem in ordens:
        nrordem = WebDriverWait(navegador, 20).until(
            lambda driver: driver.find_element(By.CSS_SELECTOR, 'input.k-textbox').is_displayed() and
                           driver.find_element(By.CSS_SELECTOR, 'input.k-textbox').is_enabled()
        )
        nrordem = navegador.find_element(By.CSS_SELECTOR, 'input.k-textbox')

        nrordem.clear()
        nrordem.send_keys(ordem)

        consultar = WebDriverWait(navegador, 20).until(
            lambda driver: driver.find_element(By.LINK_TEXT, 'Consultar').is_displayed() and
                           driver.find_element(By.LINK_TEXT, 'Consultar').is_enabled()
        )
        consultar = navegador.find_element(By.LINK_TEXT, 'Consultar')
        consultar.click()

        try:
            fechar = WebDriverWait(navegador, 5).until(
                lambda driver: driver.find_element(By.LINK_TEXT, 'Fechar').is_displayed() and
                               driver.find_element(By.LINK_TEXT, 'Fechar').is_enabled()
            )
            fechar = navegador.find_element(By.LINK_TEXT, 'Fechar')
            fechar.click()

            fechar_ordem = WebDriverWait(navegador, 20).until(
                lambda driver: driver.find_element(By.LINK_TEXT, "Fechar Ordem").is_displayed() and
                               driver.find_element(By.LINK_TEXT, "Fechar Ordem").is_enabled()
            )
            fechar_ordem = navegador.find_element(By.LINK_TEXT, "Fechar Ordem")
            fechar_ordem.click()

            primeiro_campo = WebDriverWait(navegador, 20).until(
                lambda driver: driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/div[2]/div[4]/div[1]/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/hj-template/div/hj-field-table/div/hj-field-table-row/div/hj-field-group/div/div/hj-field-group-row[3]/div/hj-field-cell/div/hj-field-control/div/div/span[1]/hj-template/div/hj-textbox/input").is_displayed() and
                               driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/div[2]/div[4]/div[1]/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/hj-template/div/hj-field-table/div/hj-field-table-row/div/hj-field-group/div/div/hj-field-group-row[3]/div/hj-field-cell/div/hj-field-control/div/div/span[1]/hj-template/div/hj-textbox/input").is_enabled()
            )
            primeiro_campo = navegador.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/div[2]/div[4]/div[1]/div/hj-flex-container/div/hj-flex-grow/div/hj-flex-scroll/div/hj-template/div/hj-field-table/div/hj-field-table-row/div/hj-field-group/div/div/hj-field-group-row[3]/div/hj-field-cell/div/hj-field-control/div/div/span[1]/hj-template/div/hj-textbox/input")

            primeiro_campo.clear()
            primeiro_campo.send_keys(f'{matricula}')


            fechar_recebi = WebDriverWait(navegador, 20).until(
                lambda driver: driver.find_element(By.LINK_TEXT, "Fechar Recebimento").is_displayed() and
                               driver.find_element(By.LINK_TEXT, "Fechar Recebimento").is_enabled()
            )
            fechar_recebi = navegador.find_element(By.LINK_TEXT, "Fechar Recebimento")
            fechar_recebi.click()

            ok = WebDriverWait(navegador, 20).until(
                lambda driver: driver.find_element(By.CSS_SELECTOR, "button.k-button").is_displayed() and
                               driver.find_element(By.CSS_SELECTOR, "button.k-button").is_enabled()
            )
            ok = navegador.find_element(By.CSS_SELECTOR, "button.k-button")
            ok.click()

            voltar = WebDriverWait(navegador, 20).until(
                lambda driver: driver.find_element(By.XPATH,
                                                   "/html/body/div[1]/div[2]/div/div/div/hj-flex-container/div/hj-flex-shrink/div/div/div[1]/a[1]/span/i[2]").is_displayed() and
                               driver.find_element(By.XPATH,
                                                   "/html/body/div[1]/div[2]/div/div/div/hj-flex-container/div/hj-flex-shrink/div/div/div[1]/a[1]/span/i[2]").is_enabled()
            )
            voltar = navegador.find_element(By.XPATH,
                                            "/html/body/div[1]/div[2]/div/div/div/hj-flex-container/div/hj-flex-shrink/div/div/div[1]/a[1]/span/i[2]")
            voltar.click()

            registrar_progresso(text="Ordem fechada com sucesso: ", endereco=ordem, sucesso=True)
            cont += 1
            porcentagem = (cont / len(ordens)) * 100
            print(f"Item {cont}/{len(ordens)} ({porcentagem:.1f}%) - {ordem}")
        except:
            cont += 1
            print(
                f"Senha [{ordem}] Já finalizada ou impossibilidade de fechamento!! [{cont}]")
            registrar_progresso(text="Ordem não finalizada: ", endereco=ordem, sucesso=False)
            while True:
                try:
                    voltar = WebDriverWait(navegador, 20).until(
                        lambda driver: driver.find_element(By.CSS_SELECTOR, "a[data-hj-test-id='active-thread-previous-button']").is_displayed() and
                                    driver.find_element(By.CSS_SELECTOR, "a[data-hj-test-id='active-thread-previous-button']").is_enabled()
                    )
                    voltar = navegador.find_element(By.CSS_SELECTOR, "a[data-hj-test-id='active-thread-previous-button']")
                    voltar.click()
                except:
                    break
    file_path.close()
    try:
        navegador.quit()
    except:
        pass
    cancelar_inputs()