while True:
    x = int(input())
    if x == 0:
        break
    else:
        resultado = ''
        for i in range (1,x+1):
            resultado += str(i) + ' '
            if i == x+1:
                resultado -= ' '
        print(resultado)
        