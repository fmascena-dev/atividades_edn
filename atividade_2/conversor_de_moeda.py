valor_reais = 100.00
taxa_dolar = 5.20
taxa_euro = 6.15

valor_dolar = valor_reais / taxa_dolar
valor_euro = valor_reais / taxa_euro

print(f"Valor em Reais: R$ {valor_reais:.2f}")
print(f"Taxa do Dólar: R$ {taxa_dolar:.2f}")
print(f"Taxa do Euro: R$ {taxa_euro:.2f}\n")

print(f"Valor convertido para Dólar: ${valor_dolar:.2f}")
print(f"Valor convertido para Euro: €{valor_euro:.2f}")