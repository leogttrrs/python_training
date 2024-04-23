nteste = int(input())
numero = nteste
num2=0
num3=0
num5=0
while numero % 2 == 0:
    numero = numero/2
    num2 += 1
while numero % 3 == 0:
    numero = numero/3
    num3 += 1
while numero % 5 == 0:
    numero = numero/5
    num5 += 1
dois = 2**num2
tres = 3**num3
cinco = 5**num5
if dois == nteste or dois*tres == nteste or dois*cinco == nteste or tres == nteste or tres*cinco == nteste or cinco == nteste or dois*tres*cinco == nteste:
    if nteste == 1:
        regular = False
    else:
        regular = True
else:
    regular = False
print(regular)
