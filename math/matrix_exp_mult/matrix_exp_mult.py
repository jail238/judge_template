# 2*2 matrix, change 2 to something

import sys
input = sys.stdin.readline
mod = 1000

def calc(m1, m2):
    global mod
    matrix = [[0] * 2 for _ in range(2)]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                matrix[i][j] += m1[i][k] * m2[k][j]
            matrix[i][j] %= mod
    return matrix

def func(mat, n):
    if n == 1:
        return mat
    else:
        if n % 2 == 0:
            new = func(mat, n // 2)
            return calc(new, new)
        else:
            return calc(func(mat, n-1), mat)

matrix = [[1, 0], [0, 1]] 
func(matrix, n)
