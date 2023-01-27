import math

# Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira.

r = float(input('Digite um numero quebrado: '))
print(
    f'O número inteiro acima é {math.ceil(r)};\n'
    f'O número inteiro abaixo é {math.floor(r)}.'
)