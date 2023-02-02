# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "Santo".

cid = input('Digite o nome de sua cidade: ')
cid1 = cid[:5]
analise = ("Santo" in cid1)

print(
    f'A cidade digitada começa com Santo? TRUE ou FALSE\n'
    f'Cidade: {cid}\n'
    f'Resposta: {analise}'
)