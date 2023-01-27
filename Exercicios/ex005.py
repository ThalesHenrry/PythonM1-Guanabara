# Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor.

num = int(input('Digite um número:'))
numero_antecessor = (num - 1)
numero_sucessor = (num + 1)

print(
    f'O Número escolhido foi {num}!\n'
    f'Seu antecessor é {numero_antecessor};\n'
    f'Seu sucessor é {numero_sucessor}.'
)
