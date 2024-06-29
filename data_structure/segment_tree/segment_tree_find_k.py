from math import log2, ceil
import sys
input = sys.stdin.readline

from math import log2, ceil
import sys
input = sys.stdin.readline

def init(n, h):
    for i in range(n):
        tree[2**h+i] = l[i]
    for i in range(2**h-1, 0, -1):
        tree[i] = tree[i<<1] + tree[(i<<1)^1]
def query(rank, end): # 몇 번째에 있는지 확인
    s = 1
    while s < end:
        if tree[s*2] >= rank:
            s = 2*s
        else:
            rank -= tree[s*2]
            s = 2*s+1
    return s-end

def update(idx, val, start): # 구간 합 업데이트
    start += idx; tree[start] += val
    while start > 1:
        if start&1:
            tree[start//2] = tree[start-1] + tree[start]
        else:
            tree[start//2] = tree[start] + tree[start+1]
        start //= 2

n = int(input())
h = ceil(log2(n))
tree = [0 for _ in range(2**(h+1))]
l = list(map(int, input().split()))
init(n, h)
