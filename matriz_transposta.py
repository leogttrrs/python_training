# Lendo uma matriz 
# A primeira linha tem dois valores inteiros n e m correspondentes as dimensões da matriz
# Em seguinda vem n linhas, cada uma delas com os m valores que definem cada linha

n, m = [int(x) for x in input().split()]
matriz = []
for _ in range(n):
    matriz.append([int(x) for x in input().split()])


#Obter a matriz transposta

matriz = [ [10, 20, 30], [5, 6, 7] ]

num_linhas = len(matriz)
num_colunas = len(matriz[0])

transposta = [ [0] * num_linhas for _ in range(num_colunas) ]
for i in range(num_linhas):
    for j in range(num_colunas):
        transposta[j][i] = matriz[i][j]

print(transposta)
