# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira, e mostre quantos dólares ela pode comprar
# cotação do dollar em 26/01/2023 $5,07

dinheiro = float(input('Quanto de Dinheiro você tem em mãos? R$'))
dollar = float(dinheiro/5.07)

print(
    f'Você pode comprar US${dollar:.2f} em Dollares!'
)