from math import isqrt
import sys
input = sys.stdin.readline

def prime(n):
    for i in range(2, isqrt(n)+1):
        if n%i == 0:
            return False
    return True
