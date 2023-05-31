# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 11:04:21 2023

@author: Administrator
"""

from math import pi
import numpy as np
import funa
import matplotlib.pyplot as plt

ts = 1 * 10 ** 3
detat = 1
t = [i/100 for i in range(0,ts,detat)]
Tfm = [i/100 for i in range(25,100,1)]     
v = 500*pi*25
Ai = pi*0.7**2
c = 0.85
rui = 0.8712
pri = 160
pgi0 = 100
rug0 = 0.85
pgiob = 150
Ty = 45
pgimm = np.zeros((len(Tfm),len(t)-1))
rumm = np.zeros((len(Tfm),len(t)-1))
qinmm = np.zeros((len(Tfm),len(t)-1))
qoutmm = np.zeros((len(Tfm),len(t)-1))
mim = np.zeros((len(Tfm),len(t)-1))
mom = np.zeros((len(Tfm),len(t)-1))
meank2 = []
nn = len(t)-1
for i in range(len(Tfm)):
    pgi = pgi0
    rug1 = rug0
    m1 = rug1 * v
    pgimm[i][0] = pgi
    rumm[i][0] = rug1
    Tf = Tfm[i]
    qinmm[i][0] = 0
    qoutmm[i][0] = 0
    for k in range(nn-1):
        qin = funa.qinfun(t[k],c,Ai,rui,pri,pgi,Tf)
        qout = funa.qoutfun(t[k]-Ty)
        qinmm[i][k+1] = qin
        qoutmm[i][k+1] = qout
        mig,mgr,m2 = funa.mupdatefun(m1,qin,rui,qout,rug1,detat)
        rug2 = m2/v
        rumm[i][k+1] = rug2
        pgi = pgi+funa.E(pgi)/rug1*(rug2-rug1)
        m1 = m2
        rug1 = rug2
        pgimm[i][k+1] = pgi
        mim[i][k] = mig
        mom[i][k] = mgr
    meank22 = abs(sum(abs(pgimm[i][:])-pgiob))/nn
    meank2.append(meank22)
b = min(meank2)
print(b)
Tf = Tfm[b]
plt.plot(t,pgimm[b][:])
        
    
    