import sys
input = sys.stdin.readline

def ccw(t1, t2, t3):
    x1, y1 = t1[0], t1[1]
    x2, y2 = t2[0], t2[1]
    x3, y3 = t3[0], t3[1]
    s = (x2-x1)*(y3-y1)-(y2-y1)*(x3-x1)
    if s >= 0:
        return True
    else:
        return False
