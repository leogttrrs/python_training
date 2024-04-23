x=int(input('Escolha um valor para analisar: '))
valor_inicial = int(input('Valor inicial: '))
valor_final = int(input('Valor final: '))
lista = list(range(valor_inicial,valor_final, 1))
sim = x in lista
igual = x == valor_final
if sim:
    print(sim)
elif igual:
    print(igual)
else:
    print(sim)

