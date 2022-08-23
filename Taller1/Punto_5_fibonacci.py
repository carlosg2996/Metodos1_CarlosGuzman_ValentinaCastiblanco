# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# 5. Sucesion de fibonnacci

# Subpunto 1.
import pandas as pd
i = []
for n in range(0,21):
    if n == 0:
        i.append(n)
    elif n == 1:
        i.append(n)
    else:
        a = i[n-1]
        b = i[n-2]
        r =i.append((int(a)+int(b)))
    fib = pd.Series(i, name="serie fibonacci")    
print(fib)


#Subpunto 2.

import matplotlib.pyplot as plt

fib.plot(color='k')
plt.title("serie fibonacci")
plt.show()

#Subpunto 3.

n=1
suar = []
while n < len(i):
    p = n+1
    if n == 0:
        n = p
    elif p < len(i):
        au = i[p]/i[n]
        suar.append(au)
    n = p
    naur = pd.Series(suar, name="aproximacion numero aureo")
print(naur)

naur.plot(color="b")
plt.title("aproximacion numero aureo")
plt.show()



        
        

    
