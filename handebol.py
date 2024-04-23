num_jogadores,num_partidas =[int(x) for x in input().split()]
goleadores = 0
for jogador in range(num_jogadores):
    gols = input().split()
    nao_marcou = False
    for gol in gols:
        if int(gol) == 0:
            nao_marcou = True
    if not nao_marcou:
        goleadores += 1

print(goleadores)
