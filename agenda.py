def adicionar_contato(contatos):
    nome = input("Digite o nome: ")
    telefone = input("Digite o telefone: ")
    email = input("Digite o email: ")
    favorito = input("Marcar como favorito? (s/n): ").lower() == "s"

    contato = {"nome": nome, "telefone": telefone, "email": email, "favorito": favorito}

    contatos.append(contato)
    print(f"Contato {nome} adicionado com sucesso!")


def visualizar_contatos(contatos):
    if not contatos:
        print("Nenhum contato cadastrado.")
    else:
        for idx, contato in enumerate(contatos, start=1):
            favorito = " (Favorito)" if contato["favorito"] else ""
            print(
                f"{idx}. {contato['nome']} - {contato['telefone']} - {contato['email']}{favorito}"
            )


def editar_contato(contatos):
    visualizar_contatos(contatos)
    try:
        idx = int(input("Escolha o número do contato para editar: ")) - 1
        if 0 <= idx < len(contatos):
            contato = contatos[idx]
            print("Deixe o campo vazio para não alterar.")
            novo_nome = input(f"Nome ({contato['nome']}): ") or contato["nome"]
            novo_telefone = (
                input(f"Telefone ({contato['telefone']}): ") or contato["telefone"]
            )
            novo_email = input(f"Email ({contato['email']}): ") or contato["email"]

            contato["nome"] = novo_nome
            contato["telefone"] = novo_telefone
            contato["email"] = novo_email

            print(f"Contato {novo_nome} editado com sucesso!")
        else:
            print("Contato não encontrado.")
    except ValueError:
        print("Entrada inválida!")


def favoritar_contato(contatos):
    visualizar_contatos(contatos)
    try:
        idx = (
            int(input("Escolha o número do contato para favoritar/desfavoritar: ")) - 1
        )
        if 0 <= idx < len(contatos):
            contato = contatos[idx]
            contato["favorito"] = not contato["favorito"]
            status = "favoritado" if contato["favorito"] else "desfavoritado"
            print(f"Contato {contato['nome']} {status} com sucesso!")
        else:
            print("Contato não encontrado.")
    except ValueError:
        print("Entrada inválida!")


def ver_favoritos(contatos):
    favoritos = [c for c in contatos if c["favorito"]]
    if not favoritos:
        print("Nenhum contato favorito.")
    else:
        for idx, contato in enumerate(favoritos, start=1):
            print(
                f"{idx}. {contato['nome']} - {contato['telefone']} - {contato['email']} (Favorito)"
            )


def apagar_contato(contatos):
    visualizar_contatos(contatos)
    try:
        idx = int(input("Escolha o número do contato para apagar: ")) - 1
        if 0 <= idx < len(contatos):
            contato = contatos.pop(idx)
            print(f"Contato {contato['nome']} apagado com sucesso!")
        else:
            print("Contato não encontrado.")
    except ValueError:
        print("Entrada inválida!")


contatos = []

while True:
    print("\n===== AGENDA DE CONTATOS =====")
    print("1. Adicionar Contato")
    print("2. Visualizar Contatos")
    print("3. Editar Contato")
    print("4. Favoritar/Desfavoritar Contato")
    print("5. Ver Contatos Favoritos")
    print("6. Apagar Contato")
    print("0. Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        adicionar_contato(contatos)
    elif opcao == "2":
        visualizar_contatos(contatos)
    elif opcao == "3":
        editar_contato(contatos)
    elif opcao == "4":
        favoritar_contato(contatos)
    elif opcao == "5":
        ver_favoritos(contatos)
    elif opcao == "6":
        apagar_contato(contatos)
    elif opcao == "0":
        print("Saindo da agenda...")
        break
    else:
        print("Opção inválida! Tente novamente.")
