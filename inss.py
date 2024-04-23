salario = float(input())
if salario <= 720:
    inss = (7.65/100)*salario
elif salario <= 1200:
    inss = (9/100) * salario
elif salario <= 2400:
    inss = (11/100) * salario
else:
    inss = (11/100)*2400
print(f'{inss:.2f}')
