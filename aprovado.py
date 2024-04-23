p1=float(input('Insira a nota da p1: '))
p2=float(input('Insira a nota da p2: '))
p3=float(input('Insira a nota da p3: '))
peso1=float(input('Insira o peso da p1: '))
peso2=float(input('Insira o peso da p2: '))
peso3=float(input('Insira o peso da p3: '))

nota= ((p1*peso1) + (p2*peso2) + (p3*peso3)) / (peso1 + peso2 + peso3)

media = 6

resultado = nota>=media
print(resultado)
