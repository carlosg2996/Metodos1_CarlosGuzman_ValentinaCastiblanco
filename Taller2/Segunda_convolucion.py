# -*- coding: utf-8 -*-


#Punto 4.

import numpy as np
import matplotlib.pyplot as plt



x = np.linspace(-10,10,50)
h = 0.05
M=np.array([1,-2,1])

expo = lambda x: 1/np.sqrt(1+np.exp(-x**2))

f = expo(x)

i=0
msum = []
while i <= len(f):
    b = i+1
    c = i+2
    
    if b < len(f) and c < len(f):
        condos=(f[i]*M[0])+(f[b]*M[1])+(f[c]*M[2])
        msum.append(condos)
    i=b 
    
msum = np.array(msum)


derdos =[]
for i in msum:
    derdos.append(i/((h**2)))
 
dfdos= np.array(derdos)


nuevo=np.insert(dfdos,0,np.zeros(M.size-2))
cero=np.insert(nuevo,nuevo.size,np.zeros(M.size-2))

x = np.linspace(-10,10,(len(x)-1))

plt.figure()
plt.grid()
plt.title("Segunda derivada por convolucion")
plt.plot(x,nuevo)
plt.show()