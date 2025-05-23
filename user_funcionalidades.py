

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
            buscar_musicas(user) # Chama a função buscar_musicas
        elif escolha == 2: # Gerenciar playlist
            gerenciar_playlist(user) # Chama a função gerenciar_playlist
        elif escolha == 3: # Visualizar histórico
            visualizar_historico() # Chama a função visualizar_historico
        elif escolha == 0: # Sair
            sair() # Chama a função sair
        else:
            print("Opção inválida. Tente novamente.")
            main_usuario()
            # Mensagem de erro para opção inválida
            
def buscar_musicas(user):
    """
    Função para buscar musicas.
    """

    # menu das possibilidades do usuario ao buscar uma musica
    menu_musica = {
        1: "Curtir musica",
        2: "Descurtir musica",
        3: "Adicionar a uma playlist nova",
        4: "Adicionar a uma playlist",
        0: "Sair"
    }
    # funcao que pode mostrar o menu ao user
    def exibir_menu_musica():
        """
        :return: Opção escolhida pelo usuário.
        """
        print("Menu:")
        for opcao, descricao in menu_musica.items():
            print(f"{opcao} - {descricao}")
        escolha = int(input("Escolha uma opção: ")) # Lê a opção escolhida pelo usuário, sem validar
        return escolha # Retorna a opção escolhida
    def main_musica(nome_musica, user):

        while True:
            escolha = exibir_menu_musica()
            if escolha == 1:
                curtir_musica(nome_musica, user)
            elif escolha == 2: 
                descurtir_musica(nome_musica, user) 
            elif escolha == 3: 
                criar_playlist(user) 
            elif escolha == 4: 
                adicionar_na_playlist() 
            elif escolha == 0: # Sair
                sair() # Chama a função sair
            else:
                print("Opção inválida. Tente novamente.") # Mensagem de erro para opção inválida

    print("Buscar musicas:")
    nome_musica = input("Digite o nome da musica: ")   

    
    with open("./arq_txt/musicas.txt", "r") as arquivo_musicas: # Abre o arquivo musicas.txt para leitura
        conteudo = arquivo_musicas.readlines() # Lê todas as linhas do arquivo e armazena em uma lista
        
    # Procura o contato no arquivo
    for linha in conteudo: # Para cada linha no conteúdo do arquivo
        musica_nome, musica_artista, musica_duracao, musica_genero, curtidas, descurtidas = linha.strip().split(",") # Divide a linha em partes, separando por vírgula
        if nome_musica.lower() == musica_nome.lower():
            print(f"Nome: {musica_nome}, Artista: {musica_artista}, Duração: {musica_duracao}, Gênero: {musica_genero}, Curtidas: {curtidas}, Descurtidas: {descurtidas}")
            main_musica(musica_nome, user)
            break # Sai do loop
           
            # mostra o menu da musica para o user, onde ele pode curtir, descurtir...
            print(main_musica())
            break # Sai do loop 
    else: # Se não encontrar a musica
        print("Música não encontrada.") # Mensagem de erro se a musica não for encontrada
        
def curtir_musica(nome_musica, user):
    """
    Função para curtir uma música.
    Atualiza o número de curtidas em musicas.txt e adiciona ao arquivo de curtidas do usuário.
    """
    caminho_musicas = "./arq_txt/musicas.txt"
    caminho_curtidas_user = f"./arq_txt/curtidas/curtidas_{user}.txt"
    caminho_descurtidas_user = f"./arq_txt/descurtidas/descurtidas_{user}.txt"

    with open(caminho_musicas, "r") as arquivo:
        conteudo = arquivo.readlines()

    encontrou = False
    for i, linha in enumerate(conteudo):
        musica_nome, musica_artista, musica_duracao, musica_genero, curtidas, descurtidas = linha.strip().split(",")
        if nome_musica.lower() == musica_nome.lower():
            # Atualiza o número de curtidas
            novas_curtidas = int(curtidas) + 1
            conteudo[i] = f"{musica_nome},{musica_artista},{musica_duracao},{musica_genero},{novas_curtidas},{descurtidas}\n"
            encontrou = True
            break

    if not encontrou:
        print("Música não encontrada.")
        return

    # Salva o novo conteúdo em musicas.txt
    with open(caminho_musicas, "w") as arquivo:
        arquivo.writelines(conteudo)

    try:
        with open(caminho_descurtidas_user, "r") as arquivo:
            musicas_descurtidas = [linha.strip().lower() for linha in arquivo.readlines()]
        musicas_descurtidas = [m for m in musicas_descurtidas if m.lower() != nome_musica.lower()]
        with open(caminho_descurtidas_user, "w") as arquivo:
            for m in musicas_descurtidas:
                arquivo.write(f"{m}\n")
    except FileNotFoundError:
        pass

    try:
        with open(caminho_curtidas_user, "r") as arquivo:
            musicas_curtidas = [linha.strip().lower() for linha in arquivo.readlines()]
    except FileNotFoundError:
        musicas_curtidas = []

    if nome_musica.lower() not in musicas_curtidas:
        with open(caminho_curtidas_user, "a") as arquivo:
            arquivo.write(f"{nome_musica}\n")
        print(f"Música '{nome_musica}' curtida com sucesso!")
    else:
        print(f"Você já curtiu a música '{nome_musica}'.")
    
    
