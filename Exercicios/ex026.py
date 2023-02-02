#Faça um programa que leia uma frase pelo teclado e mostre:
#Quantas vezes aparece a letra 'A';
#Em que posição aparece na primeia e ultima ves.

frase = input('Escreva uma frase: ')
contagem = (frase.count('a'))
pos1 = (frase.find('a'))
pos2 = (frase.rfind('a'))

print(
    f'Frase: {frase}\n'
    f'Quantas vezes aparece a letra (A): {contagem}\n'
    f'Posição da 1ª letra (A): {pos1}\n'
    f'Posição da Ultima letra (A): {pos2}'
)