"""
Modulo compartilhado para variaveis e funcoes globais.
"""
import os
import subprocess
from functools import lru_cache

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Lista para manter o historico de funcoes
historico_funcoes = []


@lru_cache(maxsize=1)
def obter_chromedriver() -> str:
    """Resolve e cacheia o caminho do chromedriver para o processo atual."""
    return ChromeDriverManager().install()


def criar_service() -> Service:
    """
    Cria um Service do Chrome de forma consistente entre maquinas.
    No Windows, forca o processo do chromedriver sem janela de console.
    """
    service = Service(
        executable_path=obter_chromedriver(),
        log_output=subprocess.DEVNULL,
    )

    if os.name == "nt":
        create_no_window = getattr(subprocess, "CREATE_NO_WINDOW", None)
        if create_no_window is not None:
            if hasattr(service, "creation_flags"):
                service.creation_flags = create_no_window
            elif hasattr(service, "creationflags"):
                service.creationflags = create_no_window

    return service


def registrar_progresso(text: str, endereco, sucesso=True, file_path="progresso.txt"):
    """Registra o progresso das operacoes em um arquivo."""
    with open(file_path, "a", encoding="utf-8") as arquivo:
        status = "SUCESSO" if sucesso else "FALHA"
        arquivo.write(f"{text} {endereco} - Status: {status}\n")


def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")
