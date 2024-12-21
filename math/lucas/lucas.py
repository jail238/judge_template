from math import comb
import sys
input = sys.stdin.readline

def lucas(n, k, m):
    ans = 1
    listn, listk = [], []
    while n != 0 and k != 0:
        ni, ki = n%m, k%m
        listn.append(ni)
        listk.append(ki)
        n //= m
        k //= m
        if ni < ki:
            ans = 0
            break
    if ans != 0:
        for i in range(len(listn)):
            ans *= comb(listn[i], listk[i])
            ans %= m
    return ans
