# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "Santo".

cid = str(input('Digite o nome de sua cidade: ')).strip()
cid1 = cid[:5].strip().title()
analise = ("Santo" in cid1)

print(
    f'A cidade digitada começa com Santo? TRUE ou FALSE\n'
    f'Cidade: {cid.title()}\n'
    f'Resposta: {analise}'
)


#cid = str('Em que cidade você nasceu').strip()
#print(cid[:5].title() == 'Santo')                      - Correção