# O(NloglogN / 2)
from math import isqrt
import sys
input = sys.stdin.readline

n = int(input())
sieve = [1 for _ in range(n+1)]
sieve[0] = sieve[1] = 0
for i in range(4, n+1, 2): sieve[i] = 0
for i in range(3, isqrt(n)+1, 2):
    if sieve[i]:
        j = 2
        while i*j <= n:
            sieve[i*j] = 0
            j += 1
