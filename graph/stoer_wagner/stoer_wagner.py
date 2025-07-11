import sys
input = sys.stdin.readline
INF = float('inf')

def find(x):
    if p[x] == x: return x
    p[x] = find(p[x])
    return p[x]

def merge(a, b):
    a, b = find(a), find(b)
    if a != b:
        if sz[a] > sz[b]: a, b = b, a
        p[a] = b
        sz[b] += sz[a]

def contract():
    global n
    dist = [0 for _ in range(n+1)]
    visited = [0 for _ in range(n+1)]
    s, t, c = 0, 0, 0
    for _ in range(n):
        max_dist, k = -1, -1
        for i in range(1, n+1):
            if not is_merged[i] and not visited[i] and dist[i] > max_dist: k, max_dist = i, dist[i]
        if k == -1: break
        s, t = t, k
        c = max_dist
        visited[k] = 1
        for i in range(1, n+1):
            if not is_merged[i] and not visited[i]: dist[i] += adj[k][i]
    return s, t, c

def stoer_wagner():
    global n
    min_cut = INF
    for _ in range(n-1):
        s, t, c = contract()
        min_cut = min(min_cut, c)
        if min_cut == 0: return 0
        is_merged[t] = 1
        for i in range(1, n+1):
            if not is_merged[i]:
                adj[s][i] += adj[t][i]
                adj[i][s] += adj[t][i]
    return min_cut

n, m = map(int, input().split())
p = [i for i in range(n+1)]
sz = [1 for _ in range(n+1)]
adj = [[0 for _ in range(n+1)] for _ in range(n+1)]
is_merged = [0 for _ in range(n+1)]
for _ in range(m):
    a, b, w = map(int, input().split())
    merge(a, b)
    adj[a][b] = w
    adj[b][a] = w
print(stoer_wagner())
