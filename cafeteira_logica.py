import estoque.itens_estoque as itens_estoque # Importando o seu módulo de estoque

carrinho = []
total_conta = 0.0

print("----- Bem-Vindo à Cafeteria Inteligente! -----")

while True:
    print("\n=========================")
    print("      MENU PRINCIPAL      ")
    print("=========================")
    print("1. Ver Menu de Cafés")
    print("2. Ver Carrinho e Finalizar Compra")
    print("3. Sair")
    print("4. Ver Estoque (Admin)")
    
    escolha = input("\nDigite o número da opção desejada: ").strip()

    if escolha == "1":
        # Criamos um loop interno exclusivo para o menu de cafés. 
        # Assim, o 'break' aqui dentro apenas VOLTA para o menu principal!
        while True:
            print("\n------ CAFÉS DISPONÍVEIS ------")
            # Exibe os cafés dinamicamente com base no estoque real e no que já está no carrinho
            for cafe, qtd_total in itens_estoque.estoque.items():
                qtd_disponivel = qtd_total - carrinho.count(cafe)
                print(f"- {cafe}: R$ {itens_estoque.precos[cafe]:.2f} ({qtd_disponivel} unid. disponíveis)")
            
            print("\n[1] Cappuccino | [2] Latte | [3] Espresso | [4] Mocha | [V] Voltar ao Menu Principal")
            opcao = input("\nEscolha o café desejado ou digite 'V': ").strip().lower()
            if opcao == "v":
                print("Saiu com sucesso do menu")
                break

            # Mapeamento da escolha do usuário para o nome do café
            cafes_mapeados = {"1": "Cappuccino", "2": "Latte", "3": "Espresso", "4": "Mocha"}
            
            if opcao in cafes_mapeados:
                nome_cafe = cafes_mapeados[opcao]
                
                # Validação usando sua lógica de estoque temporário/disponível
                if (itens_estoque.estoque[nome_cafe] - carrinho.count(nome_cafe)) > 0:
                    carrinho.append(nome_cafe)
                    total_conta += itens_estoque.precos[nome_cafe]
                    print(f"✅ {nome_cafe} adicionado ao carrinho!")
                else:
                    print(f"❌ Desculpe, o estoque de {nome_cafe} esgotou para este pedido!")
                
            else:
                print("❌ Opção inválida. Escolha de 1 a 4, ou 'v' para voltar.")

    elif escolha == "2":
        print("\n---- SEU CARRINHO ----")
        if not carrinho:
            print("Seu carrinho está vazio!")
        else:
            # Lista os itens sem repetir linhas, mostrando a quantidade
            for cafe in set(carrinho):
                print(f"• {cafe}: {carrinho.count(cafe)} unid. (R$ {itens_estoque.precos[cafe] * carrinho.count(cafe):.2f})")
            print(f"----------------------")
            print(f"Total a Pagar: R$ {total_conta:.2f}")

            opcao_finalizar = input("\nDigite 'Sim' para finalizar ou 'Não' para voltar: ").strip().lower()

            if opcao_finalizar in ["sim", "s"]:
                # MOMENTO 2: Agora sim, damos a baixa definitiva no estoque real!
                for item in set(carrinho):
                    itens_estoque.estoque[item] -= carrinho.count(item)
                
                print("🎉 Compra finalizada com sucesso! Seu café começará a ser preparado.")
                carrinho.clear()
                total_conta = 0.0
            else:
                print("🔄 Voltando ao menu principal. Seus itens continuam salvos no carrinho.")

    elif escolha == "3": 
        print("Obrigado por visitar a Cafeteria Inteligente! Volte sempre! 👋")
        break

    elif escolha == "4":
        print("\n🔒 Acesso restrito ao administrador.")
        admin = input("Digite a senha de administrador: ").strip()
        
        if admin == "admin123":
            print("\n----- ESTOQUE ATUAL REAL -----")
            for cafe, quantidade in itens_estoque.estoque.items():
                print(f"• {cafe}: {quantidade} unidades")
        else:
            print("❌ Senha incorreta. Acesso negado.")
    else:
        print("❌ Opção inválida no menu principal. Escolha de 1 a 4.")