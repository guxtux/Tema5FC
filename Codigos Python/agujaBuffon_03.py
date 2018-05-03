# -*- coding: utf-8 -*-
"""
Created on Thu May 18 11:05:10 2017

@author: Master Chief
"""


import math
import numpy
import matplotlib.pyplot as plt
import matplotlib.font_manager as font_manager
import random

font_path = 'C:\Windows\Fonts\consola.ttf'
font_prop = font_manager.FontProperties(fname=font_path, size=12)

CL = 0
NN = 0
 
PIa = []
PIb = []
NNa = []
PIc = []
ANGLES = []
 
for ii in range(10000):
 
    PPy = random.uniform(0.0,1.0) #A-end y position (lines separated by unit distance)
 
    RRx = random.uniform(0.0,1.0) #x projection
    RRy = numpy.sqrt(1.0 - RRx**2) #y projection
 
    QQy = PPy + RRy #B-end y position
    QQyf = math.floor(QQy)
    PPyf = math.floor(PPy)
 
    NN = NN + 1
    if (QQyf-PPyf > 0.0): #if crossing line
        CL = CL + 1
 
    NNa.append(NN)
    PIc.append(math.pi)
    RAT = (1.0*CL)/(1.0*NN)
    if (CL==0):
        PIa.append(0)
    else:
        PIa.append(2.0/RAT)
 
    PIb.append(4*RAT)
 
    ANGLES.append(abs(math.atan(RRy/(RRx+0.0001)))/math.pi)
 
print (PIa[-1])
print (PIb[-1])
 
plt.figure(1)
plt.xlabel("Total de Agujas")
plt.ylabel("2 A_T / A_C")
plt.plot(NNa,PIc,'r')
plt.plot(NNa,PIa,'k')
#plt.savefig('DPI1.png')
# 
#plt.figure(2)
#plt.hist(ANGLES, bins=10)
#plt.xlabel("Acute angle in factors of pi")
#plt.ylabel("Needles dropped")
#plt.savefig('DPI2.png')
 
plt.figure(2)
plt.xlabel("Total de agujas")
plt.ylabel("Valor aproximado de $\pi$")
plt.plot(NNa,PIc,'r')
plt.plot(NNa,PIb,'k', label='Agujas =' + str(NN))
plt.legend(loc=1, prop=font_prop)
plt.title('Aproximación del valor de $\pi$ \ncon el número de agujas que cruzan')
#plt.savefig('aproximacionPi_' +str(NN)+'.eps')
 
plt.show()