from random import randint
import sys
input = sys.stdin.readline
prime = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41]

def miller_rabin(n, p):
    if n%p == 0: return n==p
    d = n-1
    while d%2==0: d >>= 1

    temp = pow(p, d, n)
    if temp == 1 or temp == n-1: return True

    while d*2 < n-1:
        d *= 2
        if pow(p, d, n) == n-1: return True
    return False

def prime_chk(n):
    if n < 2: return False
    for i in range(13):
        if n == prime[i]: return True
        if n%prime[i] == 0: return False
        if not miller_rabin(n, prime[i]): return False
    return True

def random_prime():
    X, Y = int(1e9), int(1e10)
    p1, p2 = -1, -1
    while p1 == -1 or p2 == -1:
        s = randint(X, Y)
        if prime_chk(s):
            if p1 == -1: p1 = s
            else:
                if p1 != s: p2 = s
    return p1, p2

def hash_init(s):
    n = len(s)
    h1, h2 = [0 for _ in range(n+1)], [0 for _ in range(n+1)]
    pow1, pow2 = [1 for _ in range(n+1)], [1 for _ in range(n+1)]
    for i, ch in enumerate(s, 1):
        ch = ord(ch)
        pow1[i] = (pow1[i-1]*base)%mod1
        pow2[i] = (pow2[i-1]*base)%mod2
        h1[i] = (h1[i-1]*base+ch)%mod1
        h2[i] = (h2[i-1]*base+ch)%mod2
    return h1, h2, pow1, pow2

def get_hash(h1, h2, pow1, pow2, l, r):
    x1 = (h1[r]-h1[l-1]*pow1[r-l+1])%mod1
    x2 = (h2[r]-h2[l-1]*pow2[r-l+1])%mod2
    return x1, x2

def f(s, k):
    check = set()
    for l in range(1, len(s)-k+2):
        r = l+k-1
        h = get_hash(l, r)
        if h in check: return 1
        check.add(h)
    return 0

mod1, mod2 = random_prime()
base = randint(256, int(1e6))
