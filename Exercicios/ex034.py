#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
#Para salário superior a R$1250,00 calcule um aumento de 10%
#Para os inferiores, um aumento de 15%

salario = float(input('Qual o seu salario atual? R$'))

if salario > 1250:
    print(
        f'Salário atual: R${salario:.2f}\n'
        f'Com aumento: R${(salario * 10)/100 + salario:.2f}'
    )
else:
    print(
        f'Salário atual: R${salario:.2f}\n'
        f'Com aumento: R${(salario * 15)/100 + salario:.2f}'
    )