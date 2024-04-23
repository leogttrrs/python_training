import math

n = float(input())
sinal = '+'

if n < 0:
    sinal = '-'
    n = abs(n)
if n >= 1:
    exp = int(math.log(n, 10))
    sinal_exp = '+'
else:
    exp = int(math.log(n, 10)) - 1
    sinal_exp = '-'

n /= 10**exp

print(f'{sinal}{n:.4f}E{sinal_exp}{abs(exp):02}')
