qtdcarros, voltas = [int(x) for x in input().split()]
carros = {}
for i in range(qtdcarros):
    soma = 0
    tempos = [int(z) for z in input().split()]
    for tempo in tempos:
        soma += tempo
    carros[i+1] = soma

carros = dict(sorted(carros.items(), key = lambda x: x[1]))
indice = 0
for carro in carros.keys():
    print (carro)
