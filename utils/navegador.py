
from selenium import webdriver
from utils.shared import service

def navegador_google():
    navegador = webdriver.Chrome(service=service)
    navegador.get("https://wmsweb-prd.martins.com.br/core/Default.html")
    navegador.maximize_window()

    return navegador