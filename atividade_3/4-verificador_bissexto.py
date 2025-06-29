def verificar_ano_bissexto():
    
    try:
        ano = int(input("Digite um ano para verificar se é bissexto: "))

        if ano < 0:
            print("Ano inválido. Por favor, digite um ano positivo.")
            return

        if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
            print(f"O ano {ano} é bissexto.")
        else:
            print(f"O ano {ano} não é bissexto.")
    except ValueError:
        print("Entrada inválida. Por favor, digite um número inteiro para o ano.")

verificar_ano_bissexto()