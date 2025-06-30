def verificar_senha():
    
    senha = input("Digite sua senha: ")

    if len(senha) < 8:
        print("Senha fraca: deve ter pelo menos 8 caracteres.")
        return False

    tem_numero = False
    for caractere in senha:
        if caractere.isdigit():
            tem_numero = True
            break
    
    if not tem_numero:
        print("Senha fraca: deve conter pelo menos um número.")
        return False

    print("Senha forte o suficiente! Atende aos critérios de segurança.")
    return True

verificar_senha()