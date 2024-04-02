import sys
input = sys.stdin.readline

def find(p, x):
    while p[x] != x:
        x = p[x]
    return x

def union(p, a, b):
    a, b = find(p, a), find(p, b)
    p[max(a, b)] = min(a, b)
