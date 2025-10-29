from time import sleep
import sys
import os
import pwinput
from utils.shared import historico_funcoes, limpar_tela
from utils.usuarios import carregar_usuarios
from main import tabela

username = os.environ.get("USER") or os.environ.get("USERNAME")

print("Instalando Packs Selenium......")

def licenca():
    print(
        f'''
    ╔══════════════════════════════════════════════════════════════════════════════════════╗
    ║            LICENÇA DE RESPONSABILIDADE PARA USO DE AUTOMAÇÃO                         ║
    ║                                                                                      ║
    ║   Eu, [{username.upper()}], declaro que li, compreendi e aceito os termos e condições           ║
    ║                       de uso da automação [Auto.App].                                ║
    ║                                                                                      ║
    ║       Termos de Uso                                                                  ║
    ║                                                                                      ║
    ║   Uso Exclusivo: Reconheço que esta automação é destinada exclusivamente a           ║
    ║ usuários autorizados, e comprometo-me a utilizá-la estritamente dentro das           ║
    ║ finalidades designadas e para as quais fui previamente treinado.                     ║
    ║                                                                                      ║
    ║   Confidencialidade: Concordo em manter sigilo absoluto sobre quaisquer              ║
    ║ informações acessadas por meio da automação, comprometendo-me a não                  ║
    ║ compartilhá-las com terceiros, seja de forma direta ou indireta.                     ║
    ║                                                                                      ║
    ║   Responsabilidade por Uso Indevido: Estou ciente de que qualquer utilização         ║
    ║ inadequada, incorreta ou fora do escopo autorizado será de minha inteira             ║
    ║ responsabilidade, sujeitando-me a sanções administrativas,                           ║
    ║ legais e/ou disciplinares, conforme regulamentação interna da empresa e              ║
    ║ legislação vigente.                                                                  ║
    ║                                                                                      ║
    ║   Monitoramento: Autorizo a empresa [Martins] a monitorar e registrar                ║
    ║ todas as minhas atividades na automação, ciente de que esses registros poderão       ║
    ║ ser utilizados em auditorias internas ou investigações.                              ║
    ║                                                                                      ║
    ║   Reportar Anomalias: Comprometo-me a reportar imediatamente ao setor                ║
    ║ responsável qualquer comportamento inesperado, falha ou vulnerabilidade detectada    ║
    ║ na automação, a fim de garantir a segurança e integridade do sistema.                ║
    ║                                                                                      ║
    ║   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━  ║
    ║  ┃     Declaração de Aceitação                         ┃                           ┃ ║
    ║  ┃                                                                                 ┃ ║
    ║  ┃ Declaro estar plenamente ciente das condições acima e concordo em utilizá-la    ┃ ║
    ║  ┃ com total responsabilidade, isentando a empresa [Martins] de qualquer           ┃ ║
    ║  ┃ responsabilidade por danos causados por negligência, uso inadequado ou          ┃ ║
    ║  ┃ não autorizadopor minha parte.                                                  ┃ ║
    ╚══════════════════════════════════════════════════════════════════════════════════════╝
''')
    lincenca_escola = input(f'''Concorda com os termos de uso: [S/N] \n> ''')[0].upper().strip()

    if lincenca_escola == "S":
        print(f"Acesso concedido!!")
        main()
    else:
        print(f"Acesso negado!!")
        sys.exit()

