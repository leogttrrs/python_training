valor = 0.1*(float(input()))
genero = input()
idade = int(input())
if genero == 'M':
    if idade > 33:
        valor *= 0.8
    elif idade >= 25:
        valor *= 0.9
else:
    if idade > 33:
        valor *= 0.65
    elif idade >= 25:
        valor *= 0.8
    else:
        valor *= 0.95
print(valor)
