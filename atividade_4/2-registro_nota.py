def calcular_media_turma():
    
    notas = []
    while True:
        try:
            nota_str = input("Digite a nota do aluno (ou 'fim' para encerrar): ")
            if nota_str.lower() == 'fim':
                break
            nota = float(nota_str)
            if 0 <= nota <= 10:
                notas.append(nota)
            else:
                print("Nota inválida. Por favor, digite uma nota entre 0 e 10.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número para a nota ou 'fim'.")

    if not notas:
        print("Nenhuma nota foi inserida.")
    else:
        media = sum(notas) / len(notas)
        print(f"\nNotas registradas: {notas}")
        print(f"A média da turma é: {media:.2f}")

calcular_media_turma()