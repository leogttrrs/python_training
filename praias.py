tentativas = int(input())
maiordistancia = 0
somadistancias = 0
praias15e20 = 0
for i in range (tentativas):  
    praia, distancia = input().split(';')
    distancia = int(distancia)
    somadistancias += distancia
    if distancia > maiordistancia:
        maisdistante = praia
        maiordistancia = distancia
    if distancia >= 15 and distancia <=20:
        praias15e20 += 1
print(f'{maisdistante};{praias15e20};{(somadistancias/tentativas):.1f}')

