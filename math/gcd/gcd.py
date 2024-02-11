import sys
input = sys.stdin.readline

def gcd(a, b): # 사실 math.gcd하면 다 해준다
    while b != 0:
        a, b = b, a%b
    return a

a, b = map(int, input().split())
print(gcd(a, b))
