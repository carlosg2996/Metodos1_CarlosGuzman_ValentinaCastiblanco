# -*- coding: utf-8 -*-
"""
Created on Fri Aug 19 23:49:03 2022

@author: CRISANTA
"""

# Punto 5.2 espiral de Arquimedes

#Subpunto a.
import math as mt
import pandas as pd
a = 0
b = 1
e = []
i = 0

while i<= (2*(mt.pi)):
      r = (a+(b*i))
      e.append(r)
      i += (2*mt.pi/45)
pr = pd.Series(e, name="posiciones r") 
#print(pr)

#Subpunto b.
y=[]
x=[]
for i in e:
    cy = i*mt.sin(2*i)
    cx = i*mt.cos(2*i)
    y.append(cy)
    x.append(cx)
co = pd.Series(x,y, name="cambio de coordenadas")
print(co)

#Subpunto c.

import matplotlib.pyplot as plt
coordenadas = {'x': x, 'y':y}

coordenadas = pd.DataFrame(coordenadas)
coordenadas.plot(x="x", y="y", title="Espiral de arquimedes")
plt.show()

#print(coordenadas)

    
    