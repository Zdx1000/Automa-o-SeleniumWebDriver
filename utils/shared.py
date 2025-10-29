"""
Módulo compartilhado para variáveis e funções globais
"""
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import os

# Configuração do serviço do Selenium
service = Service(ChromeDriverManager().install())

# Lista para manter o histórico de funções
historico_funcoes = []

def registrar_progresso(text: str, endereco, sucesso=True, file_path="progresso.txt"):
    """Registra o progresso das operações em um arquivo"""
    with open(file_path, "a", encoding="utf-8") as arquivo:
        status = "SUCESSO" if sucesso else "FALHA"
        arquivo.write(f"{text} {endereco} - Status: {status}\n")

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')