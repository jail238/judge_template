import sys
input = sys.stdin.readline

def miller_rabin(n, p):
    if n%p == 0: return True
    d = n-1
    while d%2==0: d >>= 1
    
    temp = pow(p, d, n)
    if temp == 1 or temp == n-1: return True
    
    while d*2 < n-1:
        d *= 2
        if pow(p, d, n) == n-1: return True
    return False

def prime_chk(n):
    # for i in range(3): # 2^32
    #     if n == prime[i]: return True
    #     if not miller_rabin(n, prime[i]): return False
    # return True
    
    for i in range(13): # 2^64
        if n == prime[i]: return True
        if not miller_rabin(n, prime[i]): return False
    return True

# prime = [2, 7, 61] # n < 2^32
prime = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41] # n < 2^64

n = int(input())
print(prime_chk(n))
