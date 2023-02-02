#Crie um programa que leia o nome de uma pessoa e diga se ela tem "Silva" no nome.

nome = input('Digite seu nome completo: ')
anl = ('Silva' in nome)

print(
    f'O nome digitado tem "Silva"? True ou False\n'
    f'Nome: {nome}\n'
    f'Resposta: {anl}'
)