
qtd = int(input())
produto = 1
raiz = 0
for i in range(qtd):
    raiz += 1
    numero = float(input())
    produto *= numero
saida = produto**(1/raiz)
print(saida)
