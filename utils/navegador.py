from selenium import webdriver
from utils.shared import criar_service


def navegador_google():
    service = criar_service()
    navegador = webdriver.Chrome(service=service)
    navegador.get("https://wmsweb-prd.martins.com.br/core/Default.html")
    navegador.maximize_window()

    return navegador
