import math

total = int(input())
menor=math.inf
for i in range (total):
    valor = int(input())
    if valor < menor:
        menor = valor
print(menor)
