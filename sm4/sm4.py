import numpy as np
from itertools import product
import math
from random import random as rand

def schemeWorking(x, part):
    if part == 0:
        return (x[0][0] and x[0][1]) or (x[0][2] and x[0][3])
    if part == 1:
        return x[1][0] and x[1][1]
    if part == 2:
        return (x[2][0] and x[2][1]) or (x[2][2] and x[2][3]) or (x[2][4] and x[2][5])

M = 3
lam = [40e-6, 10e-6, 80e-6]
n = [4, 2, 6]
T, P0, eps, ta = 8760, 0.999, 0.001, 3.090
N = int(ta**2 * ((P0*(1-P0)) / eps**2))
t = [[0 for _ in range(n[i])] for i in range(M)]
x = [[False for _ in range(n[i])] for i in range(M)]

print(lam)
print('N = ', N)

for Lsum in range(100):
    #Звёздочки и чёрточки
    L = [np.array(i) for i in product(range(Lsum + 1), repeat=M) if sum(i) == Lsum]

    for Lidx in range(len(L)):
        d = 0
        for _ in range(N):
            for i in range(M):

                for j in range(n[i]):
                    t[i][j] = -math.log(rand())/lam[i]

                idMin = np.argmin(t[i])

                for _ in range(L[Lidx][i]):
                    t[i][idMin] -= math.log(rand())/lam[i]
                    idMin = np.argmin(t[i])

                for j in range(n[i]):
                    x[i][j] = t[i][j] > T

                if not schemeWorking(x, i):
                    d += 1
                    break

        PT = 1 - d/N
        print(Lsum, ' ', L[Lidx], 'P(T) = {:.4f}'.format(PT), end = ' ')

        if(PT > P0):
            print('OK')
        else:
            print()
