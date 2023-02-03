
# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

num = int(input('Digite um número: '))
num_dobro = (num*2)
num_triplo = (num*3)
num_rq = (num**(1/2))

print(
    f'O número inteiro é {num}!\n'
    f'O seu dobro é {num_dobro};\n'
    f'O seu triplo é {num_triplo};\n'
    f'Sua raiz quadrada é {num_rq:.2f}.\n'
)
