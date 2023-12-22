# BOJ 11266
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
INF = int(1e6)

def dfs(now, isRoot):
    global cnt
    cnt += 1
    visited_n[now], child_cnt = cnt, 0
    visited[now] = True
    temp_n = visited_n[now]
    for nxt in graph[now]:
        if visited[nxt]:
            temp_n = min(temp_n, visited_n[nxt])
            continue
        visited[nxt] = True
        child_cnt += 1
        pre_n = dfs(nxt, False)
        if not isRoot and pre_n >= visited_n[now]: ans.add(now)
        temp_n = min(temp_n, pre_n)
    if isRoot and child_cnt >= 2:
        ans.add(now)
    return temp_n

v, e = map(int, input().split())
graph = [[] for _ in range(v+1)]
visited = [False for _ in range(v+1)]
visited_n = [INF for _ in range(v+1)]
ans = set()
for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

cnt = 0
for i in range(1, v+1):
    if not visited[i]: dfs(i, True)
print(len(ans))
print(*sorted(ans))
