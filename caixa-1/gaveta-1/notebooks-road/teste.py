def calcular_media_notas():
    try:
        quantidade = int(input('Quantas notas deseja informar? '))
        if quantidade <= 0:
            print('Informe um número inteiro maior que zero.')
            return
    except ValueError:
        print('Valor inválido. Informe um número inteiro.')
        return

    notas = []
    for i in range(1, quantidade + 1):
        try:
            nota = float(input(f'Nota {i}: '))
            notas.append(nota)
        except ValueError:
            print('Valor inválido. Informe uma nota numérica.')
            return

    media = sum(notas) / quantidade
    print(f'Média das notas: {media:.2f}')


if __name__ == '__main__':
    calcular_media_notas()