def calcular_imc():

    try:
        peso = float(input("Por favor, digite seu peso em kg: "))
        altura = float(input("Por favor, digite sua altura em metros (ex: 1.75): "))

        if peso <= 0 or altura <= 0:
            print("Peso e altura devem ser valores positivos.")
            return

        imc = peso / (altura ** 2)
        classificacao = ""

        if imc < 18.5:
            classificacao = "Abaixo do peso"
        elif imc < 25:
            classificacao = "Peso normal"
        elif imc < 30:
            classificacao = "Sobrepeso"
        else:
            classificacao = "Obeso"

        print(f"Seu IMC é: {imc:.2f}")
        print(f"Classificação: {classificacao}")
    except ValueError:
        print("Entrada inválida. Por favor, digite números válidos para peso e altura.")

calcular_imc()