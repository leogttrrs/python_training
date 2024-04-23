partidas = int(input())
while partidas != 0:
    contador = 0
    john = 0
    jogadas = input().replace(' ','')
    while contador < len(jogadas):
        john += int(jogadas[contador])
        contador += 1
    mary = partidas - john
    print(f'Mary won {mary} times and John won {john} times')
    partidas = int(input())
