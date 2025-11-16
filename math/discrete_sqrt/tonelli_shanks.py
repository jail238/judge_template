from random import *
import sys
input = sys.stdin.readline

def tonelli_shanks(n, p):
    n %= p
    if n == 0: return 0, 0
    if pow(n, (p-1)//2, p) != 1: return -1, -1
    if p%4 == 3:
        x = pow(n, (p+1)//4, p)
        return x, (p-x)%p
    
    s, q = 0, p-1
    while q%2 == 0:
        q >>= 1
        s += 1
    
    z = randint(2, p-1)
    while pow(z, (p-1)//2, p) != p-1: z = randint(2, p-1)
    c, x, t, m = pow(z, q, p), pow(n, (q+1)//2, p), pow(n, q, p), s
    while t != 1:
        i = 1
        tmp = pow(t, 2, p)
        while tmp != 1:
            tmp = pow(tmp, 2, p)
            i += 1
        b = pow(c, 1<<(m-i-1), p)
        x, t, c, m = (x*b)%p, (t*b*b)%p, (b*b)%p, i
    return x, (p-x)%p
