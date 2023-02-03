# Faça um algoritmo que leia o sálario de um funcionário e mostre seu novo salário, com 15% de aumento.

salario = float(input('Salário atual R$'))
aumento = float(salario*15/100)

print(
    f'O sálario atual é de R${salario:.2f},\n'
    f'com o aumento de 15% ficará R${salario+aumento:.2f}'
)
