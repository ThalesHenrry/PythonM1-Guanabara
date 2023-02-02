#Faça um programa que leia um ano qualque e mostre se ele é Bissexto.

ano = int(input('Escolha um ano: '))

if (ano % 400 == 0) and (ano % 100 == 0):
    print(
        f'Ano escolhido: {ano}\n'
        f'É um ano Bissexto!'
    )
else:
    print(
        f'Ano escolhido: {ano}\n'
        f'Não é um ano Bissexto!'
    )