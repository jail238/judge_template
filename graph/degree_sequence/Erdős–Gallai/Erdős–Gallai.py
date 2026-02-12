def is_graphical(a):
    a.sort(reverse=True)
    n = len(a)
    presum = [0 for _ in range(n+1)]
    for i in range(n): presum[i+1] = presum[i]+a[i]
    if presum[-1]&1: return 0
    p = n
    for k in range(1, n+1):
        if p<k: p=k
        while p>k and a[p-1]<k: p -= 1
        if presum[k] > k*(k-1)+k*(p-k)+(presum[n]-presum[p]): return 0
    return 1
