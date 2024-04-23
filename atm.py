plug1 = input().split()
plug2 = input().split()
compativel = True
for i in range(5):
    if plug1[i] == plug2[i]:
        compativel = False
        break

if compativel:
    print('Y')
else:
    print('N')
