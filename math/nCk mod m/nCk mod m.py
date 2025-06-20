from math import gcd, lcm
import sys
input = sys.stdin.readline

def nCk_mod_m(N, K, M):
    if M == 1: return 0
    if K < 0 or K > N: return 0
    if K == 0 or K == N: return 1%M
    if K > N//2: K = N-K

    def prime_fac(n):
        div, i, k = {}, 3, n
        while k%2 == 0:
            if 2 not in div: div[2] = 1
            else: div[2] += 1
            k //= 2
        while i * i <= k:
            while k % i == 0:
                if i not in div: div[i] = 1
                else: div[i] += 1
                k //= i
            i += 2
        if k != 1:
            if k not in div: div[k] = 1
            else: div[k] += 1
        return div

    def crt(a, p):
        if not a: return 0
        a0, m0 = a[0], p[0]
        for i in range(1, len(p)):
            ai, mi = a[i], p[i]
            g = gcd(m0, mi)
            if (a0-ai) % g != 0: return -1
            k = ((ai-a0)//g)*pow(m0//g, -1, mi//g)%(mi//g)
            m_tmp = lcm(m0, mi)
            a0, m0 = (a0+k*m0)%m_tmp, m_tmp
        return a0

    def cntm(n, m):
        tmp = 0
        while n > 0:
            tmp += n//m
            n //= m
        return tmp
    
    pi, mod, fstarp = None, None, None

    def f_star_p(n, mm):
        nonlocal mod
        fstarlist = [1 for _ in range(n+1)]
        res = 1
        for i in range(1, n+1):
            if i % mm != 0: res = (res*i)%mod
            fstarlist[i] = res
        return fstarlist

    def f_p(p):
        nonlocal pi, mod, fstarp
        if p == 0: return 1
        return (pow(fstarp[mod], p//mod, mod)*(f_p(p//pi)%mod)*(fstarp[p%mod]))%mod

    mdiv = prime_fac(M)
    a_i, p_i = [], []
    for pii, eii in mdiv.items():
        cnt = cntm(N, pii)-cntm(K, pii)-cntm(N-K, pii)
        pi, mod = pii, pii**eii
        
        if cnt >= eii:
            a_i.append(0)
            p_i.append(mod)
        else:
            fstarp = f_star_p(mod, pi)
            x1n, x1k, x1nk = f_p(N), f_p(K), f_p(N-K)
            x = (x1n * pow(x1k, -1, mod)*pow(x1nk, -1, mod)*pow(pi, cnt, mod))%mod
            a_i.append(x)
            p_i.append(mod)

    return crt(a_i, p_i)

N, K, M = map(int, input().split())
print(nCk_mod_m(N, K, M))
