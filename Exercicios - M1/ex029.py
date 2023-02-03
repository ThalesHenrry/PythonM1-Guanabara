#Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar a velocidade de 80k/h, mostre uma mensagem dizendo que ele foi multado.
#A multa vai custar R$7,00 por cada km acima do limite.

velocidade = float(input('Qual a velocidade que o veiculo percorreu? '))
velocidade_a_mais = velocidade - 80
valor_multa = velocidade_a_mais * 7

if velocidade > 80:
    print(
        f'VOCÊ FOI MULTADO!\n'
        f'Ultrapassando {velocidade_a_mais}Km/h a mais do que o permitido.\n'
        f'O valor da multa a ser paga é R${valor_multa:.2f}'
    )
else:
    print('Dentro da velocidade permitida de 80km/h')