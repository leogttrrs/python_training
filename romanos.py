def romano_para_decimal(num_romano):
    romanos = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    resultado = 0
    for i in range(len(num_romano)):
        if i > 0 and romanos[num_romano[i]] > romanos[num_romano[i-1]]:
            resultado += romanos[num_romano[i]] - 2 * romanos[num_romano[i-1]]
        else:
            resultado += romanos[num_romano[i]]
    return resultado

num_romano = input()
print(romano_para_decimal(num_romano))

