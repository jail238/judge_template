import sys
input = sys.stdin.readline
MOD = 998244353

def NTT(arr, inv):
    n = len(arr)
    if n == 1: return arr
    r = [0 for _ in range(n)]
    for i in range(n):
        r[i] = r[i>>1]>>1
        if i&1: r[i] |= n>>1
        if i < r[i]: arr[i], arr[r[i]] = arr[r[i]], arr[i]
    
    exp = pow(3, (MOD-1)//n, MOD)
    if inv: exp = pow(exp, MOD-2, MOD)
    root = [0 for _ in range(n)]
    root[0] = 1
    for i in range(1, n): root[i] = (root[i-1]*exp)%MOD
    i = 2
    while i <= n:
        step = n//i
        for j in range(0, n, i):
            for k in range(i>>1):
                u, v = arr[j|k], (arr[j|k|i>>1]*root[step*k])%MOD
                arr[j|k], arr[j|k|i>>1] = (u+v)%MOD, (u-v)%MOD
        i <<= 1

    t = pow(n, MOD-2, MOD)
    if inv:
        for i in range(n): arr[i] = (arr[i]*t)%MOD

    return arr

def mult(a, b):
    n = 1
    while n < len(a)+len(b): n <<= 1
    a = a+[0]*(n-len(a))
    b = b+[0]*(n-len(b))
    arr1 = NTT(a, False)
    arr2 = NTT(b, False)
    conv = [(arr1[i]*arr2[i])%MOD for i in range(n)]
    intt = NTT(conv, True)
    return intt

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
print(mult(a, b))
