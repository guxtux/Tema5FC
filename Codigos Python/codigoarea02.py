#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

"""
import random
import time
import numpy as np
import matplotlib.pyplot as plt


def MCint_area(f, a, b, n, m):
    abajo = 0  
    for i in range(n):
        x = random.uniform(a, b)
        y = random.uniform(0, m)
        if y <= f(x):
            abajo += 1
    area = abajo/float(n)*m*(b-a)
    return area



def MCint_area_vec(f, a, b, n, m):
    x = np.random.uniform(a, b, n)
    y = np.random.uniform(0, m, n)
    abajo = np.sum(y < f(x))
    area = abajo/float(n)*m*(b-a)
    return area

def MCint3_area(f, a, b, n, m, N=1000):
    I_valores = []
    k_valores = []
    abajo = 0  # counter for no of points below the curve
    for k in range(1, n+1):
        x = random.uniform(a, b)
        y = random.uniform(0, m)
        if y <= f(x):
            abajo += 1
        area = abajo/float(k)*m*(b-a)
        if k % N == 0:
            I = area
            I_valores.append(I)
            k_valores.append(2*k)
            
    return k_valores, I_valores


def f1(x):
    return 2 + 3*x

a = 1; b = 2; n = 1000000; N = 10000; fmax = f1(b)

t0 = time.clock()
print (MCint_area(f1, a, b, n, fmax))
t1 = time.clock()
print (MCint_area_vec(f1, a, b, n, fmax))
t2 = time.clock()
print ('fraccion bucle/vectorizado', (t1 - t0)/(t2 - t1))

k, I = MCint3_area(f1, a, b, n, fmax, N)

print (I[-1])

error = 6.5 - np.array(I)

plt.plot(k, error, label='Integracion Monte Carlo')
plt.xlabel('Numero de puntos')
plt.ylabel('Error')
plt.show()
