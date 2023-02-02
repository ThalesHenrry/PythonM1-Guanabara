#Crie um programa que leia um número inteiro e mostre na tela se ele é Par ou Impar.

num = int(input('Ecolha um numero inteiro: '))

if num % 2 == 0:
    print(f'Número escolhido: {num} é Par.')
else:
    print(f'Número escolhido: {num} é Impar')