def descurtir_musica(nome_musica,user):
    
    caminho_musicas = "./arq_txt/musicas.txt"
    caminho_curtidas_user = f"./arq_txt/curtidas/curtidas_{user}.txt"
    caminho_descurtidas_user = f"./arq_txt/descurtidas/descurtidas_{user}.txt"

    with open(caminho_musicas, "r") as arquivo:
        conteudo = arquivo.readlines()

    encontrou = False
    for i, linha in enumerate(conteudo):
        musica_nome, musica_artista, musica_duracao, musica_genero, curtidas, descurtidas = linha.strip().split(",")
        if nome_musica.lower() == musica_nome.lower():
            # Atualiza o número de curtidas
            novas_curtidas = max(0, int(curtidas) - 1)
            novas_descurtidas = int(descurtidas) + 1
            conteudo[i] = f"{musica_nome},{musica_artista},{musica_duracao},{musica_genero},{novas_curtidas},{novas_descurtidas}\n"
            encontrou = True
            break

    if not encontrou:
        print("Música não encontrada.")
        return

    # Salva o novo conteúdo em musicas.txt
    with open(caminho_musicas, "w") as arquivo:
        arquivo.writelines(conteudo)

    try:
        with open(caminho_curtidas_user, "r") as arquivo:
            musicas_curtidas = [linha.strip() for linha in arquivo.readlines()]
        musicas_curtidas = [m for m in musicas_curtidas if m.lower() != nome_musica.lower()]
        with open(caminho_curtidas_user, "w") as arquivo:
            for m in musicas_curtidas:
                arquivo.write(f"{m}\n")
    except FileNotFoundError:
        pass


    # Adiciona à lista de descurtidas, se ainda não estiver
    try:
        with open(caminho_descurtidas_user, "r") as arquivo:
            musicas_descurtidas = [linha.strip().lower() for linha in arquivo.readlines()]
    except FileNotFoundError:
        musicas_descurtidas = []

    if nome_musica.lower() not in musicas_descurtidas:
        with open(caminho_descurtidas_user, "a") as arquivo:
            arquivo.write(f"{nome_musica}\n")
        print(f"Música '{nome_musica}' descurtida com sucesso!")
    else:
        print(f"Você já descurtiu a música '{nome_musica}'.")

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
    nome_playlist = "playlist_"+user+"_"+nome_playlist
    caminho_playlist = f"./arq_txt/playlists/{nome_playlist}.txt"
    with open(caminho_playlist, "w") as arquivo_playlists:
        arquivo_playlists.write(f"\n")
        print(f"Playlist '{nome_playlist}' criada com sucesso!")
        print("Adicione músicas à sua playlist (digite 'fim' para parar):")
        while True:
            musica = input("Nome da música: ").strip()
            if musica.lower() == "fim":
                break
            arquivo_playlists.write(f"{musica}\n")
        print("Músicas adicionadas à playlist!")

    # adicona nome da playlist ao arq txt contendo todas as playlists do user
    nome_arq_txt_todas_as_playlists = f"playlists_{user}"
    caminho_playlist_arq_txt_todas_as_playlists = f"./arq_txt/playlists/{nome_arq_txt_todas_as_playlists}.txt"
    with open(caminho_playlist_arq_txt_todas_as_playlists, "w") as arq_txt_todas_as_playlists:
        arq_txt_todas_as_playlists.write(f"{nome_playlist}\n")

def mostrar_musicas_playlist(nome_playlist):
    caminho_playlist = f"./arq_txt/playlists/{nome_playlist}.txt"
    try:
        with open(caminho_playlist, "r") as arquivo:
            linhas = arquivo.readlines()
        print(f"Músicas da playlist '{nome_playlist}':")
        for musica in linhas[1:]:  # pula a primeira linha (nome da playlist)
            print(musica.strip())
    except FileNotFoundError:
        print("Playlist não encontrada.")

def adicionar_musica(nome_playlist):
    caminho_playlist = f"../arq_txt/playlists/{nome_playlist}.txt"
    nome_musica = input("Digite o nome da musica que deseja adicionar: ")
    with open(caminho_playlist, "a") as arquivo:
        arquivo.write(f"{nome_musica}\n")
    print(f"Música '{nome_musica}' adicionada à playlist!")

def remover_musica(nome_playlist):
    caminho_playlist = f"./arq_txt/playlists/{nome_playlist}.txt"
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
    playlists = f"./arq_txt/playlists/playlists_{user}.txt"
    # [f for f in os.listdir("./arq_txt/playlists/") if f.startswith("playlists"+"_"+user) and f.endswith(".txt")]




    try:
        with open(playlists, "r") as arquivo:
            linhas = arquivo.readlines()
        print(f"Músicas da playlist '{playlists}':")
        for musica in linhas:
            print(musica.replace(".txt", ""))
    except FileNotFoundError:
        print("Playlist não encontrada.")
        return
    nomeInput = input("Digite o nome da playlist que deseja gerenciar: ").strip()
    nome = "playlist_"+user+"_"+nomeInput
    if not os.path.exists(f"./arq_txt/playlists/{nome}.txt"):
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