# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo todas as informações possiveis sobre ela.


algo = input('digite algo: ')

print('O tipo primitivo desse valor é {}'.format(type(algo)))
print('Só tem espaços?', algo.isspace())
print('É um número?', algo.isnumeric())
print('É alfabético?', algo.isalpha())
print('É alfanumérico?', algo.isalnum())
print(f'Está em maiúsculo? {algo.isupper()}')
print(f'Está em minúsculo? {algo.islower()}')
print('Está capitalizada? {}'.format(algo.istitle()))



