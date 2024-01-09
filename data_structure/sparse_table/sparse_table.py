#BOJ 17435

from math import ceil, log2
import sys
input = sys.stdin.readline

def set_parent():
    for i in range(1, lg):
        for j in range(1, m+1):
            p[j][i] = p[p[j][i-1]][i-1]

m = int(input())
lg = ceil(log2(m))+1
p = [[0 for _ in range(lg)] for _ in range(m+1)]
f = list(map(int, input().split()))
for i in range(1, m+1):
    p[i][0] = f[i-1]
set_parent()

q = int(input())
for _ in range(q):
    n, x = map(int, input().split())
    for i in range(lg-1, -1, -1):
        if n >= 2**i:
            n = n-2**i
            x = p[x][i]
    print(x)
