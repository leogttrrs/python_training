dias = int(input('Dias: '))
diaria=45*dias
kms= float(input("Km's: "))
kmdiaria = 60*dias
if (kms / kmdiaria) > 1:
    precokm = ((kms - (kmdiaria)) * 0.5)
else:
    precokm = 0

preco = diaria + precokm
print(preco)
