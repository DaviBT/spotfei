# funcoes importadas
from cadastro_login import *

# arquivo com as funcionalidades dos adms

menu = {
    0: "sair",
    1: "adicionar musicas",
    2: "consultar usuarios", 
    3: "excluir musicas",
    4: "cadastrar artistas",
    5: "ver estatisticas",
}

def exibir_menu_adm():
    """
    Função para exibir o menu de opções e retornar a escolha do adm.
    :return: Opção escolhida pelo adm.
    """
    print("Menu:")
    for opcao, descricao in menu.items():
        print(f"{opcao} - {descricao}")
    escolha = int(input("Escolha uma opção: ")) # Lê a opção escolhida pelo usuário, sem validar
    return escolha # Retorna a opção escolhida

def main_adm():
    """
    Função principal que exibe o menu e chama as funções correspondentes
    de acordo com a escolha do adm.
    """
    while True: # Loop infinito
        escolha = exibir_menu_adm() # Chama a função exibir_menu e armazena a escolha do usuário
        if escolha == 1: 
            add_musica() # Chama a função 
        elif escolha == 2: 
            consultar_user() # Chama a função 
        elif escolha == 3: 
            excluir_musica() # Chama a função 
        elif escolha == 4: 
            add_artista() # Chama a função 
        elif escolha == 5: 
            ver_estatisticas() # Chama a função 
        elif escolha == 0: # Sair
            sair() # Chama a função sair
        else:
            print("Opção inválida. Tente novamente.") # Mensagem de erro para opção inválida


def add_musica():
    """
    Função para adicionar uma nova musica 
    """
    print("Nova musica:")
    musica_nome = input("Digite o nome da musica: ")
    musica_artista = input("Digite o artista da musica: ")
    musica_duracao = input("Digite a duracao da musica: ")
    musica_genero = input("Digite o genero da musica: ")
    # Abre o arquivo musicas para escrita. Modo "a" para adicionar ao final do arquivo
    arquivo_musicas = open("./arq_txt/musicas.txt", "a")
    # Grava a musica no arquivo
    arquivo_musicas.write(f"{musica_nome},{musica_artista},{musica_duracao},{musica_genero},0\n") # Grava a musica no arquivo, separando os dados por virgula
    # Fecha o arquivo
    arquivo_musicas.close()
    print("Musica adicionada com sucesso!") # Mensagem de sucesso

def consultar_user():
    print("Consultar usuario")
    user_name = input("Digite o username do usuario: ")
    # abre o arquivo de usuarios para leitura
    arquivo_users = open("./arq_txt/users.txt", "r")
    # Lê o conteúdo do arquivo
    conteudo = arquivo_users.readlines()
    # Fecha o arquivo
    arquivo_users.close()
    # Procura o user no arquivo
    for i, linha in enumerate(conteudo):
        user_name = linha.strip().split(",")
        if user_name.lower() == nome[0].lower():
            print(f"Informacoes do usuario {user_name}: ")
            print("playlists: ")
            
            print("-----------------")
            
            print("musicas curtidas: ")
            
            print("-----------------")
            
            print("musicas descurtidas: ")

            print("-----------------")
        else:
            print("usuario nao encontrado")
            exibir_menu_adm() # volta para o menu em caso de erro
            

def excluir_musica():
    """
    Apaga uma musica do arquivo musicas.txt
    :return: None
    """
    nome_apagar = input("Digite o nome da musica que deseja apagar: ")
    # Abre o arquivo musicas.txt para leitura
    arquivo_musicas = open("./arq_txt/musicas.txt", "r")
    # Lê o conteúdo do arquivo
    conteudo = arquivo_musicas.readlines()
    # Fecha o arquivo
    arquivo_musicas.close()
    # Procura a musica no arquivo
    for i, linha in enumerate(conteudo):
        nome = linha.strip().split(",")
        if nome_apagar.lower() == nome[0].lower():
            # .strip() -> remove espacos no inicio e fim da string
            print(f"Musica deletada: {linha.strip()}")
            # Remove a musica da lista da variavel conteudo
            conteudo.pop(i)
            break
    else: # Se não encontrar a musica
        print("Musica não encontrada.")
        
    # Abre o arquivo musicas.txt para escrita
    arquivo_musicas = open("./arq_txt/musicas.txt", "w")
    # Grava as musicas restantes no arquivo
    for linha in conteudo: # Para cada linha no conteudo do arquivo
        arquivo_musicas.write(linha) # Grava a linha no arquivo musicas.txt
    # Fecha o arquivo
    arquivo_musicas.close()
    print("Musica apagada com sucesso!") # Mensagem de sucesso


def add_artista():
    """
    Função para cadastrar um artista
    """
    print("Cadastrar artista:")
    artista_inserido = input("Digite o nome do artista: ")

    # Lê os artistas já cadastrados
    with open("./arq_txt/artistas.txt", "r") as arquivo_artistas:
        artistas = arquivo_artistas.readlines()

    # Verifica se já existe (ignorando maiúsculas/minúsculas e espaços)
    if any(artista.strip().lower() == artista_inserido.lower() for artista in artistas):
        print("O artista já existe no arquivo.")
        exibir_menu_adm() # volta para o menu em caso de erro
    else:
        # Se não existir, adiciona
        with open("./arq_txt/artistas.txt", "a") as artistas_editar:
            artistas_editar.write(f"{artista_inserido}\n")
        print("Artista cadastrado com sucesso!")

def ver_estatisticas():
    print("")
    print("Estatisticas do sistema: ")
    print("")
    
    print("Top 5 musicas com mais curtidas: ")
    
    print("")
    print("-------------")
    print("")
    
    print("Top 5 musicas mais descurtidas: ")

    
    print("")
    print("-------------")
    print("")
    
    print("Quantidade de usuarios: ")
    # abre o arquivo no modo de leitura
    arq_users = open("./arq_txt/users", "r")
    # cria uma lista com as musicas do arquivo
    users = arq_users.readlines()
    for indice, conteudo in users:
        a = 0
    print(indice)
    
        

    print("")
    print("-------------")
    print("")
    
    print("Quantidade de musicas: ")
    # abre o arquivo no modo de leitura
    arq_musicas = open("./arq_txt/musicas", "r")
    # cria uma lista com as musicas do arquivo
    musicas = arq_musicas.readlines()
    for indice, conteudo in musicas:
        a = 0
    print(indice)
