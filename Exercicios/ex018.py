from math import sin, cos, tan, radians
#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

ang = float(input('Digite o ângulo: '))
sen = sin(radians(ang))
cos = cos(radians(ang))
tan = tan(radians(ang))

print(
    f'O ângulo é de {ang}º\n'
    f'Seno: {sen:.2f}\n'
    f'Coseno: {cos:.2f}\n'
    f'Tangente: {tan:.2f}'
)