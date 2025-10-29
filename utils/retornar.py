"""
Módulo para função de cancelar inputs e navegação
"""
from utils.shared import historico_funcoes

def cancelar_inputs():
    """Função para cancelar inputs e retornar à função anterior"""
    input(f" ● Precione enter para continuar....")
    if historico_funcoes:
        funcao_anterior = historico_funcoes.pop()
        print(f"\nVoltando para a função anterior: {funcao_anterior.__name__}")
        return funcao_anterior
    else:
        print("\nNenhuma função anterior. Retornando ao menu principal.")
        # Importamos aqui para evitar importação circular
        from main import tabela
        return tabela