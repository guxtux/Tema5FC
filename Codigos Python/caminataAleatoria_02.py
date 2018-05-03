# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal
"""


import turtle
from random import randint
from colorsys import hsv_to_rgb
from math import sqrt
import numpy as np
import matplotlib.pyplot as plt
 
paso = 30 
npasos = 500             
hinc = 1.0/npasos         
turtle.width(2)                
 
(w,h) = turtle.screensize()    
turtle.speed('fastest')
turtle.colormode(1.0)          
turtle.bgcolor('black')       

distancia = []
raizn = []

def caminata(pasitos):
    hue=0.0
    for i in range(npasos):
        turtle.setheading(randint(0,359))
        #   https://docs.python.org/2/library/colorsys.html
        turtle.color(hsv_to_rgb(hue, 1.0, 1.0))  
        hue += hinc                           
        turtle.forward(paso)
        distancia.append(sqrt(i)*paso)
        #raizn.append(sqrt(i))              
        (x,y) = turtle.pos()                  
        if abs(x) > w or abs(y) > h:
            turtle.backward(paso)                     
    turtle.done()
    return distancia

plt.figure(1)
plt.subplot(121)
plt.plot(caminata(300))
plt.plot(caminata(500))
plt.show()