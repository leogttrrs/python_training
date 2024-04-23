#Pintura
area=int(input())
litros = area/18
galoes = round(litros/ 3.6)
if galoes ==0:
    galoes=1
    
valor = (galoes*25)


print(area)
print(galoes)
print(valor)

