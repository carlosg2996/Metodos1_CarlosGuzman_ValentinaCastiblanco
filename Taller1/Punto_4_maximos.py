# -*- coding: utf-8 -*-
"""
Created on Sat Aug 20 10:53:54 2022

@author: CRISANTA
"""

# Punto 4. Maximos locales

import pandas as pd

serie = pd.read_fwf("EstrellaEspectro.txt", header=None)

x = serie[0].copy()
y = serie[1].copy()

#print(len(y))

mlx =[]
mly =[]

i = 1
while i < (len(y)):
    a = (i-1)
    b = (i+1)
    if a < len(y) and b < len(y):
        if y[a] < y[i] and y[b] < y[i]:
           py= i
           my=y[i]
           mly.append(my)
           mx=x[py]
           mlx.append(mx)
    i=b
ml=pd.Series(mlx,mly, name="coordenadas maximos locales")
print(ml)

import matplotlib.pyplot as plt
coordenadas = {'x': x, 'y':y}
coordenadas = pd.DataFrame(coordenadas)
coordenadas.plot(x="x", y="y", title="")
plt.scatter(mlx, mly, color= 'r')
plt.show()

    



        
    

