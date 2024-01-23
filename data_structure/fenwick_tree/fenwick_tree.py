import sys
input = sys.stdin.readline

def bit_sum(x): #range 1~n sum
    val = 0
    while i > 0:
        val += tree[i]
        i -= (i & -i)
    
    return val

def bit_add(idx, val, n): #init
    while i <= n:
        tree[i] += val
        i += (i & -i)

def bit_update(idx, val): #update
    bit_add(idx, val)

def bit_range_query(l, r):
    return bit_sum(r) - bit_sum(l-1)

def bit_range_update(l, r, val): #range update
    add(l, x)
    add(r+1, -x)

def point_query(idx): #array value
    return bit_sum(idx)
