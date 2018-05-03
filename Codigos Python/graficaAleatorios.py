# -*- coding: utf-8 -*-
"""
Created on Tue May 16 14:52:11 2017

@author: Master Chief
"""

import matplotlib as mpl
mpl.rcParams['font.family'] = 'Monospace'

import matplotlib.pyplot as plt

x = []
y = []

a, semilla, c, m, n = 128, 10, 0, 509, 500
for i in range (1, n):
   nuevasemilla = (a * semilla + c) % m
   semilla = nuevasemilla
   x.append( nuevasemilla)

a, semilla, c, m, n = 269, 10, 0, 2048, 500

for i in range (1, n):
   nuevasemilla = (a * semilla + c) % m
   semilla = nuevasemilla
   y.append( nuevasemilla)

#plt.plot(x, y, 'b+')
plt.figure(1)
plt.plot(x, 'b+')
plt.title('Secuencia de números aleatorios, a=128 y m=509', size=12)
plt.xlabel('x')
plt.show()

plt.figure(2)
plt.plot(y, 'r+')
plt.title(r'Secuencia de números aleatorios, a=269 y m=2048', size=12)
plt.xlabel('x')
plt.show()