import math
num_sorteios = int(input())
for sorteio in range(num_sorteios):
    num_alunos, num_secreto = [int(x) for x in input().split()]
    palpites = [int(x) for x in input().split()]
    dif_maisproximo = math.inf
    for aluno in range(len(palpites)):
        if abs(palpites[aluno] - num_secreto) < abs(dif_maisproximo):
            dif_maisproximo = abs(palpites[aluno]  - num_secreto)
            vencedor = aluno + 1
    print(vencedor)
