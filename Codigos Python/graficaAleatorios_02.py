# -*- coding: utf-8 -*-
"""
Created on Tue May 16 16:24:17 2017

@author: Master Chief
"""

import matplotlib.pyplot as plt
import random

def arreglonumeros(muestra=500, semilla=None):
    x = []
    random.seed(semilla)
    
    for i in range(muestra):
        nuevoValor = random.random()
        x.append(nuevoValor)
    
    return x

x1 = arreglonumeros()
x2 = arreglonumeros(semilla=500)
x3 = arreglonumeros(semilla=2018)

plt.figure(figsize=(8,5)) 
plt.plot(x1,'b+', label='seed = reloj sistema')
plt.plot(x2,'r+', label='seed = 500')
plt.plot(x3,'y+', label='seed = 2018')
plt.legend(loc='upper center', bbox_to_anchor=(0.93, 1.1), borderaxespad = 0.)
plt.title('Secuencia de números aleatorios')
plt.xlabel('x')
plt.ylabel('y')
plt.show()