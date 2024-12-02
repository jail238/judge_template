import sys
input = sys.stdin.readline
MAX = 210

def dfs(now):
    visited[now] = True
    for nxt in graph[now]:
        if b[nxt] == -1 or (not visited[b[nxt]] and dfs(b[nxt])):
            a[now] = nxt
            b[nxt] = now
            return True
    return False

n, m = map(int, input().split())
graph = [[] for _ in range(MAX)]
for i in range(1, n+1):
    a, *b = map(int, input().split())
    for j in b:
        graph[i].append(j)
matching = 0
a, b = [-1 for _ in range(MAX)], [-1 for _ in range(MAX)]
visited = [False for _ in range(MAX)]

for i in range(1, n+1):
    if dfs(i):
        visited = [False for _ in range(MAX)]
        matching += 1
print(matching)
