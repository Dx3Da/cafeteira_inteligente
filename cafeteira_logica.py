import estoque.itens_estoque as itens_estoque

carrinho = []
total_conta = 0.0

print(f"-----Bem-Vindo à Cafeteria Inteligente!-----")


while True:

    print(f"""
          Menu de Seleção:
          1. Ver Menu de Cafés
          2. Ver Carrinho e Finalizar Compra
          3. Sair
          4. Ver Estoque
          """)
    escolha = input("Digite o numero da opção desejada:...").strip()

    if escolha == "1":
        # Exibir menu de cafes/ Precos
        for cafe, quantidade in itens_estoque.estoque.items():
            if itens_estoque.estoque[cafe] > 0:
                print(f""" 
                      ------ Cafes disponiveis: ------
                      Selecione o numero do cafe que deseja adicionar ao carrinho:
                      1. Cappuccino - R${itens_estoque.precos['Cappuccino']:.2f}
                      2. Latte - R${itens_estoque.precos['Latte']:.2f}
                      3. Espresso - R${itens_estoque.precos['Espresso']:.2f}
                      4. Mocha - R${itens_estoque.precos['Mocha']:.2f}
                      v - Voltar ao menu
                      """)

                opcao = input(
                    "Escolha o cafe que deseja e digite Voltar(para retornar ao menu) ou Carrinho (Para ver o carrinho)").lower()

                if opcao == "1":
                    cafe = "Cappuccino"
                    carrinho.append(cafe)
                    total_conta += itens_estoque.precos[cafe]
                    itens_estoque.estoque[cafe] -= 1
                    print(f"🍫 1. {cafe} adicionado ao carrinho.")

                elif opcao == "2":
                    cafe = "Latte"
                    carrinho.append(cafe)
                    total_conta += itens_estoque.precos[cafe]
                    itens_estoque.estoque[cafe] -= 1
                    print(f"🥛 1. {cafe} adicionado ao carrinho.")

                elif opcao == "3":
                    cafe = "Espresso"
                    carrinho.append(cafe)
                    total_conta += itens_estoque.precos[cafe]
                    itens_estoque.estoque[cafe] -= 1
                    print(f"☕ 1. {cafe} adicionado ao carrinho.")

                elif opcao == "4":
                    cafe = "Mocha"
                    carrinho.append(cafe)
                    total_conta += itens_estoque.precos[cafe]
                    itens_estoque.estoque[cafe] -= 1
                    print(f"🥐 1. {cafe} adicionado ao carrinho.")

                elif opcao == "v":
                    break

                else:
                    print("Opção inválida. Por favor, escolha novamente.")

    elif escolha == "2":
        # Exibir o carrinho e o total da conta
        print("---- Carrinho: ----")
        for cafe in carrinho:
            print(f"{cafe}: R${itens_estoque.precos[cafe]:.2f}")
        print(f"Total a Pagar: R${total_conta:.2f}")

        opcao_finalizar = input(
            "Digite Sim para finalizar a compra ou Não para voltar ao menu: ").lower()

        if opcao_finalizar == "sim":
            print("Compra finalizada com sucesso!")
            carrinho.clear()
            total_conta = 0.0
        elif opcao_finalizar == "não" or opcao_finalizar == "nao":
            break

    elif escolha == "3": 
        print("Obrigado por visitar a Cafeteria Inteligente! Volte sempre!")
        break

    elif escolha == "4":
        print("Acesso ao estoque requer senha de administrador.")
        admin = input("Digite a senha de administrador para acessar o estoque: ")
        if admin == "admin123":
            print("----- Estoque Atual -----")
            for cafe, quantidade in itens_estoque.estoque.items():
                print(f"{cafe}: {quantidade} unidades")
        else:
            print("Senha incorreta. Acesso negado.")
        break
    else:
        print("Opção inválida. Por favor, escolha novamente.")

