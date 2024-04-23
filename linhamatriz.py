linha_chave = int(input())
operacao = input()

matriz = []
for linha in range(12):
    numeros_linha = []
    for numero in range(12):
        numeros_linha.append(float(input()))
    matriz.append(numeros_linha)
        
resultado = sum(matriz[linha_chave])

if operacao == 'm' or operacao == 'M':
    resultado /= 12
    
print(f'{resultado:.1f}')
