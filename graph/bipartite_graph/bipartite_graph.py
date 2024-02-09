import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(now, cor):
    color[now] = cor
    for nxt in graph[now]:
        if color[nxt] == 'W':
            if cor == 'X': dfs(nxt, 'Y')
            else: dfs(nxt, 'X')
        else:
            if color[now] == color[nxt]:
                isBigraph = False
                return
    return


v, e = map(int, input().split())
color = ['W' for _ in range(v+1)]
graph = [[] for _ in range(v+1)]
isBigraph = True
for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
for i in range(1, v+1):
    if color[i] == 'W': dfs(i, 'X')
    else:
        for nxt in graph[i]:
            if color[i] == color[nxt]:
                isBigraph = False
                break
    if not isBigraph: break
print(1 if isBigraph else 0)
