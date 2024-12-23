#BOJ 13970
from math import log
import sys
input = sys.stdin.readline

def div2(x):
        ret = x
        while ~x & 1:
            x >>= 1
        if ret != x:
            ret >>= 1
        return ret, x

def phi(x):
    ans, x = div2(x)
    p = 3
    while p*p <= x:
        if x%p == 0:
            ans -= ans//p
            while x % p == 0:
                x //= p
        p += 2
    if x > 1: return ans-(ans//x)
    return ans

t, MOD = map(int, input().split())
euler_mod = [MOD]
while euler_mod[-1] != 1: euler_mod.append(phi(euler_mod[-1]))
for _ in range(t):
    a, *l = map(int, input().split())
    ll = [0]
    for i in l:
        ll.append(i)
        if i == 1: break
    f, r, ans = 0, 1, 1
    for i in range(min(len(ll), len(euler_mod))-1, 0, -1):
        ff = True
        if not f:
            if log(ll[i])*r > log(2*MOD): f = 1
        if not f:
            r = pow(ll[i], r)
            if r < 2*euler_mod[i-1]:
                ans = r
                ff = False
        if ff: ans = pow(ll[i], ans, euler_mod[i-1])+euler_mod[i-1]
    print(ans%MOD)
