# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros
# (Aumento de desafio na Correção)

metros = int(input("Digite um valor em metros: "))

km = (metros * 0.001)
hm = (metros * 0.01)
dam = (metros * 0.1)
dm = (metros * 10)
cm = (metros * 100)
mm = (metros * 1000)

print(
    f'Metros {metros}m.\n'
    f'Convertido em Centímetros {cm}cm;\n'
    f'Convertido em Milímetros {mm}mm;\n'
    f'Convertido em Decimetros {dm}dm;\n'
    f'Convertido em Decametros {dam:.1f}dam;\n'
    f'Convertido em Hectometros {hm}hm;\n'
    f'Convertido em kilometros {km}km.\n'
)
