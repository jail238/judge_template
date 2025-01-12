from collections import deque
import sys
input = sys.stdin.readline

class Dinic:
    def __init__(self, n): # size of graph
        self.n = n
        self.adj = [[] for _ in range(n)]
    
    def add_edge(self, a, b, cap):
        self.adj[a].append([b, len(self.adj[b]), cap])
        self.adj[b].append([a, len(self.adj[a])-1, 0])
    
    def bfs(self, S, T, lvl):
        for i in range(len(lvl)): lvl[i] = -1
        lvl[S] = 0
        q = deque([S])

        while q:
            now = q.popleft()
            for edge in self.adj[now]:
                nxt, cap = edge[0], edge[2]
                if cap > 0 and lvl[nxt] == -1:
                    lvl[nxt] = lvl[now]+1
                    q.append(nxt)
        return lvl[T] >= 0

    def dfs(self, now, dest, lvl, flow, work):
        if now == dest: return flow
        while work[now] < len(self.adj[now]):
            edge = self.adj[now][work[now]]
            nxt, rev, cap = edge
            if cap > 0 and lvl[nxt] == lvl[now]+1:
                tmp = self.dfs(nxt, dest, lvl, min(flow, cap), work)
                if tmp > 0:
                    self.adj[nxt][rev][2] += tmp
                    self.adj[now][work[now]][2] -= tmp
                    return tmp
            work[now] += 1
        return 0
    
    def max_flow(self, S, T):
        if S == T: return -1
        INF = int(1e9)
        total_flow = 0
        lvl = [-1 for _ in range(self.n)]

        while self.bfs(S, T, lvl):
            work = [0 for _ in range(self.n)]
            while flow := self.dfs(S, T, lvl, INF, work): total_flow += flow
        return total_flow

# def in_node(v): return 2*v -> 정점 분할
# def out_node(v): return 2*v+1 -> 정점 분할

n, m = map(int, input().split())
INF, SIZE = int(1e9), 500
dinic = Dinic(SIZE)
# for i in range(1, n+1): dinic.add_edge(in_node(i), out_node(i), cap) -> 정점 분할
for _ in range(m):
    a, b, c = map(int, input().split())
    dinic.add_edge(a, b, c) # -> a->b 간선, 용량: c
    # dinic.add_edge(out_node(a), in_node(b), INF) -> 정점 분할
    # dinic.add_edge(out_node(b), in_node(a), INF) -> 정점 분할
src, sink = 0, 1 # out_node(0), in_node(1) -> 정점 분할
flow = dinic.max_flow(src, sink)
print(flow)
