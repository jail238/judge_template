from math import isqrt
import sys
input = sys.stdin.readline

def linear_sieve(n):
    for i in range(2, n+1):
        if prime[i] == 1: sieve.append(i)
        for j in sieve:
            if i*j > n: break
            sieve[i*j] = j
            if i%j == 0: break

n = int(input())
prime, sieve = [0, 0] + [1 for _ in range(n)], []
