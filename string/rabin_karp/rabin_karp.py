from random import randint
import sys
input = sys.stdin.readline
prime = [2, 7, 61] # n < 2^32
# prime = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41] # n < 2^64

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
    for i in range(3): # 2^32
        if n == prime[i]: return True
        if not miller_rabin(n, prime[i]): return False
    return True
    
    # for i in range(13): # 2^64
    #     if n == prime[i]: return True
    #     if not miller_rabin(n, prime[i]): return False
    # return True

def hash(s, p_l, mod): #p_l = patterns_length
    c, tc, hash_val = 128, 1, 0
    for i in range(p_l):
        tc = c*tc%mod
        hash_val = hash_val*c+ord(s[i])%mod
    ret = [0 for _ in range(len(s)-p_l+1)]
    ret[0] = hash_val
    for i in range(p_l, len(s)):
        hash_val = (hash_val*c+ord(s[i])+(mod-tc)*ord(s[i-p_l]))%mod
        ret[i-p_l+1] = hash_val

    return ret

def hash2(s, p_l, sw): # sw is defined if you use pattern or not
    r1 = hash(s, p_l, m1)
    r2 = hash(s, p_l, m2)
    if sw == 1: return (r1[0] << 32) | r2[0]
    new_ret = [0 for _ in range(len(s)-p_l+1)]
    for i in range(len(s)-p_l+1):
        new_ret[i] = (r1[i] << 32) | r2[i]
    return new_ret

m1, m2 = -1, -1
while m1 == -1 or m2 == -1:
    n = randint(int(1e8), int(1e9))
    if prime_chk(n):
        if m1 == -1: m1 = n
        else: m2 = n

n = int(input())
lo, hi = 0, n
s = input().rstrip()
s2 = input().rstrip()
text = hash2(s, len(s2), 0)
pattern = hash2(s2, len(s2), 1)
cnt = 0
for i in text:
    if i == pattern: cnt += 1
print(cnt)
