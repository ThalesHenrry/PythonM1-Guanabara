from datetime import date
from time import sleep
from random import choice
print(
    '=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=\n'
    ' \033[1;44m          Ficha de Cadastro         \033[m \n'
    '=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=\n'
)

nasc = int(input('Ano de Nascimento: '))
idade = date.today().year - nasc

if idade < 18:
    print('\033[1;41mNão tem idade suficiente para cadastro!\033[m'.upper())
else:
    nome = str(input('Nome completo: ').title())
    cpf = str(input('Número de cpf: '))
    tel = str(input('Número de telefone: '))
    nome_mae = str(input('Nome da Mãe: '))
    nome_pai = str(input('Nome do Pai: '))
    filhos = bool(input('Tem filhos?'))
    escolha = ['Basquete', 'Volei', 'Futebol', 'Karate', 'Corrida']

    print(
        f'\033[1mNome:{nome:2}     Idade:{idade}\n'
        f'\033[1mCPF:{cpf:2}       Telefone:{tel}\n'
        
        f'-------------------------------------------\n'
        
        f'\033[1mPai:{nome_pai}\n'
        f'\033[1mMãe:{nome_mae}\n'
        
        f'\033[1mFilhos: {filhos}\n'
    )

    print('\033[1;97;45mSORTEIO DE ESPORTES DA CIDADE\033[m\n')
    print('\033[41mCarregando...\033[m\n')
    sleep(10)
    print(f'\033[1;4;97mVOCÊ FOI ESCALADO PARA A MODALIDADE: {choice(escolha).upper()}!')