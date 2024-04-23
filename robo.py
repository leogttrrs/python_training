linhas,colunas = [int(x) for x in input().split()]
linicial, cinicial = [int(x) for x in input().split()]
jafoi = set()
matriz = []
for i in range(linhas):
    linha = [int(x) for x in input().split()]
    matriz.append(linha)
xcursor = linicial - 1
ycursor = cinicial - 1
jafoi.add((xcursor,ycursor))

condicao = True
while condicao == True:
    condicao = False
    if ycursor > 0 and matriz[xcursor][ycursor - 1] == 1 and (xcursor,ycursor - 1) not in jafoi:
        ycursor -= 1
        jafoi.add((xcursor,ycursor))
        condicao = True
    elif ycursor < colunas -1 and matriz[xcursor][ycursor + 1] == 1 and (xcursor,ycursor + 1) not in jafoi:
        ycursor += 1
        jafoi.add((xcursor,ycursor))
        condicao = True
    elif xcursor < linhas -1 and matriz[xcursor + 1][ycursor] == 1 and  (xcursor +1,ycursor) not in jafoi:
        xcursor += 1
        jafoi.add((xcursor,ycursor))
        condicao = True
    elif xcursor > 0 and matriz[xcursor -1][ycursor] == 1 and (xcursor-1 , ycursor) not in jafoi:
        xcursor -= 1
        jafoi.add((xcursor,ycursor))
        condicao = True

print(f'{xcursor + 1} {ycursor + 1}')
