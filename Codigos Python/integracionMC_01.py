# -*- coding: utf-8 -*-


import random
import numpy as np
import matplotlib.pyplot as plt

title_font = {'fontname':'Roboto', 'size':'14', 'color':'black', 'weight':'normal',
              'verticalalignment':'bottom'} # Bottom vertical alignment for more space
axis_font = {'fontname':'Roboto', 'size':'12', 'color':'blue'}

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

def f1(x):
    return 2 + 3*x


k, I = MCint3(f1, 1, 2, 1000000, N=10000)

error = 6.5 - np.array(I)

plt.plot(k, error, color='k')
plt.xlabel('n')
plt.ylabel('error', **axis_font)
plt.title('Error obtenido con la integración Monte Carlo', **title_font)
plt.axhline(y=0, ls='dashed', lw=0.7, color='k')
#plt.savefig('integracionMC01.eps')
plt.show()