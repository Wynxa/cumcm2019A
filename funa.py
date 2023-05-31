# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 10:34:24 2023

@author: Administrator
"""
import math
from math import pi
import numpy as np


def qinfun(t,c,Ai,rui,pri,pgi,Tf):
    dti = t-math.floor(t/(Tf+10)) * (Tf+10)
    if dti<Tf:
        qin = c*Ai*np.sqrt(2*(pri-pgi)/rui)
    elif dti>=Tf:
        qin = 0
    return qin

def qoutfun(t):
    dto = t-math.floor(t/100)*100
    if dto<0.2 and dto>=0:
        qout = 100 * dto
    elif dto>0.2 and dto<2.2:
        qout = 20
    elif dto>2.2 and dto<2.4:
        qout = -100*dto+240
    elif dto>=2.1 and dto<100:
        qout = 0
    return qout

def mupdatefun(m1,qin,rub,qout,rug,detat):
    mig = qin*rub*detat
    mgr = qout*rug*detat
    m2 = m1+mig-mgr
    return mig,mgr,m2

def E(p):
    E = 0.0001*p**3-0.001082*p**2+5.474*p+1532
    return E



   
