def analisar_numeros():
    
    numeros_pares = 0
    numeros_impares = 0

    while True:
        try:
            entrada = input("Digite um número (ou 'fim' para encerrar): ")
            if entrada.lower() == 'fim':
                break
            
            numero = int(entrada)
            if numero % 2 == 0:
                print(f"{numero} é um número PAR.")
                numeros_pares += 1
            else:
                print(f"{numero} é um número ÍMPAR.")
                numeros_impares += 1
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro ou 'fim'.")

    print(f"\n--- Resumo ---")
    print(f"Total de números pares inseridos: {numeros_pares}")
    print(f"Total de números ímpares inseridos: {numeros_impares}")

analisar_numeros()