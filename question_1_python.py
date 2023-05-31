
"""
Created on Wed Mar 29 11:04:21 2023

@author: Administrator
"""

from math import pi
import numpy as np
import funa
import matplotlib.pyplot as plt

ts = 2 * 10 ** 3+0.01

detat = 0.01
#t = [i/100 for i in range(0,ts,detat)]
t = np.arange(0,ts,detat)
Tfm = [i/100 for i in range(25,100,1)]     
v = 500*pi*25
Ai = pi*0.7**2
c = 0.85
rui = 0.8712
pri = 160
pgi0 = 100
rug0 = 0.85
pgiob = 100
Ty = 40
pgimm = np.zeros((len(Tfm),len(t)))
rumm = np.zeros((len(Tfm),len(t)))
qinmm = np.zeros((len(Tfm),len(t)))
qoutmm = np.zeros((len(Tfm),len(t)))
mim = np.zeros((len(Tfm),len(t)))
mom = np.zeros((len(Tfm),len(t)))
meank2 = []
nn = len(t)
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
    #meank22 = abs(sum(abs(pgimm[i][:])-pgiob))/np.size(pgimm,1)
    meank22 = abs(sum(mim[i][:])-sum(mom[i][:])-706.57632)
    meank2.append(meank22)
b = min(meank2)
a = meank2.index(min(meank2))
print(b,a)
print("Tf = ",Tfm[a])

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
plt.figure(1)
plt.subplot(2,1,1)
plt.plot(t[:],pgimm[a][:])
plt.axis([0,ts,0,200])
plt.xlabel('t')
plt.ylabel('压力')
plt.title('高压油管压力曲线')
plt.grid

plt.subplot(2,1,2)
plt.plot(t[:],rumm[a][:])
plt.xlabel('t')
plt.ylabel('密度')
plt.title('高压油管燃油密度曲线')
plt.grid
plt.show()

plt.figure(2)
plt.subplot(2,1,1)
plt.plot(t[:],qinmm[a][:])
plt.xlabel('t')
plt.ylabel('进油量')
plt.title('进油量变化曲线')
plt.grid

plt.subplot(2,1,2)
plt.plot(t[:],qoutmm[a][:])
plt.xlabel('t')
plt.ylabel('出油量')
plt.title('出油量变化曲线')
plt.grid
plt.show()
    
    