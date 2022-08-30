# -*- coding: utf-8 -*-


#Punto 4.

import numpy as np
import matplotlib.pyplot as plt
import sys
sys.path.append("\.spyder-py3\Taller_2\Convolucion")
import Convolucion as s


h = 0.05
f = s.cero
M=np.array([-1,0,1])

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
    derdos.append(i/(4*(h**2)))
 
dfdos= np.array(derdos)


nuevo=np.insert(dfdos,0,np.zeros(M.size-2))
cero=np.insert(nuevo,nuevo.size,np.zeros(M.size-2))

x = np.linspace(-10,10,(len(s.x)-1))

plt.figure()
plt.grid()
plt.title("Segunda derivada por convolucion")
plt.plot(x,nuevo)
plt.show()