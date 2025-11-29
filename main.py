from time import sleep
from utils.ciclica import ciclica
from utils.verificacao import Verificacao
from utils.shared import historico_funcoes, limpar_tela
from utils.fechar_divergencia import fechar_com_divergencia
from utils.cancelamento import Cancelamento_de_pedido_de_ajuste_contabil
from utils.desbloqueio import desbloqueio
from utils.bloqueio import bloqueio
from utils.inclusao import inclusao_pedidos_ajustes
from utils.confirmacao import confirmacao_de_pedido_ajuste
from utils.bloqueado_avancado import Bloqueado_avancado
from utils.excluir_apanha import excluir_apanha
from utils.usuarios import Administrador
from utils.classArmazenagem import classArmazenagem
from utils.data_de_validade_lote import Lote

def tabela(username, permissoes_usuario):
    from servidor import login_user, main
    historico_funcoes.append(login_user)

    opcoes = {
        "1": ciclica,
        "2": Verificacao,
        "3": Cancelamento_de_pedido_de_ajuste_contabil,
        "4": confirmacao_de_pedido_ajuste,
        "5": inclusao_pedidos_ajustes,
        "6": bloqueio,
        "7": desbloqueio,
        "8": Bloqueado_avancado,
        "9": fechar_com_divergencia,
        "10": excluir_apanha,
        "11": classArmazenagem,
        "12": Lote,
        "ADM": Administrador
    }
    try:
        while True:
            limpar_tela()

            # Cabeçalho com destaque
            print(
                "\033[96m\n╔════════════════════════════════════════════════════════╗"
                "\n║                   Sistema Auto.app                     ║"
                "\n╠════════════════════════════════════════════════════════╣"
                "\n║    Automatização WMS - KORBER  Controle de Estoque     ║"
                "\n╚════════════════════════════════════════════════════════╝\033[0m"
            )

            # Menu estilizado
            print(
                "\n\033[92m➤\033[0m 1  •  Gerar cíclica"
                "\n\033[92m➤\033[0m 2  •  Gerar verificação"
                "\n\033[92m➤\033[0m 3  •  Cancelamento de pedido de ajuste contábil"
                "\n\033[92m➤\033[0m 4  •  Confirmação de pedido de ajuste contábil"
                "\n\033[92m➤\033[0m 5  •  Inclusão de pedido de ajuste contábil"
                "\n\033[92m➤\033[0m 6  •  Bloquear por item"
                "\n\033[92m➤\033[0m 7  •  Desbloqueio por item"
                "\n\033[92m➤\033[0m 8  •  Tratativa do bloqueado avançado"
                "\n\033[92m➤\033[0m 9  •  Fechar ordem com divergência"
                "\n\033[92m➤\033[0m 10 •  Excluir endereços vazios"
                "\n\033[92m➤\033[0m 11 •  Itens sem classe de armazenagem"
                "\n\033[92m➤\033[0m 12 •  Data de validade e lote"
                "\n────────────────────────────────────────────────────────"
                "\n\033[91m➤\033[0m 0  •  Voltar ao menu anterior"
            )

            print("\nDigite o número da opção desejada:")

            escolha = input("» ").upper().strip()

            if escolha == "0":
                limpar_tela()
                print(f"Voltando ao menu anterior...")
                main
                break

            funcao = opcoes.get(escolha)

            if escolha in opcoes and escolha in permissoes_usuario or escolha in opcoes and "ADM" in permissoes_usuario:
                limpar_tela()
                print(f"\nExecutando: {funcao.__name__.replace('_', ' ').capitalize()}...\n")
                funcao()
            else:
                print(f"Opção inválida, ou acesso NEGADO!! Tente novamente.")
                sleep(1)
    except:
        return main

