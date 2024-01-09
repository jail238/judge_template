#BOJ 15681

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(start):
    now = start
    visited[now] = True
    for nxt in graph[now]:
        if not visited[nxt]:
            dp[now] += dfs(nxt)
    return dp[now]

n, r, q = map(int, input().split())
p = [i for i in range(n+1)]
dp = [1 for _ in range(n+1)]
visited = [False for _ in range(n+1)]
graph = [[] for _ in range(n+1)]

for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

dfs(r)
for _ in range(q):
    s = int(input())
    print(dp[s])
