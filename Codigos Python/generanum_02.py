#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""


"""

import random

x = []

muestra = 500

random.seed()

valoresRandomX = []
valoresRandomY = []


for i in range(muestra):
    nuevoValor = random.random()
    valoresRandomX.append(nuevoValor)

for i in range(muestra):
    nuevoValor = random.random()
    valoresRandomY.append(nuevoValor)

random.seed(500)
valoresRandomX2 = []
valoresRandomY2 = []

for i in range(muestra):
    nuevoValor = random.random()
    valoresRandomX2.append(nuevoValor)

for i in range(muestra):
    nuevoValor = random.random()
    valoresRandomY2.append(nuevoValor)


x = valoresRandomX
y = valoresRandomY

x2 = valoresRandomX2
y2 = valoresRandomY2
