from math import gcd
from random import *
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

def pollard_rho(n):
    if prime_chk(n): return n
    if n == 1: return 1
    a = b = randint(2, n)
    c, d = randint(1, n), 1
    
    while True:
        a = ((a*a)%n+c%n)%n
        for _ in range(2): b = ((b*b)%n+c%n)%n
        d = gcd(abs(a-b), n)
        if d == n: return pollard_rho(n)
        if d != 1: break
    
    if prime_chk(d): return d
    else: return pollard_rho(d)

def prime_factorization(n):
    ans = {}
    while n%2==0:
        if not 2 in ans: ans[2] = 1
        else: ans[2] += 1
        n >>= 1
    
    while n > 1:
        div = pollard_rho(n)
        if not div in ans: ans[div] = 1
        else: ans[div] += 1
        n //= div
    return ans
