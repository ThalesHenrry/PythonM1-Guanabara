from datetime import date
#Faça um programa que leia um ano qualque e mostre se ele é Bissexto.

ano = int(input('Que ano quer analisar? Se for o atual coloque: 0: '))

if ano == 0:
    ano = date.today().year  # Pegar apenas o ano do dia de hoje!

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