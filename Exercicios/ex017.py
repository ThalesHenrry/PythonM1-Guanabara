import math

# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre
# o comprimento da hipotenusa.

#co = float(input('Comprimento do cateto oposto: '))
#ca = float(input('Comprimento do cateto adjacente: '))
#hi = (co**2 + ca**2)**(1/2)                            Que eu fiz

#print(
 #   f'O comprimento do Hipotnusa é: {hi:.2f}'
#)

co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = (math.hypot(co, ca))                              #Correção

print(
    f'O comprimento da Hipotenusa é: {hi:.2f}'
)