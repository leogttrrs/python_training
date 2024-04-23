import math

a=float(input('Digite o valor de A '))
b=float(input('Digite o valor de B '))
c=float(input('Digite o valor de C '))

calculosoma= ((-b) + (math.sqrt((b**2)-(4*a*c))))/(2*a)

calculosub= ((-b) - (math.sqrt((b**2)-(4*a*c))))/(2*a)

print('x1 = '+ str(calculosoma))
print('x2 = '+ str(calculosub))