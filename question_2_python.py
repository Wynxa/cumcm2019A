# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 11:22:02 2023

@author: Administrator
"""

from math import pi
import numpy as np
import funb
import matplotlib.pyplot as plt

hmax= 4.826000000000001
m=1
PT=20

m = int(input("请输入（1或2）："))
print(type(m))
if m == 1:
    sita00=pi
    hb00=0
    pb00=0.5    
    rub00=0.8046
    v0=25/4*pi*hmax+20
    kai00=0
elif m == 2:
    sita00=0
    hb00=hmax 
    pb00=160
    rub00=0.8711
    v0=20
    kai00=1



t = np.arange(0,10000+0.01,0.01)
vg=500*pi*25
Ai=pi*0.7**2
dert=t[1]-t[0]
Ty=t[1009]
c=0.85
ru0=0.8046
wa = np.arange(0.0280,0.0289,0.0001)#0.0282
Tf=91.5 #或者不用Tf，即采用mbgfun7

pgm = np.zeros((len(wa),len(t)))
Pbm = np.zeros((len(wa),len(t)))
mgm = np.zeros((len(wa),len(t)))
mbim = np.zeros((len(wa),len(t)))
mbm = np.zeros((len(wa),len(t)))
mbgm = np.zeros((len(wa),len(t)))
rubm = np.zeros((len(wa),len(t)))
mgrm = np.zeros((len(wa),len(t)))
hzm = np.zeros((len(wa),len(t)))
Imr = np.zeros((len(wa),len(t)))
hbm = np.zeros((len(wa),len(t)))
sitam = np.zeros((len(wa),len(t)))
Imr = []

for i in range(len(wa)):
    Pb0=pb00
    rub0=rub00 
    mb0=v0*rub0
    pgi0=100
    mg0=0.85*vg
    dti=0
    pgm[i][0]=100
    Pbm[i][0]=Pb0
    mbim[i][0]=0 
    mgr=0
    sita1=sita00 
    mgm[i][0]=mg0
    kai=kai00
    mbg=0
    mbm[i][0]=mb0
    hbm[i][0]=hb00
    mbgm[i][0]=0
    mgrm[i][0]=0
    hzm[i][0]=0
    rubm[i][0]=rub0
    hz1=0
    sitam[i][0]=sita00
    for k in range(len(t)-1):
        sita2=sita1+wa[i]*dert
        mi0,kai,hb,sita0,rub0,Pb0 = funb.rumiupdatefun11(sita2,hmax,ru0,kai,mb0,rub0,Pb0)
        sitam[i][k+1]=sita0
        sita1=sita2
        mbim[i][k+1]=mi0
        hbm[i][k+1]=hb
        mb1,rub1,pb1 = funb.rumiupdatefun21(mi0,mb0,mbg,hb,hmax,Pb0,rub0)
        mbg,dti = funb.mbgfun5(c,Ai,Pb0,pgi0,rub0,Tf,dert,dti)
        mb0=mb1
        mbm[i][k+1]=mb1
        Pb0=pb1
        rub0=rub1
        rubm[i][k+1]=rub1
        Pbm[i][k+1]=pb1    
        mbgm[i][k+1]=mbg
        mg1,rug,pg = funb.mrumigupdatefun(mbg,mg0,mgr,vg)
        pgi0=pg
        mg0=mg1
        pgm[i][k+1]=pg
        mgm[i][k+1]=mg1
        if t[k]>Ty:
            hz1,mgr = funb.penyoufun(t[k]-Ty,c,pg,rug,PT,dert); PT=20
        mgrm[i][k+1]=mgr  
        hzm[i][k+1]=hz1   
    Imr1 = np.mean(abs(pgm[i][:]-100))
    Imr.append(Imr1)

fd1 = min(Imr)
fd2 = Imr.index(fd1)
print(wa[fd2])

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

#plt.figure (1)
#plt.subplot(2,2,1)
#plot(t(1:10:size(sitam,2)),sitam(fd2(1),1:10:end))
plt.plot(t[:],mbim[fd2][:])
plt.xlabel('t')
plt.ylabel("加注质量") 
plt.title("栓塞腔燃油加注质量曲线") 
plt.grid
plt.show()

#plt.subplot(2,2,2)
plt.plot(t[:],Pbm[fd2][:])
plt.xlabel('t')
plt.ylabel("质量") 
plt.title ("栓塞腔压力曲线")
plt.grid
plt.show()

#plt.subplot(2,2,3)
plt.plot(t[:],mbm[fd2][:])
plt.xlabel('t')
plt.ylabel("质量") 
plt.title ("栓塞腔质量曲线")
plt.grid
plt.show()

#plt.subplot(2,2,4)
plt.plot(t[:],rubm[fd2][:])
plt.xlabel('t')
plt.ylabel("密度") 
plt.title ("栓塞腔燃油密度曲线")
plt.grid
plt.show()

#plt.figure(2)
#plt.subplot(3,1,1)
plt.plot(t[:],mbim[fd2][:])
plt.xlabel('t')
plt.ylabel("压力")
plt.title("‘高压管压力曲线") 
plt.grid
plt.show()

#splt.ubplot(3,1,2)
plt.plot(t[:],mbim[fd2][:])
plt.xlabel('t')
plt.ylabel("质量")
plt.title("‘高压管燃油质量曲线") 
plt.grid
plt.show()

plt.subplot(3,1,3)
plt.plot(t[:],mbim[fd2][:])
plt.xlabel('t')
plt.ylabel("质量")
plt.title("高压管受油质量曲线") 
plt.grid
plt.show()

#plt.figure(3)
#plt.subplot(2,1,1)
plt.plot(t[:],mbim[fd2][:])
plt.xlabel('t')
plt.ylabel("高程")
plt.title("‘针阀高程曲线") 
plt.grid
plt.show()

plt.subplot(2,1,2)
plt.plot(t[:],mbim[fd2][:])
plt.xlabel('t')
plt.ylabel("质量")
plt.title("‘喷嘴喷油质量曲线") 
plt.grid
plt.show()

        




        


