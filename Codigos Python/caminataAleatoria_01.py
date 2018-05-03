# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal
"""

from tkinter import *
import turtle
from random import randint
from colorsys import hsv_to_rgb

 
paso = 30 
npasos = 2000             
hinc = 1.0/npasos         
turtle.width(2)                
 
(w,h) = turtle.screensize()    
turtle.speed('fastest')
turtle.colormode(1.0)          
turtle.bgcolor('black')       
hue=0.0
for i in range(npasos):
    turtle.setheading(randint(0,359))
    #   https://docs.python.org/2/library/colorsys.html
    turtle.color(hsv_to_rgb(hue, 1.0, 1.0))  
    hue += hinc                           
    turtle.forward(paso)
    (x,y) = turtle.pos()                  
    if abs(x) > w or abs(y) > h:
        turtle.backward(paso)                     




ts = turtle.getscreen()
turtle.done()