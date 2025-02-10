from math import ceil, sqrt
import sys
input = sys.stdin.readline

def baby_step_giant_step(a, n, p):
    m = ceil(sqrt(p-1))
    s = {}
    for i in range(m):
        s[pow(a, i, p)] = i # {a^i (mod p): i}를 저장
    tmp = pow(pow(a, p-2, p), m, p) # pow(a, -m, p)와 같음
    for i in range(m):
        x = (n%p*pow(tmp, i, p))%p
        if x in s: return m*i+s[x]
    return -1 # 해가 없는 경우
