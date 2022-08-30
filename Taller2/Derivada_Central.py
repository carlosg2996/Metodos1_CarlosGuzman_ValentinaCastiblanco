# -*- coding: utf-8 -*-


# Punto 2. Derivada central.

#Subpunto a.

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10,10,50)
h = 0.05

expo = lambda x: 1/np.sqrt(1+np.exp(-x**2))

f = expo(x)

def Derivada_Central(x,f,h):
    return (f(x+h)-f(x-h))/(2*h)

DCentral = Derivada_Central(x,expo,h)

print(DCentral)

fig = plt.figure(figsize=(7,3))
ax = fig.add_subplot(2,2,1)

ax1 = fig.add_subplot(2,2,2)

ax2 = fig.add_subplot(2,2,3)


ax.scatter(x,f)#funcion
ax1.scatter(x,DCentral)#la derivada de la funcion

#Subpunto b.

d = (x*np.exp(-x**2))/(1+(np.exp(-x**2))**3/2)#derivada de f

ax1.scatter(x,d, color="y")#derivada de f
ax2.scatter(x,np.abs(d-DCentral))#error



