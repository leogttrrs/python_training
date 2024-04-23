cartas = input().split()
crescente = 'C'
for carta in range(len(cartas)-1):
    if cartas[carta] > cartas[carta+1]:
        crescente = 'D'
print(crescente)
