import numpy as np
import pandas as pd

np.random.seed(2)


def LU_decomposition(A):
    n = len(A[0])
    L = np.zeros([n, n])
    U = np.zeros([n, n])
    for i in range(n):
        L[i][i] = 1
        if i == 0:
            U[0][0] = A[0][0]
            for j in range(1, n):
                U[0][j] = A[0][j]
                L[j][0] = A[j][0] / U[0][0]
        else:
            for j in range(i, n):  # U
                temp = 0
                for k in range(0, i):
                    temp = temp + L[i][k] * U[k][j]
                U[i][j] = A[i][j] - temp
            for j in range(i + 1, n):  # L
                temp = 0
                for k in range(0, i):
                    temp = temp + L[j][k] * U[k][i]
                L[j][i] = (A[j][i] - temp) / U[i][i]
    return L, U


if __name__ == '__main__':
    A = [[21, 32, 14, 8, 6, 9, 11, 3, 5], [17, 2, 8, 14, 55, 23, 19, 1, 6], [41, 23, 13, 5, 11, 22, 26, 7, 9], [12, 11, 5, 8, 3, 15, 7, 25, 19], [14, 7, 3, 5, 11, 23, 8, 7, 9], [2, 8, 5, 7, 1, 13, 23, 11, 17], [11, 7, 9, 5, 3, 8, 26, 13, 17], [23, 1, 5, 19, 11, 7, 9, 4, 16], [31, 5, 12, 7, 13, 17, 24, 3, 11]]
    L, U = LU_decomposition(A)
    print(L, '\n', U)