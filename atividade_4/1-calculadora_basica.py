def calculadora():

    try:
        num1 = float(input("Digite o primeiro número: "))
        operador = input("Digite o operador (+, -, *, /): ")
        num2 = float(input("Digite o segundo número: "))

        resultado = 0
        if operador == '+':
            resultado = num1 + num2
        elif operador == '-':
            resultado = num1 - num2
        elif operador == '*':
            resultado = num1 * num2
        elif operador == '/':
            if num2 == 0:
                print("Erro: Divisão por zero não é permitida.")
                return
            resultado = num1 / num2
        else:
            print("Operador inválido. Por favor, use +, -, * ou /.")
            return

        print(f"O resultado é: {resultado}")
    except ValueError:
        print("Entrada inválida. Por favor, digite números válidos.")

calculadora()