# -*- coding: utf-8 -*-
"""
Created on Thu May 18 10:32:32 2017

@author: Master Chief
"""

import numpy as np
import matplotlib.pylab as plt

class Buffon_needle_problem:

    def __init__(self,x,y,n,m):
        self.x = x #width of the needle
        self.y = y #witdh of the space
        self.r = []#coordinated of the centre of the needle
        self.z = []#measure of the alingment of the needle
        self.n = n#no of throws
        self.m = m#no of simulations
        self.pi_approx = []

    def samples(self):
        # throwing the needles
        for i in range(self.n):
            self.r.append(np.random.uniform(0,self.y))
            self.z.append(np.random.uniform(0,self.x/2.0))
        return [self.r,self.z]

    def simulation(self):
        self.samples()
        # m simulation
        for j in range(self.m):
            # n throw
            hits = 0 #setting the succes to 0
            for i in range(self.n):
                #condition for a hit
                if self.r[i]+self.z[i]>=self.y or self.r[i]-self.z[i] <= 0.0:
                    hits += 1
                else:
                    continue
            hits = 2*(self.x/self.y)*float(self.n/hits)
            self.pi_approx.append(hits)
        return self.pi_approx

y = Buffon_needle_problem(1,2,40000,5)

print (y.simulation())