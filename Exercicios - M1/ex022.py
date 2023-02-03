#Crie um programa que leia o nome completo de uma pessoa e mostre:
# O nome com toda letra maiúscula;
# Outro com letra minúscula;
# Contar todas a letras sem os epaços;
# E quantas letras tem o primeiro nome.

nome = input('Escreva o seu nome completo: ')
null = (nome.split())
cont = ''.join(null)

print(
    f'Nome: {nome}\n'
    f'Nome em Maisculo: {nome.upper()}\n'
    f'Nome em Minusculo: {nome.lower()}\n'
    f'Quantidade de Char, sem espaço: {len(cont)}\n'
    f'Quantidade de Char, primeiro nome: {len(null[0])}'
)