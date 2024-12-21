from math import gcd, lcm
import sys
input = sys.stdin.readline

def crt(a, p): # x = a_i (mod p_i), it can solve if gcd(p_i, p_j) != 1
    a0, m0 = a[0], p[0]
    for i in range(1, len(p)):
        ai, mi = a[i], p[i]
        g = gcd(m0, mi)
        if (a0-ai)%g != 0: return -1 # no solution
        k = ((ai-a0)//g)*pow(m0//g, -1, mi//g)%(mi//g)
        m_tmp = lcm(m0, mi)
        a0, m0 = (a0+k*m0)%m_tmp, m_tmp
    return a0

a = list(map(int, input().split()))
p = list(map(int, input().split()))
print(crt(a, p))
