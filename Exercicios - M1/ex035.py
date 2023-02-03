#Desenvolva um programa que leia o comprimento de 3 retas e diga ao usuáriose elas podem ou não formar um triângulo.

linha1 = float(input('Comprimento da 1º linha: '))
linha2 = float(input('Comprimento da 2º linha: '))
linha3 = float(input('Comprimento da 3º linha: '))

prova1 = (linha1 > abs(linha2-linha3)) and (linha1 < abs(linha2+linha3)) and \
         (linha2 > abs(linha1-linha3)) and (linha2 < abs(linha1+linha3)) and \
         (linha3 > abs(linha1-linha2)) and (linha3 < abs(linha1+linha2))

if prova1 == True:
    print(
        f'Possivel formar um Triângulo!'
    )
else:
    print(
        f'Impossivel formar um Triângulo!'
    )


