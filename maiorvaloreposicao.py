import math
maiorvalor = -math.inf
posicao = 0
qtd = int(input())
for i in range(qtd):
    valor = int(input())
    posicao += 1
    if valor > maiorvalor:
        maiorvalor = valor
        pfinal = posicao
print (maiorvalor, pfinal)

