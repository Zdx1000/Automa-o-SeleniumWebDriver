from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import pandas as pd
from utils.retornar import cancelar_inputs
from utils.navegador import navegador_google
from utils.shared import historico_funcoes, registrar_progresso
from time import sleep
from utils.wms_selenium import WmsSelenium

def Lote():

    print(f'''
    ╔════════════════════════════════════════════════════════╗
    ║       Implementação de data de validade e lote         ║
    ╚════════════════════════════════════════════════════════╝
    ''')
    from main import tabela
    historico_funcoes.append(tabela)

    try:
        navegador = navegador_google()
    except:
        try:
            navegador.quit()
        except:
            pass
        return cancelar_inputs()
    cont = 0

    wms = WmsSelenium(navegador)

    wms.login_suplay()

    wms.selenium_click(By.LINK_TEXT, 'Warehouse Advantage', 20)

    wms.selenium_click(By.LINK_TEXT, 'Configuração Armazém', 20)

    wms.selenium_click(By.LINK_TEXT, 'Itens', 20)

    wms.selenium_click_element(By.LINK_TEXT, 'Itens', 1)

    try:
        file_path = 'Banco de dados.xlsx'
        file_path = pd.ExcelFile(file_path)
        file_path.sheet_names

        sheet_data = file_path.parse('Lote')
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

        wms.selenium_send_keys(By.CSS_SELECTOR, 'input.k-textbox', f'{item}', 20)

        wms.selenium_click(By.LINK_TEXT, 'Consulta', 20)

        wms.selenium_click(By.CSS_SELECTOR, 'a.hj-link', 20)

        sleep(1.5)

        controle_expiracao = WebDriverWait(navegador, 20).until(
            lambda driver: driver.find_element(By.XPATH, "//span[contains(text(), 'Controle Data Expiração')]")
        )
        navegador.execute_script("arguments[0].scrollIntoView({block: 'center'});", controle_expiracao)

        sleep(1)

        validador_lote = navegador.find_elements(By.CSS_SELECTOR, "span.k-input")

        if validador_lote[6].text == 'Somente Armazenagem':
            print("Item com controle de lote já Ativando...")
        else:
            validador_lote[6].click()
            ativador_lote = navegador.find_elements(By.CSS_SELECTOR, "li.k-item")

            for option in ativador_lote:
                if option.text == "Somente Armazenagem":
                    option.click()
                    break
        
        if validador_lote[7].text == 'Sim':
            print("Item com controle de data já Ativando...")
        else:
            validador_lote[7].click()
            ativador_data = navegador.find_elements(By.CSS_SELECTOR, "li.k-item")

            for option in ativador_data:
                if option.text == "Sim":
                    option.click()
                    break
        
        wms.selenium_click(By.LINK_TEXT, 'Alterar', 20)

        sleep(2)
        validador_error = navegador.find_elements(By.CSS_SELECTOR, "ul.field-errors")
        for error in validador_error:
            if error.text == "Não é possível alterar o controle por lote de um item que possui estoque no armazém":
                print("\n\nNão é possível alterar o controle por lote de um item que possui estoque no armazém!!!")

                wms.selenium_click(By.CSS_SELECTOR, "a[data-hj-test-id='active-thread-previous-button']", 20)

        wms.selenium_click(By.CSS_SELECTOR, "a[data-hj-test-id='active-thread-previous-button']", 20)
        
        cont += 1

        porcentagem = (cont / len(itens)) * 100
        print(f"Confirmado com sucesso: {cont}/{len(itens)} ({porcentagem:.1f}%) - {item}")

    file_path.close()
    navegador.quit()
    cancelar_inputs()

