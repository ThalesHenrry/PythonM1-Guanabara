# Escreva um programa que converta uma temperatura digitando em graus celsius e converta para Fahrenheit.

cel = float(input('Informe a temperatura em ºC: '))
fh = float(cel*1.8+32)

print(
    f'A temperatura de {cel}ºC corresponde a {fh}ºF!'
)