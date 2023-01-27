# Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado, e a quantidade de dias pelos quais
# ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

km = float(input('Quantidade de KM percorrido: '))
dias = int(input('Dias com o veiculo: '))
pg_km = km*0.15
pg_dias = dias*60

print(
    f'Valor do aluguel do veiculo R${pg_km+pg_dias:.2f}'
)
