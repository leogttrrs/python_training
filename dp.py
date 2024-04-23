import math
num_valores = int(input())
valores = []
for i in range(num_valores):
    valor = float(input())
    valores.append(valor)
media = sum(valores)/num_valores
soma = 0
for valor in valores:
    soma += (valor-media)**2
dp = math.sqrt(soma/(num_valores-1))
print(dp)
