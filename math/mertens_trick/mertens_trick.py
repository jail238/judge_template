from math import isqrt
import sys
input = sys.stdin.readline

def phi_prefix(t): # t = ~sqrt(n)+500 precomputation
    phi = [i for i in range(t+1)]
    for p in range(2, t+1):
        if phi[p] == p:
            for k in range(p, t+1, p): phi[k] -= phi[k]//p
    prefix = [0 for _ in range(t+1)]
    s = 0
    for i in range(1, t+1):
        s += phi[i]
        prefix[i] = s
    return prefix

def mertens_trick(n, t, g1, pf, s_g, s_fg): # pf: O(1) (x <= t)
    def s_f(x):
        if x in cached: return cached[x]
        if x <= t: v = pf(x)
        else:
            sqrt_x = isqrt(x)
            ans, limit, s = s_fg(x), x//sqrt_x, 2
            
            while s <= limit: # harmonic_lemma
                e = x//(x//s)
                ans -= (s_g(e)-s_g(s-1))*s_f(x//s)
                s = e+1
            for i in range(1, sqrt_x): ans -= s_f(i)*(s_g(x//i)-s_g(x//(i+1)))
            v = ans//g1
        cached[x] = v
        return v
    return s_f(n)

def tmp_phi_sum(n): # f = phi, g = I, f*g = Id, S_{f*g}(x) = x(x+1)//2, s_g(x) = x, g(1) = 1
    t = isqrt(n)+500
    pf = phi_prefix(t)
    pf_phi, s_g, s_fg = lambda x: pf[x], lambda x: x, lambda x: x*(x+1)//2
    def cached_phi_sum(n): return mertens_trick(n, t, 1, pf_phi, s_g, s_fg)
    return cached_phi_sum

cached = {}
phi_sum = tmp_phi_sum(101010)
