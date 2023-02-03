#Desenvolva um programa que pergunte a distância de uma viagem em km. Calcule o preço da passagem, cobrando R$0,50 por km para viagem de até 200km e R$0,45 para viagens mais longas.

km_viagem = float(input('Distância de viagem por Km: '))

if km_viagem <= 200:
    print(
        f'Distâcia da viagem: {km_viagem} Km/h\n'
        f'Valor R${km_viagem*0.50:.2f}'
    )
else:
    print(
        f'Distância da viagem: {km_viagem} Km/h\n'
        f'Valor R${km_viagem*0.45:.2f}'
    )