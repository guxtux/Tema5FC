#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 16 20:44:15 2017

@author: gustavo
"""

import sys
import math
import random


def get_random(l, k):
    return random.random()*(l - 2*k) + k

def get_point(w, h, k):
    return (get_random(w, k), get_random(h, k))

def get_angle():
    return random.random()*2*math.pi

def intercept(p1, p2, h, k):
    for line in range(0, h+1, k):
        if (line >= p1[1] and line <= p2[1]) or \
           (line <= p1[1] and line >= p2[1]):
            return True

def drop_and_check(w, h, k):
    p1 = get_point(w, h, k)
    angle = get_angle()
    p2 = (p1[0] + (k/2.0)*math.cos(angle), 
          p1[1] + (k/2.0)*math.sin(angle))
    return intercept(p1, p2, h, k)

def repeat(times):
    w = h = 1000
    k = 10
    count = 0
    for i in range(times):
        if drop_and_check(w, h, k): count += 1
    return float(times)/count

if __name__ == "__main__":
    print(repeat(10000000))