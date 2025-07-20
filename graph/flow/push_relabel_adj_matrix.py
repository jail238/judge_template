import sys
input = sys.stdin.readline

class PushRelabel:
    def __init__(self, v):
        self.v = v
        self.inf = int(1e9)
        self.capacity = [[0 for _ in range(v)] for _ in range(v)]
        self.flow = [[0 for _ in range(v)] for _ in range(v)]
        self.h = [0 for _ in range(v)]
        self.f = [0 for _ in range(v)]

    def add_edge(self, u, v, capacity):
        self.capacity[u][v] += capacity

    def push(self, u, v):
        d = min(self.f[u], self.capacity[u][v]-self.flow[u][v])
        self.flow[u][v] += d; self.flow[v][u] -= d
        self.f[u] -= d; self.f[v] += d

    def relabel(self, u):
        min_h = self.inf
        for i in range(self.v):
            if self.capacity[u][i] > self.flow[u][i]: min_h = min(min_h, self.h[i])
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
        for i in range(self.v):
            if self.capacity[s][i] > 0:
                self.f[s] += self.capacity[s][i]
                self.push(s, i)

        while True:
            V = self.find_max_h(s, t)
            if not V: break
            for u in V:
                pushed = False
                for v in range(self.v):
                    if self.f[u] == 0: break
                    if self.capacity[u][v] > self.flow[u][v] and self.h[u] == self.h[v] + 1:
                        self.push(u, v)
                        pushed = True
                if not pushed:
                    self.relabel(u)
                    break
        total_flow = 0
        for i in range(self.v): total_flow += self.flow[i][t]
        return total_flow

SIZE = 1234
flow = PushRelabel(SIZE)
