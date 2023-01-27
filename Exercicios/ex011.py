# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta
# necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m².

altura = float(input('Qual a altura da parede? '))
largura = float(input('Qual a largura da parede? '))
area = float(altura*largura)
litro_area = (area/2)

print(
    f'Á área da parede é de {area}m².\n'
    f'-Quantidade de tinta necessária para pintar é: {litro_area}l'
)