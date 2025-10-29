import pwinput
import json
from time import sleep
from utils.shared import limpar_tela

PERMISSOES_ARQUIVO = r"\\fs010J\grpctlest$\PASTA GERAL CE\DANYLLO\Automação em Projeto\usuarios.json"

def carregar_usuarios():
    try:
        with open(PERMISSOES_ARQUIVO, "r") as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return {}

def salvar_usuarios(usuarios):
    with open(PERMISSOES_ARQUIVO, "w") as arquivo:
        json.dump(usuarios, arquivo, indent=4)

def Registrar_usuario():
    usuarios = carregar_usuarios()

    print(f'''
    ╔════════════════════════════════════════════════════════╗
    ║                Registrar Novo Usuário                  ║
    ╚════════════════════════════════════════════════════════╝
    ''')

    username = input(f"\nDigite o nome do novo usuário\n> ").upper().strip()

    if username in usuarios:
        print(f"Usuário [ {username} ] já existe no banco de dados!")
    else:
        while True:
            senha = pwinput.pwinput(f"\nDigite a senha para o novo usuário: ", mask="*").strip()
            senha2 = pwinput.pwinput("Confirme a senha: ", mask="*").strip()
            if senha == senha2:
                break
            else:
                print(f"\nSenha de confirmação NÃO esta de acordo com a senha descrita!")

        usuarios[username] = {"senha": senha, "permissoes": []}
        salvar_usuarios(usuarios)
        print(f"Usuário [ {username} ] registrado com sucesso!")
    input(f"Pressione enter para continuar...")

def Remover_usuario():
    usuarios = carregar_usuarios()

    print(f'''
    ╔════════════════════════════════════════════════════════╗
    ║                  Remover Usuário                       ║
    ╚════════════════════════════════════════════════════════╝
    ''')

    print(f'''
---------------------
- Lista de usuários -
---------------------''')
    for usuario in usuarios:
        if usuario != "ADM":
            print(f" ● {usuario} ")

    username = input(f"\nDigite o nome do usuário para remover\n> ").upper().strip()

    if username in usuarios and username != "ADM":
        confirmacao = input(f"Tem certeza que deseja remover o usuário [ {username} ]? (s/n) > ").strip().lower()
        if confirmacao == "s":
            del usuarios[username]
            salvar_usuarios(usuarios)
            print(f"Usuário [ {username} ] removido com sucesso!")
        else:
            print(f"Operação cancelada!")
    else:
        print(f"Usuário não existe ou é protegido!")
    input(f"Pressione enter para continuar...")

def Alterar_senha():
    usuarios = carregar_usuarios()

    print(f'''
    ╔════════════════════════════════════════════════════════╗
    ║                 Alterar Senha de Usuário                  ║
    ╚════════════════════════════════════════════════════════╝
    ''')

    print(f'''
---------------------
- Lista de usuários -
---------------------''')
    for usuario in usuarios:
        if usuario != "ADM":
            print(f" ● {usuario} ")

    username = input(f"\nDigite o nome do usuário para alterar a senha\n> ").upper().strip()

    if username in usuarios:
        while True:
            nova_senha = pwinput.pwinput("Digite a nova senha: ", mask="*").strip()
            nova_senha2 = pwinput.pwinput("Confirme a senha: ", mask="*").strip()
            if nova_senha == nova_senha2:
                break
            else:
                print(
                    f"\nSenha de confirmação NÃO esta de acordo com a senha descrita!",
                    0.7)
        usuarios[username]["senha"] = nova_senha
        salvar_usuarios(usuarios)
        print(f"Senha do usuário [ {username} ] alterada com sucesso!")
    else:
        print(f"Usuário não existe em nosso banco de dados!!")
    input(f"Pressione enter para continuar...")

