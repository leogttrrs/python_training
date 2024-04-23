atacantes, zagueiros = [int(x) for x in input().split()]
while atacantes != 0 and zagueiros != 0:
    linhaataque = 0
    linhadefesa = 0
    disataque = [int(w) for w in input().split()]
    disdefesa = [int(z) for z in input().split()]
    ultimodef = min(disdefesa)
    disdefesa.remove(ultimodef)
    if min(disataque) < min(disdefesa):
        print('Y')
    else:
        print('N')
    atacantes, zagueiros = [int(x) for x in input().split()]
