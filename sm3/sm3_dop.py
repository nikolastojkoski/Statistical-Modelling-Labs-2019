import random
import math
from scipy.stats import t

def RNNRM2(m, sigma):
    z = sum([random.random() for _ in range(12)]) - 6.0
    y = m + sigma * z
    return y

def RNCHIS(N):
    return sum([RNNRM2(0, 1)**2 for _ in range(N)])

def RNSTUD(N):
    return RNNRM2(0, 1) / math.sqrt(RNCHIS(N) / float(N))

def kolmogorov_test(N, n):
    u = sorted([RNSTUD(N) for _ in range(n)])
    maxD = 0
    f = open('sm3_dop.csv', 'w')
    for i in range(n):
        x = u[i]
        fn_x = (i+1)/n
        f0_x = t.cdf(x, N)
        maxD = max(maxD, abs(fn_x - f0_x))
        print(f'x = {x}, Fn(x) = {fn_x}, F0(x) = {f0_x}')
        f.write(f'{x},{fn_x},{f0_x}\n')

    lam = math.sqrt(n) * maxD
    print(f'maxD = {maxD}, lambda = {lam}')
    f.write(f'{maxD}, {lam}')

kolmogorov_test(10, 10**4)