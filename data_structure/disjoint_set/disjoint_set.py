import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

def find(p, x):
    if p[x] != x:
        p[x] = find(p, p[x])
    return p[x]

def union(p, a, b):
    a, b = find(p, a), find(p, b)
    p[max(a, b)] = min(a, b)
