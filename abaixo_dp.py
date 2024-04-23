operacao = input()
matriz = []
for i in range(12):
    linha = [float(input()) for j in range(12)]
    matriz.append(linha)
soma = 0
for i in range(1, 12):
    soma += sum(matriz[i][0:i])
if operacao.lower() == 's':
    print(soma)
else:
    print(f'{soma/66:.1f}')