
nota=float(input('Insira a nota a ser arredondada: '))
rounded=round(nota*2)/2
if nota - rounded == 0.25:
    rounded += 0.5
print(rounded)
