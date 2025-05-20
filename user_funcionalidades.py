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

def main_usuario():
    """
    Função principal que exibe o menu e chama as funções correspondentes
    de acordo com a escolha do usuário.
    """
    while True: # Loop infinito
        escolha = exibir_menu_usuario() # Chama a função exibir_menu e armazena a escolha do usuário
        if escolha == 1: # Buscar musicas
            buscar_musicas() # Chama a função buscar_musicas
        elif escolha == 2: # Gerenciar playlist
            gerenciar_playlist() # Chama a função gerenciar_playlist
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
    # Aqui você pode implementar a lógica para buscar musicas
    # Exemplo: input para o usuário digitar o nome da musica
    nome_musica = input("Digite o nome da musica: ")
    print(f"Buscando a musica: {nome_musica}")
    # Aqui você pode adicionar a lógica para buscar a musica no banco de dados ou na lista de musicas
    
def gerenciar_playlist():
    """
    Função para gerenciar playlist.
    """
    print("Gerenciar playlist:")
    # Aqui você pode implementar a lógica para gerenciar a playlist
    with open("playlists.txt", "r") as arquivo_playlists: 
        playlists = arquivo_playlists.readlines()
    
    print("Playlists disponíveis:")
    for nome in playlists:
        print(f"- {nome}")

    nome_playlist = input("Digite o nome da playlist que deseja gerenciar: ").strip()
    if nome_playlist not in playlists:
        print("Playlist não encontrada. Tente novamente.")
        return
    
   
    
    # Exemplo: adicionar ou remover musicas da playlist
    acao = input("Digite 'adicionar' para adicionar uma musica ou 'remover' para remover uma musica: ")
    if acao == "adicionar":
        nome_musica = input("Digite o nome da musica que deseja adicionar: ")
        print(f"Adicionando a musica: {nome_musica} à sua playlist")
        add_musicas_playlist = open("musicas_playlist.txt", "a")
        add_musicas_playlist.write(f"{nome_musica}\n")
        add_musicas_playlist.close()
        print("Música adicionada com sucesso!")
         
    elif acao == "remover":
        nome_musica = input("Digite o nome da musica que deseja remover: ")
        remove_musicas_playlist = open("musicas_playlist.txt", "r")
        musicas = remove_musicas_playlist.readlines()
        remove_musicas_playlist.close()
        # Remove a música desejada
        musicas = [musica for musica in musicas if musica.strip() != nome_musica]
        # Salva novamente a lista sem a música removida
        salva_playlist = open("musicas_playlist.txt", "w")
        salva_playlist.writelines(musicas)
        salva_playlist.close()
        print(f"Música '{nome_musica}' removida da sua playlist.")
        
    else:
        print("Ação inválida. Tente novamente.")
        
def visualizar_historico():
    """
    Função para visualizar o histórico de musicas.
    """
    print("Visualizar histórico:")
    # Aqui você pode implementar a lógica para visualizar o histórico de musicas
    # Exemplo: visualizar musicas curtidas 
    visualizar_historico = input("Digite 'curtidas' para ver as musicas curtidas ou 'descurtidas' para ver todas as musicas descurtidas: ")
    
    if visualizar_historico == "curtidas":
        print("Mostrando musicas curtidas:")
        # Aqui você pode adicionar a lógica para mostrar as musicas curtidas : 
        musicas_curtidas = open("musicas_curtidas.txt", "r")
        for musica in musicas_curtidas:
            print(musica.strip())
    elif visualizar_historico == "descurtidas":
        print("Mostrando musicas descurtidas:")
        # Aqui você pode adicionar a lógica para mostrar as musicas descurtidas : 
        musicas_descurtidas = open("musicas_descurtidas.txt", "r")
        for musica in musicas_descurtidas:
            print(musica.strip())
            
    else:
        print("Opção inválida. Tente novamente.")
        
def sair():
    """
    Função para sair do programa.
    """
    print("Saindo do programa...")
    exit() # Encerra o programa