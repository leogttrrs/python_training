operacao = input()
matriz = []
for linha in range(12):
    coluna = []
    for numero in range(12):
        coluna.append(float(input()))
    matriz.append(coluna)
soma = 0
indice = 12
for i in range(5):
    indice -= 1
    soma += sum(matriz[i][i+1:indice])

if operacao == 'S':
    print(f'{soma:.1f}')
else:
    print(f'{(soma/30):.1f}')
