lado1=abs(float(input('lado1: ')))
lado2=abs(float(input('lado2: ')))
lado3=abs(float(input('lado3: ')))

con1=lado1 < lado2+lado3
con2=lado2 < lado1+lado3
con3=lado3 < lado1+lado2

existe = con1 and con2 and con3



print(existe)

