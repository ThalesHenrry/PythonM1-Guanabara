from random import shuffle
# O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

aluno1 = input('Nome do 1º aluno: ')
aluno2 = input('Nome do 2º aluno: ')
aluno3 = input('Nome do 3º aluno: ')
aluno4 = input('Nome do 4º aluno: ')

lista = [aluno1, aluno2, aluno3, aluno4]
shuffle(lista)

print(
    f'A ordem de apresentação é: \n'
    f'{lista}'
)