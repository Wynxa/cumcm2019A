import math
from math import pi

def hbfun(sita,hmax):
    sita=min(max(sita-math.floor(sita/(2*pi))*2*pi,0),2*pi)
    sita=sita-pi
    hb=min(max(2.438*math.sin(0.06542*sita+1.365)+2.387*math.sin(1.004*sita-1.584),0),hmax)
    return hb,sita

def rumiupdatefun11(sita,hmax,ru0,kai,mb0,rub0,pb0):
    hb,sita = hbfun(sita,hmax)
    if hb<0.001 and kai==1:
        v0 = mb0/ru0
        v = max(25/4*pi*(hmax-hb),0)+20-v0    
        m = ru0*v
        rru = (m+mb0)/(max(25/4*pi*(hmax-hb),0)+20)
        pb=E(0.5)/0.8049*(rru-0.8049)+0.5;kai=0
    elif hb>=0.001:
        kai=1;m=0
        rru=rub0
        pb=pb0
    else:
        m=0
        rru=rub0
        pb=pb0
    return m,kai,hb,sita,rru,pb

def E(x):
    #Efal= 3.454e-07 *x^4+(-3.813e-05) *x^3+0.01667*x^2 + 4.688* x +  1540 
    Efal= 0.0001 *x**3-0.001082*x**2 + 5.474* x +  1532 
    return Efal

def rumiupdatefun21(m11,m0,mbg,hb,hmax,pb0,rub0):
    m1=m0+m11-mbg
    v=max(25/4*pi*(hmax-hb),0)+20
    rub=m1/v
    pb=E(pb0)/rub0*(rub-rub0)+pb0
    return m1,rub,pb

def mbgfun2(c,Ai,Pb1,pgi,rub,Tf,dert,dti):
    if Pb1>pgi and dti<Tf :
        Q=c*Ai*math.sqrt(2*(Pb1-pgi)/rub)
        dti=dti+dert
    elif Pb1>pgi and dti>=Tf and dti<Tf+10 :
        dti=dti+dert
        Q=0
    else:
        dti=0
        Q=0
    mout=rub*Q*dert
    return mout,dti

def mbgfun5(c,Ai,Pb1,pgi,rub,Tf,dert,dti):
    if Pb1>pgi and dti<Tf : 
        Q=c*Ai*math.sqrt(2*(Pb1-pgi)/rub)
        dti=dti+dert
    elif dti>0 and dti<Tf+10 :
        dti=dti+dert
        if dti>=Tf+10:
            dti=0
        Q=0
    else:
        dti=0
        Q=0
    mout=rub*Q*dert
    return mout,dti

def mbgfun7(c,Ai,Pb1,pgi,rub, dert):
    if Pb1>pgi:    
        Q=c*Ai*math.sqrt(2*(Pb1-pgi)/rub)
    else:
        Q=0
    mout=rub*Q*dert
    return mout

def mrumigupdatefun(mbg,mg0,mgr,v):
    m1=mg0+mbg-mgr
    rug=m1/v
    pg=E(100)/0.85*(rug-0.85)+100
    # pg=E(pg0)/rug0*(rug-rug0)+pg0
    return m1,rug,pg

def penyoufun(t,c,pgi,rug,PT,dert):
    hz1=hzfun(t)
    L2=1.25+math.tan(9*pi/180)*hz1
    Ac21=max(min(pi*0.7**2,pi*((L2)**2-1.25**2)),0)
    if pgi<PT:
        Qc21=0
        print("初始化失败")
    else:
        Qc21=c*Ac21*math.sqrt(2*(pgi-PT)/rug)
        # max(c*Ac21*sqrt(2*(pgi-PT)/rug),0);
    mgr=rug*Qc21*dert
    return hz1,mgr

def hzfun(t):
    t=min(max(t-math.floor(t/100)*100,0),100)
    if t>=0 and t<0.45:
        hz1=min(max(-298.7*t**4+249.3*t**3-48.61*t**2+3.245*t-0.04327,0),2)
    elif t>=0.45 and t<=2:
        hz1=2;   
    elif t>2 and t<2.46:
        hz1=min(max(-280*t**4+2509*t**3-8402*t**2+12460*t-6897,0),2)
    elif t>=2.46 and t<=100:
        hz1=0
    return hz1

















