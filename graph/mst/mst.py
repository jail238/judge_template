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

n, m = map(int, input().split())
p = [i for i in range(n+1)]
edges = []
for _ in range(m):
    a, b, c = map(int, input().split())
    edges.append((c, a, b))
edges.sort()
ans, lines = 0, 0
for edge in edges:
    cost, a, b = edge
    if find(p, a) != find(p, b):
        union(p, a, b)
        ans += cost
    if lines == n-1:
        break
print(ans)
