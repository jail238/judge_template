import math, operator, sys
input = sys.stdin.readline

class SegTree:
    __slots__ = ("n", "op", "e", "t")
    INF = int(1e18)

    def merge(self, l, r):
        suml, prefl, suffl, bestl = l
        sumr, prefr, suffr, bestr = r
        sum_lr = suml+sumr
        pref_lr = max(prefl, suml+prefr)
        suff_lr = max(suffr, sumr+suffl)
        best_lr = max(bestl, bestr, suffl+prefr)
        return (sum_lr, pref_lr, suff_lr, best_lr)

    def __init__(self, arr, mode, inf=INF):
        self.n = len(arr)
        if mode == "+":
            self.op = operator.add
            self.e = 0
        elif mode == "gcd":
            self.op = math.gcd
            self.e = 0
        elif mode == "xor":
            self.op = operator.xor
            self.e = 0
        elif mode == "min":
            self.op = min
            self.e = inf
        elif mode == "max":
            self.op = max
            self.e = -inf
        elif mode == "maxsub":
            self.op = self.merge
            self.e = (0, -inf, -inf, -inf)

        n, e, op = self.n, self.e, self.op
        t = [e]*(2*n)
        t[n:n+n] = arr
        for i in range(n-1, 0, -1): t[i] = op(t[i<<1],t[i<<1|1])
        self.t = t
    
    def update(self, idx, val):
        n, t, op = self.n, self.t, self.op
        i = idx+n
        t[i] = val
        i >>= 1
        while i:
            t[i] = op(t[i<<1], t[i<<1|1])
            i >>= 1
        
    def query(self, l, r):
        n, t, op, sml, smr = self.n, self.t, self.op, self.e, self.e
        l += n; r += n+1
        while l < r:
            if l&1:
                sml = op(sml, t[l])
                l += 1
            if r&1:
                r -= 1
                smr = op(t[r], smr)
            l >>= 1; r >>= 1
        return op(sml, smr)

    def get(self, idx):
        return self.t[self.n+idx]
