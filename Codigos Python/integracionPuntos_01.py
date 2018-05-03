# -*- coding: utf-8 -*-
"""
Created on Thu May 18 17:31:11 2017

@author: Master Chief
"""
import random
import numpy as np
import matplotlib.pyplot as plt
import time


def MCint_area(f, a, b, n, m):
    porDebajo = 0 # counter for no of points below the curve
    for i in range(n):
        x = random.uniform(a, b)
        y = random.uniform(0, m)
        if y <= f(x):
            porDebajo += 1
    area = porDebajo/float(n)*m*(b-a)
    
    return area

def MCint_area_vect(f, a, b, n, m):
    x = random.uniform(a, b, n)
    y = random.uniform(0, m, n)
    below = y[y < f(x)].size
    area = below/float(n)*m*(b-a)
    return area

def f1(x):
    return 2 + 3*x

a = 1; b = 2; n = 1000000; N = 10000; fmax = f1(b)

t0 = time.clock()
print (MCint_area(f1, a, b, n, fmax))
t1 = time.clock()
print (MCint_area_vect(f1, a, b, n, fmax))
t2 = time.clock()
print ('loop/vectorized fraction:', (t1-t0)/(t2-t1))

k, I = MCint_area(f1, a, b, n, fmax, N)
print (I[-1])

error = 6.5 - np.array(I)

plt.plot(k, error, label='Monte Carlo integration')
plt.xlabel('number of samples')
plt.ylabel('error')
#plt.savefig('tmp.pdf')
plt.show()