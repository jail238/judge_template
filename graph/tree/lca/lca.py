#BOJ 11438

from math import ceil, log2
from collections import deque
import sys
input = sys.stdin.readline

def bfs(start, depth):
    q = deque()
    q.append((start, depth))
    while q:
        now, depth = q.popleft()
        dep[now] = depth
        visited[now] = True
        for nxt in graph[now]:
            if not visited[nxt]:
                p[nxt][0] = now
                q.append((nxt, depth+1))

def set_parent(root):
    bfs(root, 0) # set_root
    for i in range(1, lg):
        for j in range(1, n+1):
            p[j][i] = p[p[j][i-1]][i-1]

def lca(a, b):
    if dep[a] > dep[b]: a, b = b, a
    for i in range(lg-1, -1, -1):
        if dep[b]-dep[a] >= 2**i:
            b = p[b][i]
    if a == b:
        return a
    
    for i in range(lg-1, -1, -1):
        if p[a][i] != p[b][i]:
            a, b = p[a][i], p[b][i]
    return p[a][0]

n = int(input())
lg = ceil(log2(n))+1
p = [[0 for _ in range(lg)] for _ in range(n+1)]
dep, visited = [0 for _ in range(n+1)], [False for _ in range(n+1)]
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

set_parent(1)
m = int(input())
for _ in range(m):
    a, b = map(int, input().split())
    print(lca(a, b))