def login_user():
    historico_funcoes.append(main)

    usuarios = carregar_usuarios()

    Total_tentativas = 5

    while Total_tentativas > 0:
        limpar_tela()
        print('\033[96m' + '''     
         █░░░ █▀▀█ █▀▀▀ ░▀░ █▀▀▄   █▀▀▄ █▀▀   █░░█ █▀▀ █░░█ █▀▀█ ░▀░ █▀▀█   █▀▄▀█ █▀▀█ █▀▀█ ▀▀█▀▀ ░▀░ █▀▀▄ █▀▀
         █░░░ █░░█ █░▀█ ▀█▀ █░░█   █░░█ █▀▀   █░░█ ▀▀█ █░░█ █▄▄▀ ▀█▀ █░░█   █▒█▒█ █▄▄█ █▄▄▀ ░░█░░ ▀█▀ █░░█ ▀▀█
         █▄▄█ ▀▀▀▀ ▀▀▀▀ ▀▀▀ ▀░░▀   ▀▀▀░ ▀▀▀   ░▀▀▀ ▀▀▀ ░▀▀▀ ▀░▀▀ ▀▀▀ ▀▀▀▀   █░░▒█ ▀░░▀ ▀░▀▀ ░░▀░░ ▀▀▀ ▀░░▀ ▀▀▀
        ''' + '\033[0m')

        username = input("\nDigite o nome de usuário: ").upper().strip()
        password = pwinput.pwinput("Digite a senha: ", mask="*").strip()

        if username in usuarios and password == usuarios[username]["senha"]:
            permissoes_usuario = usuarios[username]["permissoes"]
            print(f"Login realizado com sucesso!!!")
            input(f"Pressione enter para continuar...")
            limpar_tela()
            tabela(username, permissoes_usuario)
            return

        else:
            Total_tentativas -= 1
            print(f"Nome de usuário ou senha incorretos! Tentativas restantes: {Total_tentativas}")
            input(f"\nPressione enter para continuar...\n")

            if Total_tentativas == 0:
                sys.exit()

def exibir_boas_vindas():
    print('\033[96m' + f'''
    ▒█▀▀█ █▀▀ █▀▄▀█ 　 ▀█░█▀ ░▀░ █▀▀▄ █▀▀▄ █▀▀█ 　 █▀▀█ █▀▀█ 　 ░█▀▀█ █░░█ ▀▀█▀▀ █▀▀█ ░ █▀▀█ █▀▀█ █▀▀█ 
    ▒█▀▀▄ █▀▀ █░▀░█ 　 ░█▄█░ ▀█▀ █░░█ █░░█ █░░█ 　 █▄▄█ █░░█ 　 ▒█▄▄█ █░░█ ░░█░░ █░░█ ▄ █▄▄█ █░░█ █░░█ 
    ▒█▄▄█ ▀▀▀ ▀░░░▀ 　 ░░▀░░ ▀▀▀ ▀░░▀ ▀▀▀░ ▀▀▀▀ 　 ▀░░▀ ▀▀▀▀ 　 ▒█░▒█ ░▀▀▀ ░░▀░░ ▀▀▀▀ █ ▀░░▀ █▀▀▀ █▀▀▀\n
    ''' + '\033[0m')
    print('''╔════════════════════════════════════════════════════════════════════════════╗''')
    print(
        f'''║                          Atenção: Uso Restrito                             ║''')
    print(
        f'''║                                                                            ║''')
    print(
        f'''║       Esta automação é destinada exclusivamente para uso de pessoas        ║''')
    print(
        f'''║                  autorizadas e devidamente treinadas.                      ║''')
    print(
        f'''║             O acesso indevido ou a utilização inadequada                   ║''')
    print(
        f'''║     pode comprometer os processos e gerar inconsistências irreparáveis.    ║''')
    print(
        f'''║                                                                            ║''')
    print('''╚════════════════════════════════════════════════════════════════════════════╝''')

def sair():
    print("Saindo do sistema...")
    sys.exit()

def main():
    exibir_boas_vindas()

    escolhas_main = {
        "1": login_user,
        "2": licenca,
        "3": sair
    }

    while True:
        print(f'''
        \033[92m[\033[0m1\033[92m]\033[0m \033[94m->\033[0m Login no sistema Auto.app
        \033[92m[\033[0m2\033[92m]\033[0m \033[94m->\033[0m Licença
        \033[92m[\033[0m3\033[92m]\033[0m \033[94m->\033[0m Sair do sistema''')

        escolha_2 = input(str(f"\nEscolha uma opção\n> "))

        if escolha_2 == "3":
            limpar_tela()
            sair()
            break

        funcao = escolhas_main.get(escolha_2)
        if funcao:
            limpar_tela()
            print(f"\nExecutando: {funcao.__name__.replace('_', ' ').capitalize()}...\n")
            funcao()
        else:
            print(f"Opção inválida. Tente novamente.")
            sleep(2)

if __name__ == "__main__":
    historico_funcoes = []
    main()


