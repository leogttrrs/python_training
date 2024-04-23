testes = int(input())
arvore = input()
for teste in range(testes):
    num_arvores = 0
    arvores = {} # 
    try:
        arvore = input()
        while arvore != '':
            num_arvores += 1
            if arvore not in arvores:
                arvores[arvore] = 1
            else:
                arvores[arvore] += 1
            arvore = input()
                
    except EOFError:
        pass
    setarvores = sorted(set(arvores))
    for i in setarvores:   
        print (f'{i} {((arvores[i]/num_arvores)*100):.4f}')
