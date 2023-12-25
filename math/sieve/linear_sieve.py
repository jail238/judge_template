from math import isqrt
import sys
input = sys.stdin.readline

def linear_sieve(n):
    for i in range(2, n+1):
        if prime[i] == 1:
            sieve.append(i)
            prime[i] = i
        for j in sieve:
            if i*j > n: break
            prime[i*j] = j
            if i%j == 0: break

def divide(n):
    p = []
    while n != 1:
        p.append(prime[n])
        n //= prime[n]
    return p

n = int(1e9) # input your problem n size
prime, sieve = [1 for _ in range(n+2)], []
linear_sieve(n)
q = int(input())
l = list(map(int, input().split()))
for i in range(q):
    print(*divide(l[i]))
