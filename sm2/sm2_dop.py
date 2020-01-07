import numpy as np
import random
import math

def IRNUNI(ILOW, IUP):
    return int((IUP - ILOW + 1)*random.random() + ILOW)

def kolmogorov_test(a, b, n):
    u = np.array([IRNUNI(a, b) for _ in range(n)])
    maxD = 0
    f = open('sm2_dop.csv', 'w')
    for x in range(a, b+1, 1):
        fn_x = (u <= x).sum() / n
        f0_x = (x - a + 1) / (b - a + 1)
        maxD = max(maxD, abs(fn_x - f0_x))
        print(f'x = {x}, Fn(x) = {fn_x}, F0(x) = {f0_x}')
        f.write(f'{x},{fn_x},{f0_x}\n')

    lam = math.sqrt(n) * maxD
    print(f'maxD = {maxD}, lambda = {lam}')
    f.write(f'{maxD}, {lam}')

kolmogorov_test(1, 100, 10**4)