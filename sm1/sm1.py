import numpy as np
import matplotlib.pyplot as plt
import random
import math
from collections import Counter


def calc(n):
    u = [random.random() for _ in range(n)]
    m = np.sum(u) / n
    d = np.sum([ (x - m)**2 for x in u ]) / n
    s = math.sqrt(d)
    k = [ np.sum( [(u[i] - m)*(u[i+f+1] - m) for i in range(n-f-1)] ) / (d * n) for f in range(n)]
    print(f' n = {n} \n M = {m} \n D = {d} \n S = {s}\n')

    plt.figure()
    plt.plot(range(n), k)
    #plt.savefig(f'correlogram_{n}.png')

    #func raspredelenie
    u.sort()
    plt.figure()
    plt.plot(np.linspace(0, 1, n), u)
    #plt.savefig(f'f_rasp_{n}.png')

    #func plotnost
    numIntervals = max(3, int(n/10))
    intervals = np.linspace(0, 1, numIntervals)
    cumulativeFreq = [(u < r).sum() / n for r in intervals]
    frequencies = [cumulativeFreq[i+1] - cumulativeFreq[i] for i in range(len(cumulativeFreq) - 1)]
    plt.figure()
    plt.ylim(max(frequencies) * -10, max(frequencies) * 10)
    plt.plot(intervals[1:], frequencies)
    #plt.savefig(f'f_plotn_{n}.png')


for n in [10, 100, 1000, 10000]:
    calc(n)