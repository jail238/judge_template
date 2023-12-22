import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def switch(x):
    if x > 0: return 2*x-1
    else: return 2*abs(x)

def scc(node):
    global ids, scc_cnt
    ids_arr[node], parents[node] = ids, ids
    ids += 1; visited[node] = True
    stack.append(node)
    
    for now in graph[node]:
        if ids_arr[now] == 0:
            scc(now)
            parents[node] = min(parents[now], parents[node])
        elif visited[now]:
            parents[node] = min(parents[now], parents[node])
    
    w = -1
    if parents[node] == ids_arr[node]:
        while w != node:
            w = stack.pop()
            scc_idx[w] = scc_cnt
            visited[w] = False
        scc_cnt += 1

v, e = map(int, input().split())
graph = [[] for _ in range((2*(v+1)))]
for _ in range(e):
    a, b = map(int, input().split())
    if not a == b: graph[switch(-a)].append(switch(b))
    graph[switch(-b)].append(switch(a))

stack = []
visited = [False]*(2*v+1)
ids, ids_arr = 1, [0]*(2*v+1)
parents, scc_idx, scc_cnt = [0]*(2*v+1), [-1]*(2*v+1), 0

for i in range(1, 2*v+1):
    if ids_arr[i] == 0: scc(i)

ans = [0] * v
for i in range(1, 2*v, 2):
    if scc_idx[i] == scc_idx[i+1]:
        print(0)
        exit()
    if scc_idx[i] < scc_idx[i+1]: # retracing
        ans[i//2] = 1
print(1)
print(*ans)
