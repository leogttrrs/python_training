primeiro=int(input('Insira o primeiro valor do intervalo: '))
segundo=int(input('Insira o segundo valor do intervalo: '))

diferenca=abs(primeiro-segundo)
if diferenca != 0:
    print(diferenca + 1)
else:
    print(1)
