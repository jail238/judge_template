from math import isqrt
import sys
input = sys.stdin.readline

def prime(n): # O(N^(1/2)/2)
    if n % 2 == 0:
        if n == 2: return True
        else: return False
    for i in range(3, isqrt(n)+1, 2):
        if n%i == 0:
            return False
    return True
