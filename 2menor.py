import math

tamanho = int(input())
menor = math.inf
menor2 = math.inf

for i in range(tamanho):
    valor = int(input())
    if valor < menor:
        menor2 = menor
        menor = valor
    elif valor < menor2 and valor >= menor:
        menor2 = valor
    
print(menor2)

