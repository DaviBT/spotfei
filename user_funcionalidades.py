

menu = {
    1: "Buscar musicas",
    2: "Gerenciar playlist",
    3: "Visualizar histórico",
    0: "Sair"
}

def exibir_menu_usuario():
    """
    Função para exibir o menu de opções e retornar a escolha do usuário.
    :return: Opção escolhida pelo usuário.
    """
    print("Menu:")
    for opcao, descricao in menu.items():
        print(f"{opcao} - {descricao}")
    escolha = int(input("Escolha uma opção: ")) # Lê a opção escolhida pelo usuário, sem validar
    return escolha # Retorna a opção escolhida

def main_usuario(user):
    """
    Função principal que exibe o menu e chama as funções correspondentes
    de acordo com a escolha do usuário.
    """
    while True: # Loop infinito
        escolha = exibir_menu_usuario() # Chama a função exibir_menu e armazena a escolha do usuário
        if escolha == 1: # Buscar musicas
            buscar_musicas() # Chama a função buscar_musicas
        elif escolha == 2: # Gerenciar playlist
            gerenciar_playlist(user) # Chama a função gerenciar_playlist
        elif escolha == 3: # Visualizar histórico
            visualizar_historico() # Chama a função visualizar_historico
        elif escolha == 0: # Sair
            sair() # Chama a função sair
        else:
            print("Opção inválida. Tente novamente.") # Mensagem de erro para opção inválida
            
def buscar_musicas():
    """
    Função para buscar musicas.
    """
    print("Buscar musicas:")
    nome_musica = input("Digite o nome da musica: ")
    
    with open("./arq_txt/musicas.txt", "r") as arquivo_musicas: # Abre o arquivo musicas.txt para leitura
        conteudo = arquivo_musicas.readlines() # Lê todas as linhas do arquivo e armazena em uma lista
        
    # Procura o contato no arquivo
    for linha in conteudo: # Para cada linha no conteúdo do arquivo
        musica_nome, musica_artista, musica_duracao, musica_genero, curtidas, descurtidas = linha.strip().split(",") # Divide a linha em partes, separando por vírgula
        if nome_musica.lower() == musica_nome.lower(): # Verifica se o nome procurado é igual ao nome do da musica, ignorando maiúsculas e minúsculas
            print(f"Nome: {musica_nome}, Artista: {musica_artista}, Duração: {musica_duracao}, Gênero: {musica_genero}, Curtidas: {curtidas}, Descurtidas: {descurtidas}") # Exibe os dados da musica
            break # Sai do loop 
    else: # Se não encontrar o contato
        print("Música não encontrada.") # Mensagem de erro se o contato não for encontrado
    
        ########################################## vamo ve
import os

def exibir_menu_playlist():
    menu_playlist = {
        1: "Criar playlist",
        2: "Visualizar playlist",
        0: "Sair"
    }
    print("Menu Playlist:")
    for opcao, descricao in menu_playlist.items():
        print(f"{opcao} - {descricao}")
    escolha = int(input("Escolha uma opção: "))
    return escolha

def criar_playlist(user):
    nome_playlist = input(f"Digite o nome da nova playlist: {user}_")
    caminho_playlist = f"./arq_txt/{nome_playlist}.txt"
    with open(caminho_playlist, "w") as arquivo_playlists:
        arquivo_playlists.write(f"{nome_playlist}\n")
        print(f"Playlist '{nome_playlist}' criada com sucesso!")
        print("Adicione músicas à sua playlist (digite 'fim' para parar):")
        while True:
            musica = input("Nome da música: ").strip()
            if musica.lower() == "fim":
                break
            arquivo_playlists.write(f"{musica}\n")
        print("Músicas adicionadas à playlist!")

def mostrar_musicas_playlist(nome_playlist):
    caminho_playlist = f"./arq_txt/{nome_playlist}.txt"
    try:
        with open(caminho_playlist, "r") as arquivo:
            linhas = arquivo.readlines()
        print(f"Músicas da playlist '{nome_playlist}':")
        for musica in linhas[1:]:  # pula a primeira linha (nome da playlist)
            print(musica.strip())
    except FileNotFoundError:
        print("Playlist não encontrada.")

def adicionar_musica(nome_playlist):
    caminho_playlist = f"./arq_txt/{nome_playlist}.txt"
    nome_musica = input("Digite o nome da musica que deseja adicionar: ")
    with open(caminho_playlist, "a") as arquivo:
        arquivo.write(f"{nome_musica}\n")
    print(f"Música '{nome_musica}' adicionada à playlist!")

def remover_musica(nome_playlist):
    caminho_playlist = f"./arq_txt/{nome_playlist}.txt"
    nome_musica = input("Digite o nome da musica que deseja remover: ")
    with open(caminho_playlist, "r") as arquivo:
        musicas = arquivo.readlines()
    # Remove a música desejada
    musicas_novas = [musica for musica in musicas if musica.strip() != nome_musica and musica.strip() != nome_playlist]
    with open(caminho_playlist, "w") as arquivo:
        arquivo.write(f"{nome_playlist}\n")
        for musica in musicas_novas:
            arquivo.write(musica)
    print(f"Música '{nome_musica}' removida da playlist (se existia).")

def visualizar_playlist(user):
    print("Suas playlists:")
    playlists = [f for f in os.listdir("./arq_txt") if f.startswith(user+"_") and f.endswith(".txt")]
    if not playlists:
        print("Nenhuma playlist encontrada.")
        return
    for pl in playlists:
        print(pl.replace(".txt", ""))
    nome = input("Digite o nome da playlist que deseja gerenciar: ").strip()
    if not os.path.exists(f"./arq_txt/{nome}.txt"):
        print("Playlist não encontrada.")
        return
    mostrar_musicas_playlist(nome)
    menu_edit = {
        1: "Adicionar música",
        2: "Remover música",
        0: "Sair"
    }
    while True:
        print("Menu de edição da playlist:")
        for opcao, descricao in menu_edit.items():
            print(f"{opcao} - {descricao}")
        escolha = int(input("Escolha uma opção: "))
        if escolha == 1:
            adicionar_musica(nome)
        elif escolha == 2:
            remover_musica(nome)
        elif escolha == 0:
            break
        else:
            print("Opção inválida. Tente novamente.")

def gerenciar_playlist(user):
    while True:
        escolha = exibir_menu_playlist()
        if escolha == 1:
            criar_playlist(user)
        elif escolha == 2:
            visualizar_playlist(user)
        elif escolha == 0:
            sair()
        else:
            print("Opção inválida. Tente novamente.")

def sair():
    print("Saindo do programa...")
    exit()