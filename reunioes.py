data1=int(input())
data2=int(input())
data3=int(input())
todosiguais = data1 == data2 and data1 == data3
umigual = (data1 == data2 and data1 != data3) or (data1 != data2 and data1 == data3) or (data1 != data2 and data2 == data3)
if todosiguais:
    numero = 1
elif umigual:
    numero = 2
else:
    numero = 3
print(numero)
