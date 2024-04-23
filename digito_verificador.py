numero = input()
soma = 0
x = 0
y = 2
while y <= len(numero):
    soma += int(numero[x:y])
    x+=2
    y+=2
calculo = (soma//11) * 11
resto = soma - calculo
digito = 11 - resto
correto = str(digito) == numero[-1]
print(correto)
#concluir

