#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

"""

# -*- coding: utf-8 -*-


import random
import numpy as np

def MCint(f, a, b, n):
    s = 0
    for i in range(n):
        x = random.uniform(a, b)
        s += f(x)
        
    I = (float(b-a)/n)*s
    return I

def MCint_vec(f, a, b, n):
    x = random.uniform(a, b, n)
    s = sum(f(x))
    I = (float(b-a)/n)*s
    return I

def MCint2(f, a, b, n):
    s = 0
    I = np.zeros(n)
    for k in range(1, n+1):
        x = random.uniform(a, b)
        s += f(x)
        I[k-1] = (float(b-a)/k)*s
    return I

def MCint3(f, a, b, n, N=100):
    s = 0
    
    I_valores = []
    k_valores = []
    
    for k in range(1, n+1):
        x = random.uniform(a, b)
        s += f(x)
        if k % N == 0:
            I = (float(b-a)/k)*s
            I_valores.append(I)
            k_valores.append(k)
    return k_valores, I_valores
