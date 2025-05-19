# imports de funcoes exteriores
from adm_funcionalidades import *

###################

menu = {
    1: "administrador",
    2: "usuário comum"
}

def exibir_menu():
    """
    Função para exibir o menu de opções e retornar a escolha do usuário.
    :return: Opção escolhida pelo usuário.
    """
    print("Menu:")
    for opcao, descricao in menu.items():
        print(f"{opcao} - {descricao}")
    escolha = int(input("Escolha uma opção: ")) # Lê a opção escolhida pelo usuário, sem validar
    return escolha # Retorna a opção escolhida

def main():
    """
    Função principal que exibe o menu e chama as funções correspondentes
    de acordo com a escolha do usuário.
    """
    while True: # Loop infinito
        escolha = exibir_menu() # Chama a função exibir_menu e armazena a escolha do usuário
        if escolha == 1: 
            adm() # Chama a função 
        elif escolha == 2: 
            usuario() # Chama a função 
        elif escolha == 0: # Sair
            sair() # Chama a função sair
        else:
            print("Opção inválida. Tente novamente.") # Mensagem de erro para opção inválida

def sair():
    """
    Função para sair do programa.
    :return: None
    """
    print("Saindo...")
    exit() # Encerra o programa

# menu para o usuario selecionar se ja possui uma conta ou nao
menu_login_ou_cadastro = {
    1: "Novo usuário",
    2: "Logar em uma conta"
    }

def escolha_login_ou_cadastro():
        """
        Função principal que exibe o menu e chama as funções correspondentes
        de acordo com a escolha do usuário.
        """
        while True: # Loop infinito
            escolha = exibir_menu_login_ou_cadastro() # Chama a função exibir_menu e armazena a escolha do usuário
            if escolha == 1: # Novo usuario
                cadastro() # Chama a função cadastro
            elif escolha == 2: # login
                login() 
            elif escolha == 0: # Sair
                sair() # Chama a função sair
            else:
                print("Opção inválida. Tente novamente.") # Mensagem de erro para opção inválida

# funcao que exibe o menu de login/cadastro
def exibir_menu_login_ou_cadastro():
    """
    Função para exibir o menu de opções e retornar a escolha do usuário.
    :return: Opção escolhida pelo usuário.
    """
    print("Menu:")
    for opcao, descricao in menu_login_ou_cadastro.items():
        print(f"{opcao} - {descricao}")
    escolha = int(input("Escolha uma opção: ")) # Lê a opção escolhida pelo usuário, sem validar
    return escolha # Retorna a opção escolhida

# funcao ainda nao concluida
def adm():
     """
    Função para o adm logar em sua conta
    """
    print("Login como administrador:")
    adm_procurar = input("Digite usename: ")
    senha_procurar = input("Digite a senha: ")
     # Abre o arquivo adms.txt para leitura, lê todo o conteúdo e fecha o arquivo
        with open("./arq_txt/adms.txt", "r") as arquivo_adms:
            adms = arquivo_adms.readlines() # Lê todas as linhas do arquivo e armazena na lista adm
            
        # Procura o adm no arquivo
        for linha in adms: # Para cada linha no conteúdo do arquivo
            adm,senha = linha.strip().split(",") # Divide a linha em partes, separando por virgula
            # Verifica se o username procurado é igual ao do adm, ignorando maiusculas e minusculas
            if adm_procurar.lower() == adm.lower(): 
                if senha_procurar == senha: # verifica se a senha inserida esta correta
                    print("Login como adm realizado com sucesso")
                    """
                    chama a funcao de exibicao do menu, a funcao vem do arquivo adm_funcionalidades
                    """
                    main_adm() 
                    break # Sai do loop se o adm e a senha forem corretos
                else:
                    print("senha incorreta")
        else: # Se não encontrar o adm
            print("Usuário não encontrado.") 

# funcao caso o usuario seja comum
def usuario():
    escolha_login_ou_cadastro()

# funcao de cadastro
def cadastro():
    """
    Função para adicionar um novo usuario 
    """
    print("Novo usuário:")
    username = input("Digite o nome de usuário: ")
    senha = input("Digite a senha: ")
    # Abre o arquivo usuarios para escrita. Modo "a" para adicionar ao final do arquivo
    arquivo_users = open("./arq_txt/users.txt", "a")
    # Grava o user no arquivo
    arquivo_users.write(f"{username},{senha}") # Grava o user no arquivo, separando os dados por vírgula
    # Fecha o arquivo
    arquivo_users.close()
    print("Usuário cadastrado com sucesso!") # Mensagem de sucesso

def login():
    """
    Procurar um contato na agenda pelo nome.
    Se o contato for encontrado, imprime os dados do contato.
    Se não for encontrado, imprime uma mensagem de erro.
    :return: None
    """
    while True:
        print("Login:")
        user_procurar = input("Digite o seu nome de usuário: ")
        senha_procurar = input("Digite sua senha: ")
        # Abre o arquivo contatos.txt para leitura, lê todo o conteúdo e fecha o arquivo
        with open("./arq_txt/users.txt", "r") as arquivo_users:
            users = arquivo_users.readlines() # Lê todas as linhas do arquivo e armazena em uma lista
            
        # Procura o user no arquivo
        for linha in users: # Para cada linha no conteúdo do arquivo
            user,senha = linha.strip().split(",") # Divide a linha em partes, separando por virgula
            # Verifica se o nome procurado é igual ao nome do user, ignorando maiusculas e minusculas
            if user_procurar.lower() == user.lower(): 
                if senha_procurar == senha: # verifica se a senha que o usuario inseriu esta correta
                    print("Login realizado com sucesso")
                    break # Sai do loop se o usuario e a senha forem corretos
                else:
                    print("senha incorreta")
        else: # Se não encontrar o usuario
            print("Usuário não encontrado.") 
   
