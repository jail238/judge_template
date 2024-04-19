import sys
input = sys.stdin.readline

def dist(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return (x1-x2)**2+(y1-y2)**2

def find_pair_dist(s, e):
    res = int(1e10)
    for i in range(s, e):
        for j in range(i+1, e+1):
            res = min(res, dist(d[i], d[j])) 
    return res

def dnc_find(s, e):
    cnt = e-s+1
    if cnt <= 5: return find_pair_dist(s, e)
    m = (s+e)//2
    l, r = dnc_find(s, m), dnc_find(m+1, e)
    delta = min(l, r)
    dt = []

    for i in range(s, e+1):
        if (d[i][0]-d[m][0])**2 < delta:
            dt.append(d[i])
    dt.sort(key=lambda x:(x[1], x[0]))

    for i in range(len(dt)):
        for j in range(i+1, len(dt)):
            if (dt[i][1]-dt[j][1])**2 < delta:
                delta = min(dist(dt[i], dt[j]), delta)
            else:
                break
    
    return delta

n = int(input())
d = sorted([tuple(map(int, input().split())) for _ in range(n)])
delta = dnc_find(0, n-1)
print(delta)
