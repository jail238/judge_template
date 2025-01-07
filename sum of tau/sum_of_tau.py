# τ(n) is number of divisors of n (n의 양의 약수의 개수)
# sum_tau(n) is τ(1)+τ(2)+...+τ(n) (O(sqrt(N)))
def sum_tau(n):
    s, e, res = 1, 0, 0
    while s <= n:
        e = (n//(n//s))
        res += (n//s)*(e-s+1)
        s = e+1
    return res
