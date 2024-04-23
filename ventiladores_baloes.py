num_linhas, num_colunas, posicao = [int(x) for x in input().split()]
while num_linhas != 0 and num_colunas != 0 and posicao != 0:
    posicao -= 1
    estourou = False
    linha_boom = 0
    for _ in range(num_linhas):
        compartimentos = [int(x) for x in input().split()]
        if not estourou:
            linha_boom += 1
            i = posicao
            j = posicao
            while compartimentos[i] == 0:
                i -= 1
            while compartimentos[j] == 0:
                j += 1
            posicao += compartimentos[i] - compartimentos[j]
            if posicao <= i:
                print(f'BOOM {linha_boom} {i + 1}')
                estourou = True
            if posicao >= j:
                print(f'BOOM {linha_boom} {j + 1}')
                estourou = True
    if not estourou:
        print(f'OUT {posicao + 1}')
    num_linhas, num_colunas, posicao = [int(x) for x in input().split()]    
