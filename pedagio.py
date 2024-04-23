comprimento,dpp = [int(x) for x in input().split()]
cpk, valorpedagio = [int(x) for x in input().split()]
preco_total = int((((comprimento//dpp) * valorpedagio) + (cpk * comprimento)))
print(preco_total)
