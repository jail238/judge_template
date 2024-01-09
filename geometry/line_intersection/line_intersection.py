#BOJ 17387

def ccw(t1, t2, t3):
    x1, y1 = t1
    x2, y2 = t2
    x3, y3 = t3
    s = (x2-x1)*(y3-y1)-(y2-y1)*(x3-x1)
    if s > 0:
        return 1
    elif s == 0:
        return 0
    else:
        return -1

x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())

if ccw((x1, y1), (x2, y2), (x3, y3))*ccw((x1, y1), (x2, y2), (x4, y4)) == 0 and ccw((x3, y3), (x4, y4), (x1, y1))*ccw((x3, y3), (x4, y4), (x2, y2)) == 0:
    if min(x1, x2) <= max(x3, x4) and min(x3, x4) <= max(x1, x2) and min(y1, y2) <= max(y3, y4) and min(y3, y4) <= max(y1, y2):
        print(1)
    else:
        print(0)
elif ccw((x1, y1), (x2, y2), (x3, y3))*ccw((x1, y1), (x2, y2), (x4, y4)) <= 0 and ccw((x3, y3), (x4, y4), (x1, y1))*ccw((x3, y3), (x4, y4), (x2, y2)) <= 0:
    print(1)
else:
    print(0)
