conjunto = set()
while True:
    try:
        valor = input()
        conjunto.add(valor)
    except EOFError:
        break

print(len(conjunto))
