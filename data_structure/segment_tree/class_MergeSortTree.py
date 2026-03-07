import sys
from bisect import bisect_right
input = sys.stdin.readline

class MergeSortTree:
    __slots__ = ("n", "t")

    def __init__(self, arr):
        n = len(arr)
        self.n = n
        t = [[] for _ in range(2*n)]
        for i, v in enumerate(arr): t[n+i] = [v]
        for i in range(n-1, 0, -1):
            a = t[i<<1]
            b = t[i<<1|1]
            la, lb = len(a), len(b)
            m = [0]*(la+lb)
            pa = pb = k = 0
            while pa < la and pb < lb:
                if a[pa] <= b[pb]: m[k] = a[pa]; pa += 1
                else: m[k] = b[pb]; pb += 1
                k += 1
            if pa < la: m[k:] = a[pa:]
            else: m[k:] = b[pb:]
            t[i] = m
        self.t = t

    def count(self, l, r, k):
        # count [x, y] => k -> x, y; bisect_right(y)-bisect_left(x)
        n, t = self.n, self.t
        l += n; r += n+1
        ans = 0
        while l < r:
            if l&1:
                vec = t[l]
                # ans += bisect_right(vec, k) #  <= k count
                ans += len(vec)-bisect_right(vec, k) # k > count
                l += 1
            if r&1:
                r -= 1
                vec = t[r]
                ans += len(vec)-bisect_right(vec, k) # k > count
                # ans += bisect_right(vec, k) #  <= k count
            l >>= 1; r >>= 1
        return ans
