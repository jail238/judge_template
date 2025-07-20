import sys
input = sys.stdin.readline

class PushRelabel:
    def __init__(self, v):
        self.v = v
        self.inf = int(1e9)
        self.adj = [[] for _ in range(v)]
        self.edge_list = []
        self.h = [0 for _ in range(v)]
        self.f = [0 for _ in range(v)]
    
    def add_edge(self, u, v, capacity):
        self.edge_list.append([v, capacity, 0, len(self.edge_list)+1])
        self.adj[u].append(len(self.edge_list)-1)
        self.edge_list.append([u, 0, 0, len(self.edge_list)-1])
        self.adj[v].append(len(self.edge_list)-1)
    
    def push(self, u, edge_idx):
        edge = self.edge_list[edge_idx]
        v = edge[0]
        d = min(self.f[u], edge[1]-edge[2])
        edge[2] += d
        self.edge_list[edge[3]][2] -= d
        self.f[u] -= d; self.f[v] += d
    
    def relabel(self, u):
        min_h = self.inf
        for edge_idx in self.adj[u]:
            edge = self.edge_list[edge_idx]
            if edge[1] > edge[2]:
                v = edge[0]
                min_h = min(min_h, self.h[v])
        if min_h < self.inf: self.h[u] = min_h+1
    
    def find_max_h(self, s, t):
        max_h_v = []
        max_h = -1
        for i in range(self.v):
            if i != s and i != t and self.f[i] > 0:
                if self.h[i] > max_h:
                    max_h = self.h[i]
                    max_h_v = []
                if self.h[i] == max_h: max_h_v.append(i)
        return max_h_v
    
    def max_flow(self, s, t):
        self.h[s] = self.v
        self.f[s] = self.inf
        for edge_idx in self.adj[s]: self.push(s, edge_idx)
        while True:
            V = self.find_max_h(s, t)
            if not V: break
            for u in V:
                pushed = False
                for edge_idx in self.adj[u]:
                    if self.f[u] == 0: break
                    edge = self.edge_list[edge_idx]
                    v = edge[0]
                    if edge[1] > edge[2] and self.h[u] == self.h[v]+1:
                        self.push(u, edge_idx)
                        pushed = True
                if not pushed:
                    self.relabel(u)
                    break
        return self.f[t]

SIZE = 1111
FLOW = PushRelabel(SIZE)
