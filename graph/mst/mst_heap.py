from heapq import *
import sys
input = sys.stdin.readline

def find(p, x):
    while p[x] != x:
        x = p[x]
    return x

def union(p, a, b):
    a, b = find(p, a), find(p, b)
    if a != b:
        p[max(a, b)] = min(a, b)
        return True
    return False

n, m = map(int, input().split())
p = [i for i in range(n+1)]
heap = []
ans, lines = 0, 0
for _ in range(m):
    a, b, c = map(int, input().split())
    heappush(heap, (c, a, b))

while heap and lines < n-1:
    cost, a, b = heappop(heap)
    pos = union(p, a, b)
    if pos:
        ans += cost; lines += 1

if lines == n-1: print(ans)
else: print(-1)
