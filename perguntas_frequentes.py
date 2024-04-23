perguntas,frequencia = [int(x) for x in input().split()]
while perguntas != 0 and frequencia != 0:
    frequente = 0
    numeros = input().split()
    for numero in numeros:
        if numeros.count(numero) >= frequencia:
            frequente = numero
    print(frequente)
    perguntas,frequencia = [int(x) for x in input().split()]
