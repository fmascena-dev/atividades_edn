def calcular_gorjeta(valor_conta: float, porcentagem_gorjeta: float) -> float:
    gorjeta = (valor_conta * porcentagem_gorjeta) / 100
    return round(gorjeta, 2)

print("Valor da gorjeta:", calcular_gorjeta(359, 10))  # Saída: 10.0
