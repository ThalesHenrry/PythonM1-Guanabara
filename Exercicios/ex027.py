#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o ultimo nome separadamente.

nome = input("Digite seu nome completo: ")
div = nome.split()

print(
    f' Nome completo: {nome.title()}\n'
    f'1º Nome: {div[0].title()}\n'
    f'Ultimo Nome: {div[-1].title()}'
)



#---------------------------------------------------------------------------

#nome = input('Digite seu nome completo: ')
#div = nome.split()

#def lastWord(nome):
                                                                # Feito com Inf. da Internet
#    lis = list(nome.split(" "))

#    length = len(lis)

#    return lis[length - 1]

#print(
 #   f'Primeiro nome: {div[0]}\n'
 #   f'Ultimo nome: {lastWord(nome)}'
#)