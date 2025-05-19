from cadastro_login import sair()

# arquivo com as funcionalidades dos adms

menu = {
    0: "sair",
    1: "adicionar musicas",
    2: "consultar usuarios", 
    3: "excluir musicas",
    4: "cadastrar artistas",
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
            add_musicas() # Chama a função 
        elif escolha == 2: 
            consultar_users() # Chama a função 
        elif escolha == 3: 
            excluir_musicas() # Chama a função 
        elif escolha == 4: 
            cadastrar_artistas() # Chama a função 
        elif escolha == 0: # Sair
            sair() # Chama a função sair
        else:
            print("Opção inválida. Tente novamente.") # Mensagem de erro para opção inválida
