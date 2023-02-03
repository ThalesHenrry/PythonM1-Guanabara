# Faça um algoritimo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

valor = float(input('Digite o valor do produto R$'))
desconto = float(valor*5/100)

print(
    f'O valor do produto de R${valor:.2f}, com desconto de 5% é R${valor-desconto:.2f}'
)