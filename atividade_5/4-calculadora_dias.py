from datetime import datetime

def calcular_dias_vivo():
    
    try:
        data_nascimento_str = input("Digite sua data de nascimento (DD-MM-AAAA): ")
        data_nascimento = datetime.strptime(data_nascimento_str, "%d-%m-%Y")

        data_atual = datetime.now()

        if data_nascimento > data_atual:
            print("A data de nascimento não pode ser no futuro.")
            return

        diferenca = data_atual - data_nascimento
        dias_vivos = diferenca.days

        print(f"Você está vivo(a) há aproximadamente {dias_vivos} dias.")

    except ValueError:
        print("Formato de data inválido. Por favor, use o formato DD-MM-AAAA (ex: 27-06-1990).")

calcular_dias_vivo()