import random
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import math

def plot_raspr(u, n):

    u.sort()
    intervals = np.array(range(int(np.min(u)), int(np.max(u)), 1))
    cumulativeFreq = [(u <= r).sum() / n for r in intervals]
    frequencies = [cumulativeFreq[i + 1] - cumulativeFreq[i] for i in range(len(cumulativeFreq) - 1)]

    plt.figure()
    plt.plot(intervals, cumulativeFreq)

    plt.figure()
    plt.ylim(0, max(frequencies) * 10)
    plt.plot(intervals[:-1], frequencies)
    plt.show()

def calc_m_d(list):
    m = np.sum(list) / len(list)
    d = np.sum([(val - m)**2 for val in list]) / len(list)
    return m, d

def IRNUNI(ILOW, IUP):
    return int((IUP - ILOW + 1)*random.random() + ILOW)

def RNNORM(N, p):
    r = random.random()
    temp_p = (1-p)**N
    sum = temp_p
    for i in range(N):
        if(sum > r):
            return i
        temp_p *= (float(N-i) / float(i+1))*(p / (1-p))
        sum += temp_p
    return N

def IRNGEO_1(p):
    pr = np.random.uniform(0, p)
    otrezok = 0
    while(p > pr):
        otrezok += 1
        pr /= p
    return otrezok
def IRNGEO_2(p):
    r = np.random.random()
    count = 1
    while(r > p):
        count+=1
        r = np.random.random()
    return count
def IRNGEO_3(p):
    u = random.random()
    k = int(math.log(u) / math.log(1-p)) + 1
    return k

def IRNPSN(mu):
    r = random.random()
    k = 0
    while(r >= math.exp(-mu)):
        r *= random.random()
        k += 1
    return k


def IRNUNI_TEST(ILOW, IUP, N):
    r = [IRNUNI(ILOW, IUP) for _ in range(N)]
    m, d = calc_m_d(r)
    t_m = (ILOW + IUP) / 2
    t_d = ((IUP - ILOW + 1) ** 2 - 1) / 12

    print(pd.DataFrame(data={'Оценка': ['@M@', '@D@'], 'IRNUNI': [m, d],
                             'Погрешность': [abs(m - t_m), abs(d - t_d)],
                             'Теоретическое значение': [t_m, t_d]}))
    plot_raspr(r, N)

def RNNORM_TEST(N, p, size):

    r1 = [RNNORM(N, p) for _ in range(size)]
    #r1 = [int(np.random.binomial(N, p)) for _ in range(size)]
    r2 = [int(np.random.normal(N * p, np.sqrt(N * p * (1 - p))) + 0.5) for _ in range(size)]

    m1, m2 = np.sum(r1) / size, np.sum(r2) / size
    d1, d2 = np.sum([(x - m1)**2 for x in r1]) / size, np.sum([(x-m2)**2 for x in r2]) / size
    t_m = N*p
    t_d = N*p*(1-p)

    print(pd.DataFrame(data = {'Оценка':['@M@', '@D@'],
        'IRNBIN':[m1, d1], 'IRNBNL': [m2, d2],
        'Теоретическое значение':[t_m, t_d]}))

    plot_raspr(r1, size)
    plot_raspr(r2, size)

def IRNGEO_TEST(p, size):
    r1 = [IRNGEO_1(p) for _ in range(size)]
    r2 = [IRNGEO_2(p) for _ in range(size)]
    r3 = [IRNGEO_3(p) for _ in range(size)]
    m1, d1 = calc_m_d(r1)
    m2, d2 = calc_m_d(r2)
    m3, d3 = calc_m_d(r3)
    t_m = 1/p
    t_d = (1-p)/(p**2)
    print(pd.DataFrame(data = {'Оценка':['@M@', '@D@'],
        'IRNGEO_1':[m1, d1], 'IRNGEO_2':[m2, d2], 'IRNGEO_3': [m3, d3],
        'Теоретическое значение':[t_m, t_d]}))

    plot_raspr(r1, size)
    plot_raspr(r2, size)
    plot_raspr(r3, size)

def IRNPSN_TEST(mu, size):

    r1 = np.random.poisson(mu, size)
    r2 = [IRNPSN(mu) for _ in range(size)]
    m1, d1 = calc_m_d(r1)
    m2, d2 = calc_m_d(r2)
    t_m = mu
    t_d = mu

    print(pd.DataFrame(data = {'Оценка':['@M@', '@D@'],
        'IRNPOI':[m1, d1], 'IRNPSN':[m2, d2],
        'Теоретическое значение':[t_m, t_d]}))

    plot_raspr(r1, size)
    plot_raspr(r2, size)

def IRNLOG_TEST(q, size):
    p = 1 - q
    alpha = 1 / math.log(p)
    r = np.random.logseries(p, size)
    m, d = calc_m_d(r)
    t_m = -alpha*q/p
    t_d = -alpha*q*(1+alpha*q)/p**2

    print(pd.DataFrame(data = {'Оценка':['@M@', '@D@'],
        'IRNLOG':[m, d], 'Отклон':[abs(m - t_m), abs(d - t_d)],
        'Теоретическое значение':[t_m, t_d]}))
    plot_raspr(r, size)

#IRNUNI_TEST(1, 100, 10**4)
#RNNORM_TEST(10, 0.5, 10**4)
#IRNGEO_TEST(0.5, 10**4)
#IRNPSN_TEST(10, 10**4)
#IRNLOG_TEST(0.5, 10**4)

while True:

    inp = input("\nВыберите тип распределения: \n1 - равномерное\n2 - биномиальное\n"
                "3 - геометрическое\n4 - пуассона\n5 - логарифмическое\n > ")
    if inp == '1':
        IRNUNI_TEST(1, 100, 10**4)
    elif inp == '2':
        RNNORM_TEST(10, 0.5, 10**4)
    elif inp == '3':
        IRNGEO_TEST(0.5, 10**4)
    elif inp == '4':
        IRNPSN_TEST(10, 10**4)
    elif inp == '5':
        IRNLOG_TEST(0.5, 10**4)

    if input("продолжить? [1 - да, 0 - нет] \n > ") == '0':
        break

