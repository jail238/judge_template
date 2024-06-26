def incode(x):
    if x == 0: return ["!"]
    w = []
    while x > 0:
        w.append(chr(x%93+33))
        x //= 93
    return ''.join(w)

def decode(x):
    w = 0
    for i in range(len(x)):
        w += (ord(x[i])-33)*(93**i)
    return w
