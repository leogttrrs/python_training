n=int(input('n :'))
m=int(input('m :'))
maior1 = n > 1 and m > 1
contador = 1
while not maior1:
    n=int(input('n: '))
    m=int(input('m: '))
    maior1 = n >1 and m >1


def multiplos(valor):
    return valor * contador
    
    
    
while (contador*n) <= m:
    print(multiplos(n))
    contador += 1
