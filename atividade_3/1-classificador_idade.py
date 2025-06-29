def classificar_idade():
    
    try:
        idade = int(input("Por favor, digite sua idade: "))
        
        if idade < 0:
            print("Idade inválida. A idade não pode ser negativa.")
        elif idade <= 12:
            print("Você é uma criança.")
        elif idade <= 17:
            print("Você é um adolescente.")
        elif idade <= 59:
            print("Você é um adulto.")
        else:
            print("Você é um idoso.")
    except ValueError:
        print("Entrada inválida. Por favor, digite um número inteiro válido.")

classificar_idade()