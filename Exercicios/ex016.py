from math import trunc

# Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira.

#r = float(input('Digite um numero quebrado: '))
#print(
  #  f'O número inteiro acima é {math.ceil(r)};\n'    Modo que eu fiz
 #   f'O número inteiro abaixo é {math.floor(r)}.'
#)

num = float(input('Digite um Numero Real: '))

print(                                               #Correção
    f'O numero inteiro é {trunc(num)}'
)