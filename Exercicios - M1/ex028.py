from random import choice    #Da pra usar o randint
from time import sleep

#Escreva um programa que faça o computador 'pensar' em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
#O programa deverá escrever na tela se o usuário venceu ou perdeu.

numeros = [0, 1, 2, 3, 4, 5]        #numero = randint(0, 5) - Dá pra usar essa opção
numC = str(choice(numeros))

escolha = input('Escolha um número de 1 á 5: ')

print('Processando...')
sleep(1)                   #Sleep, faz aparecer uma mensagem por tempo definido.

if escolha == numC:
    print(f'Parabéns, você é o vencedor!\n'
          f'Número sorteado ({numC})')
else:
    print(f'Que pena, você perdeu.\n'
          f'O número correto é ({numC})')

