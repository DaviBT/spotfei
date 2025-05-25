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
    arquivo_musicas.write(f"{musica_nome},{musica_artista},{musica_duracao},{musica_genero},0,0\n") # Grava a musica no arquivo, separando os dados por virgula
    # Fecha o arquivo
    arquivo_musicas.close()
    print("Musica adicionada com sucesso!") # Mensagem de sucesso

def consultar_user():
    print("Consultar usuario")
    user_name = input("Digite o username do usuario: ")


    # musicas curtidas -------------

    # abre o arquivo para leitura
    arquivo_curtidas = open(f"./arq_txt/curtidas/curtidas_{user_name}.txt", "r")
    # Lê o conteúdo do arquivo
    curtidas = arquivo_curtidas.readlines()
    # Fecha o arquivo
    arquivo_curtidas.close()
    musica = []
    for linha in curtidas:
        musica.append(linha.strip())
    print(f"musicas curtidas: {musica}")

    print("-----------------")

    # musicas descurtidas -------------

    # abre o arquivo para leitura
    arquivo_descurtidas = open(f"./arq_txt/descurtidas/descurtidas_{user_name}.txt", "r")
    # Lê o conteúdo do arquivo
    descurtidas = arquivo_descurtidas.readlines()
    # Fecha o arquivo
    arquivo_descurtidas.close()
    musicas_descurtidas = []
    for descurtida in descurtidas:
        musicas_descurtidas.append(descurtida.strip())
    print(f"musicas descurtidas: {musicas_descurtidas}")
            
            
            
    print("-----------------")


    # playlists -------------

    # abre o arquivo para leitura
    arq_playlists = open(f"./arq_txt/playlists/playlists_{user_name}.txt", "r")
    # Lê o conteúdo do arquivo
    playlists_array = arq_playlists.readlines()
    # Fecha o arquivo
    arq_playlists.close()
    playlists = []
    for playlist in playlists_array:
        nome_playlist = playlist.strip().split("_")
        playlist = nome_playlist[2]
        playlists.append(playlist)
        nome_playlist = []
    print(f"playlists do usuario: {playlists}")
            
            
            
    print("-----------------")
            

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
    print("Estatísticas do sistema: ")
    print("")

    print("Top 5 músicas com mais curtidas: ")
    musicas = []

    # Abre e lê o arquivo
    with open("./arq_txt/musicas.txt", "r") as arq_musicas:
        conteudo = arq_musicas.readlines()

    for linha in conteudo:
        musica = linha.strip().split(",")
        nome = musica[0]
        autor = musica[1]
        curtidas = int(musica[4])  # índice 4 e de curtidas
        musicas.append((nome, autor, curtidas))

    # Ordena por número de curtidas (ordem decrescente)
    musicas.sort(key=lambda x: x[2], reverse=True)

    # Mostra as 5 mais curtidas
    for i, (nome, autor, curtidas) in enumerate(musicas[:5], start=1):
        print(f"{i}. {nome} - {autor} ({curtidas} curtidas)")

        

    
    print("")
    print("-------------")
    print("")
    
    print("Top 5 músicas mais descurtidas: ")
    musicas_descurtidas = []

    # Lê novamente o arquivo e carrega descurtidas
    with open("./arq_txt/musicas.txt", "r") as arq_musicas:
        conteudo = arq_musicas.readlines()

    for linha in conteudo:
        musica = linha.strip().split(",")
        nome = musica[0]
        autor = musica[1]
        descurtidas = int(musica[5])  # índice 5 é descurtidas
        musicas_descurtidas.append((nome, autor, descurtidas))

    # Ordena por descurtidas (ordem decrescente)
    musicas_descurtidas.sort(key=lambda x: x[2], reverse=True)

    # Mostra top 5 descurtidas
    for i, (nome, autor, descurtidas) in enumerate(musicas_descurtidas[:5], start=1):
        print(f"{i}. {nome} - {autor} ({descurtidas} descurtidas)")
    
    print("")
    print("-------------")
    print("")
    
    print("Quantidade de usuarios: ")
    # abre o arquivo no modo de leitura
    arq_users = open("./arq_txt/users.txt", "r")
    # cria uma lista com os users do arquivo
    users = arq_users.readlines()
    quant_users = 0
    for user in users:
        quant_users = quant_users + 1
    print(quant_users)

    print("")
    print("-------------")
    print("")
    
    print("Quantidade de musicas: ")
    # abre o arquivo no modo de leitura
    arq_musicas = open("./arq_txt/musicas.txt", "r")
    # cria uma lista com as musicas do arquivo
    musicas = arq_musicas.readlines()
    qnt_musicas = 0
    for musica in musicas:
        qnt_musicas = qnt_musicas + 1
    print(qnt_musicas)
    print("")
