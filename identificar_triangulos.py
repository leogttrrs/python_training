l1=int(input('Insira o primeiro lado do triângulo: '))
l2=int(input('Insira o segundo lado do triângulo: '))
l3=int(input('Insira o terceiro lado do triângulo: '))
naoforma = l1 >= l2 + l3 or l2 >= l1+l3 or l3 >= l1 + l2
while naoforma:
    print('Os lados escolhidos não formam triangulo, por favor, escolha os 3 lados novamente.')
    l1=int(input('Insira o primeiro lado do triângulo: '))
    l2=int(input('Insira o segundo lado do triângulo: '))
    l3=int(input('Insira o terceiro lado do triângulo: '))
    naoforma = l1 >= l2 + l3 or l2 >= l1+l3 or l3 >= l1 + l2

if l1 == l2:
    if l1 == l3:
        print('equilátero')
    else:
        print('isóceles')
elif l1 == l3:
    if l1 == l2:
        print('equilátero')
    else:
        print('isóceles')
elif l2 == l3:
    if l1 == l2:
        print('equilátero')
    else:
        print('isóceles')
else:
    print('escaleno')
