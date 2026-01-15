from math import isqrt
import sys
input = sys.stdin.readline

def continued_fraction(D):
    period = [isqrt(D)]
    m, d, a = 0, 1, period[0]
    while a != 2*period[0]:
        m = d*a-m
        d = (D-m*m)//d
        a = (period[0]+m)//d
        period.append(a)
    return period

def pell_equation(D):
    sqrtD = isqrt(D)
    if sqrtD**2 == D: return 1, 0
    cf = continued_fraction(D)
    a0, l = cf[0], len(cf)-1
    if l&1: period = 2*l-1 # 주기 홀수면 -1 다음에 1
    else: period = l-1
    pm2, pm1 = 0, 1
    qm2, qm1 = 1, 0
    for i in range(period+1):
        if i == 0: a = cf[0]
        else: a = cf[(i-1)%l+1]
        p, q = a*pm1+pm2, a*qm1+qm2
        pm2, pm1 = pm1, p
        qm2, qm1 = qm1, q
    return p, q
