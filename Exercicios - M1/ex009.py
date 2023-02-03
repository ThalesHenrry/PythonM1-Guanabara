# Faça um programa que leia um númnero inteiro qualquer e mostre na tela sua tabuada.

num = int(input('Escolha um número para tabuada: '))

print(
    f'- Tabuada do {num} -\n'
    f'{num} x 1 = {num * 1}\n'
    f'{num} x 2 = {num * 2}\n'
    f'{num} x 3 = {num * 3}\n'
    f'{num} x 4 = {num * 4}\n'
    f'{num} x 5 = {num * 5}\n'
    f'{num} x 6 = {num * 6}\n'
    f'{num} x 7 = {num * 7}\n'
    f'{num} x 8 = {num * 8}\n'
    f'{num} x {9:2} = {num * 9}\n'
    f'{num} x 10 = {num * 10}'
)
