#Faça um programa que leia 3 números e mostre qual é o maior e qual é o menor.

num1 = int(input('Escolha o 1º número: '))
num2 = int(input('Escolha o 2º número: '))
num3 = int(input('Escolha o 3º número: '))

maior = num1
menor = num1

#MAIOR
if (num2 > maior):
    maior = num2
if (num3 > maior):
    maior = num3

#MENOR
if (num2 < menor):
    menor = num2
if (num3 < menor):
    menor = num3


print(
    f'Maior Número: {maior}\n'
    f'Menor Número: {menor}\n'
)