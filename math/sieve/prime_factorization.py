import sys
input = sys.stdin.readline

def prime_fac(n):
    div, i, k = {}, 3, n
    while k%2 == 0:
        if not 2 in div: div[2] = 1
        else: div[2] += 1
        k //= 2
    while i*i <= k:
        while k%i == 0:
            if not i in div: div[i] = 1
            else: div[i] += 1
            k //= i
        i += 2
    if k != 1: div[k] = 1
    return div

def divisors(divs):
    factors = [1]
    for pr, exp in divs.items():
        new_divs = []
        for d in factors:
            for i in range(1, exp+1):
                new_divs.append(d*(pr**i))
        factors.extend(new_divs)
    return factors

n = int(input())
divs = prime_fac(n)
factors = divisors(divs)
