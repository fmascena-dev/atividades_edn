def calcular_preco_final_com_desconto():
    
    try:
        preco_original = float(input("Digite o preço original do produto: R$ "))
        porcentagem_desconto = float(input("Digite a porcentagem de desconto (ex: 15 para 15%): "))

        if preco_original < 0 or porcentagem_desconto < 0:
            print("Preço e porcentagem de desconto devem ser valores positivos.")
            return

        valor_desconto = preco_original * (porcentagem_desconto / 100)
        preco_final = preco_original - valor_desconto

        print(f"\nPreço Original: R${preco_original:.2f}")
        print(f"Desconto Aplicado: R${valor_desconto:.2f} ({porcentagem_desconto:.2f}%)")
        print(f"Preço Final com Desconto: R${preco_final:.2f}")

    except ValueError:
        print("Entrada inválida. Por favor, digite números válidos para o preço e a porcentagem.")

calcular_preco_final_com_desconto()