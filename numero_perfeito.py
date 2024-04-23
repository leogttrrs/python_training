tentativas = int(input())
def soma_divisores(x):
    hipotese = 1
    soma=0
    while hipotese <= x/2:
        if x % hipotese == 0:
            soma += hipotese
        hipotese += 1
    return soma
for i in range(tentativas):
    numero = int(input())
    if (soma_divisores(numero)) == numero:
        print(numero,'eh perfeito')
    else:
        print(numero,'nao eh perfeito')



