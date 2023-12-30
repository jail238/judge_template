import sys
input = sys.stdin.readline

def ccw(t1, t2, t3):
    x1, y1 = t1
    x2, y2 = t2
    x3, y3 = t3
    s = (x2-x1)*(y3-y1)-(y2-y1)*(x3-x1)
    if s > 0:
        return True
    else:
        return False

n = int(input())
dots, bottom_convex_hull, top_convex_hull = [], [], []
for _ in range(n):
    dots.append(tuple(map(int, input().split())))

dots.sort()
bottom_convex_hull.append(dots[0])
bottom_convex_hull.append(dots[1])

for i in range(2, n):
    bottom_convex_hull.append(dots[i])
    p = True
    while p and len(bottom_convex_hull) > 2:
        d1 = bottom_convex_hull.pop()
        d2 = bottom_convex_hull.pop()
        if ccw(bottom_convex_hull[-1], d2, d1):
            bottom_convex_hull.append(d2)
            bottom_convex_hull.append(d1)
            p = False
        else:
            bottom_convex_hull.append(d1)

top_convex_hull.append(dots[-1])
top_convex_hull.append(dots[-2])

for i in range(n-3, -1, -1):
    top_convex_hull.append(dots[i])
    p = True
    while p and len(top_convex_hull) > 2:
        d1 = top_convex_hull.pop()
        d2 = top_convex_hull.pop()
        if ccw(top_convex_hull[-1], d2, d1):
            top_convex_hull.append(d2)
            top_convex_hull.append(d1)
            p = False
        else:
            top_convex_hull.append(d1)

top_convex_hull.pop()
bottom_convex_hull.pop()
convex_hull = bottom_convex_hull+top_convex_hull
