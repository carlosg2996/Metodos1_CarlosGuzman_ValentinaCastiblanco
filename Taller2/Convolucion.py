# -*- coding: utf-8 -*-


import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10,10,50)
h = 0.05
M=np.array([-1,0,1])

expo = lambda x: 1/np.sqrt(1+np.exp(-x**2))

f = expo(x)


i=0
msum = []
while i <= len(f):
    b = i+1
    c = i+2
    
    if b < len(f) and c < len(f):
        con=(f[i]*M[0])+(f[b]*M[1])+(f[c]*M[2])
        msum.append(con)
    i=b 
    
msum = np.array(msum)


der =[]
for i in msum:
    der.append(i/(2*h))
     
df= np.array(der)



cero=np.insert(df,0,np.zeros(M.size-2))
cero=np.insert(cero,cero.size,np.zeros(M.size-2))


plt.figure()
plt.grid()
plt.title("Derivada por convolucion")
plt.plot(x,cero)
plt.show()


