# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos digitos separado.

num = (input('Digite um número de 0 a 9999: '))
s = '000' + num

print(
    f'Número digitado: {num}\n'
    f'Unidade: {s[-1]}\n'
    f'Dezena:  {s[-2]}\n'
    f'Centena: {s[-3]}\n'
    f'Milhar:  {s[-4]}'
)
