def verificar_palindromo(texto: str) -> str:
    texto_formatado = ''.join(c.lower() for c in texto if c.isalnum())
    if texto_formatado == texto_formatado[::-1]:
        return "Sim"
    else:
        return "Não"

# Exemplos de uso
print(verificar_palindromo("Ame a ema"))
print(verificar_palindromo("Olá mundo"))