folioes = int(input())
teste = 0
while folioes != 0:
    vencedor = None
    ordem = 0
    teste += 1
    participantes = [int(x) for x in (input().split())]
    for ingresso in participantes:
        ordem += 1
        if ingresso == ordem:
            vencedor = ingresso
            break
    print(f'Teste {teste}')
    print(vencedor)
    print()
    
    folioes = int(input())