def Adicionar_permissao():
    permissoes = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "ADM"]
    usuarios = carregar_usuarios()
    print(f'''
    ╔════════════════════════════════════════════════════════╗
    ║           Adicionar Permissão a um Usuário             ║
    ╚════════════════════════════════════════════════════════╝
    ''')

    cont = 0
    print(f'''
---------------------
- Lista de usuários -
---------------------''')
    for usuario in usuarios:
        if usuario == "ADM":
            pass
        else:
            cont += 1
            print(f" ● {usuario} ")
    usuario = input(f"\nDigite o nome do usuário\n> ").upper().strip()

    print(f'''
    -----------------------
    - Lista de permissões -
    -----------------------''')
    print(f'''
       [ 1 ]  Gerar ciclica
       [ 2 ]  Gerar verificação
       [ 3 ]  Cancelamento de pedido de ajuste contábil
       [ 4 ]  Confirmação de pedido de ajuste contábil
       [ 5 ]  Inclusão de pedido de ajuste contábil
       [ 6 ]  Bloquear por item
       [ 7 ]  Desbloqueio por item
       [ 8 ]  Tratativa do bloqueado avançado
       [ 9 ]  Fechar Ordem com divergência

    ''')
    if usuario in usuarios:
        nova_permissao = input(f"\nDigite a permissão a adicionar para [ {usuario} ]\n> ").strip().upper()
        if nova_permissao not in usuarios[usuario]["permissoes"] and nova_permissao in permissoes:
            usuarios[usuario]["permissoes"].append(nova_permissao)
            salvar_usuarios(usuarios)
            print(f"Permissão [ {nova_permissao} ] adicionada para o usuário [ {usuario} ]")
            input(f"Pressione enter para continuar...")
        else:
            print(f"O usuário [ {usuario} ] já possui a permissão ou [ {nova_permissao} ] não existe!!!")
            input(f"Pressione enter para continuar...")
    else:
        print(f"Usuário não existe em nosso banco de dados!!")
        input(f"Pressione enter para continuar...")

def Remover_permissao():
    usuarios = carregar_usuarios()
    print(f'''
    ╔════════════════════════════════════════════════════════╗
    ║            Remover Permissão a um Usuário              ║
    ╚════════════════════════════════════════════════════════╝
    ''')

    cont = 0
    print(f'''
---------------------
- Lista de usuários -
---------------------''')
    for usuario in usuarios:
        if usuario == "ADM":
            pass
        else:
            cont += 1
            print(f" ● {usuario} ")
    usuario = input(f"\nDigite o nome do usuário\n> ").upper().strip()
    print(f'''
    -----------------------
    - Lista de permissões -
    -----------------------''')
    print(f'''
       [ 1 ]  Gerar ciclica
       [ 2 ]  Gerar verificação
       [ 3 ]  Cancelamento de pedido de ajuste contábil
       [ 4 ]  Confirmação de pedido de ajuste contábil
       [ 5 ]  Inclusão de pedido de ajuste contábil
       [ 6 ]  Bloquear por item
       [ 7 ]  Desbloqueio por item
       [ 8 ]  Tratativa do bloqueado avançado
       [ 9 ]  Fechar Ordem com divergência

    ''')
    if usuario in usuarios:
        print(f"Permissões atuais de [ {usuario} ]: [ {usuarios[usuario]['permissoes']} ]")
        permissao_remover = input(f"Digite a permissão a remover\n> ").strip().upper()
        if permissao_remover in usuarios[usuario]["permissoes"]:
            usuarios[usuario]["permissoes"].remove(permissao_remover)
            salvar_usuarios(usuarios)
            print(f"Permissão [ {permissao_remover} ] removida do usuário [ {usuario} ]")
            input(f"Pressione enter para continuar...")
        else:
            print(f"O usuário [ {usuario} ] não possui a permissão [ {permissao_remover} ]")
            input(f"Pressione enter para continuar...")
    else:
        print(f"Usuário não existe em nosso banco de dados!!")
        input(f"Pressione enter para continuar...")


def Administrador():
    from main import tabela

    opcoes_administrador = {
        "1": Registrar_usuario,
        "2": Alterar_senha,
        "3": Adicionar_permissao,
        "4": Remover_permissao,
        "5": Remover_usuario,
        "0": tabela,
    }
    while True:
        limpar_tela()

        print("\n╔════════════════════════════════════════════════════════╗\n║")
        print("              Bem-vindo a rede Administrador            ")
        print("║\n╚════════════════════════════════════════════════════════╝")

        # Menu
        print(f'''
       [ 1 ]  Registrar usuário ao sistema
       [ 2 ]  Alterar senha do usuário
       [ 3 ]  Adincionar permissão do usuário
       [ 4 ]  Remover permissão do usuário
       [ 5 ]  Remover usuário
       [ 0 ]  Voltar ao menu anterior
    ''')

        print("\nEscolha uma das opções:")

        escolha = input("> ").upper()

        if escolha == "0":
            limpar_tela()
            print(f"Voltando ao menu anterior...")
            tabela
            break

        funcao = opcoes_administrador.get(escolha)

        if escolha in opcoes_administrador:
            limpar_tela()
            print(f"\nExecutando: {funcao.__name__.replace('_', ' ').capitalize()}...\n")
            funcao()
        else:
            print(
                f"Opção inválida!! Tente novamente.",
                0.5)
            sleep(1)