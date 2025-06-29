def converter_temperatura():
    
    try:
        temperatura = float(input("Digite a temperatura: "))
        unidade_origem = input("Qual a unidade de origem (C, F, K)? ").upper()
        unidade_destino = input("Para qual unidade deseja converter (C, F, K)? ").upper()

        if unidade_origem not in ['C', 'F', 'K'] or unidade_destino not in ['C', 'F', 'K']:
            print("Unidades inválidas. Use C para Celsius, F para Fahrenheit ou K para Kelvin.")
            return

        temp_em_celsius = 0.0

        if unidade_origem == 'C':
            temp_em_celsius = temperatura
        elif unidade_origem == 'F':
            temp_em_celsius = (temperatura - 32) * 5/9
        elif unidade_origem == 'K':
            temp_em_celsius = temperatura - 273.15

        resultado = 0.0
        if unidade_destino == 'C':
            resultado = temp_em_celsius
        elif unidade_destino == 'F':
            resultado = (temp_em_celsius * 9/5) + 32
        elif unidade_destino == 'K':
            resultado = temp_em_celsius + 273.15

        print(f"A temperatura convertida é: {resultado:.2f} {unidade_destino}")

    except ValueError:
        print("Entrada inválida. Por favor, digite um número para a temperatura.")

converter_temperatura()