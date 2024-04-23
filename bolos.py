farinha, ovos, leite = [int(x) for x in input().split()]
qtdfarinha = farinha/2
qtdovo = ovos/3
qtdleite = leite/5
bolos = min(qtdfarinha, qtdovo, qtdleite)
print(int(bolos))
