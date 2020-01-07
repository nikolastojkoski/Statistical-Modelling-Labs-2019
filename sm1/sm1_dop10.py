import numpy as np
import random
import math
from collections import Counter

def permutation_test(t, n):
    u = [random.random() for _ in range(n)]
    numIntervals = int(n / t)
    combCount = Counter()
    for i in range(numIntervals):
        sublist = [(u[i*t + j], j) for j in range(t)]
        sublist.sort(key=lambda v: v[0])
        combinationId = 0
        for j in range(t):
            combinationId += sublist[j][1]*(10**j)
        combCount[combinationId] += 1

    v = [x[1] for x in combCount.items()]
    t_fact = math.factorial(t)
    num_zero_combs = t_fact - len(v)
    term = (n/t)*(1/t_fact)
    sum = np.sum([(vi - term)**2 for vi in v])
    sum += num_zero_combs * (-(n/t)*(1/t_fact))**2
    chi2 = (1/((n/t)*(1/t_fact)))*sum
    return chi2

print('t,  N,  chi2')
for t in range(2, 20, 1):
    t_fact = math.factorial(t)
    N = t_fact - 1
    chi2 = permutation_test(t, 10**4)
    print(t, ' ', N, ' ', chi2)