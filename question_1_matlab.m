ts=10000;detat=0.01 ;
t=0:detat:ts; 
Tfm=0.25:0.01:1;
v=500*pi*25;Ai=pi*0.7^2;
c=0.85;rui= 0.8712;
pri=160;pgi0=100;rug0=0.85;
pgiob=150;Ty=45;

[Im,Iv]=min(meank2)
Tf=Tfm(Iv),%0.29
figure (1)
subplot(2,1,1)
plot(t((1:end)),pgimm(Iv,1:end))
axis([0 ts 0 200])
xlabel ‘t’
ylabel ‘压力’
title ‘高压油管压力曲线’
grid on
subplot(2,1,2) 
plot(t(1:end),rumm(Iv,1:end))
xlabel ‘t’
ylabel ‘密度’
title ‘高压油管燃油密度曲线’
grid on
figure(2)
subplot(2,1,1)
plot(t(1:end),qinmm(Iv,1:end))
xlabel ‘t’
ylabel ‘进油量’
title ‘进油量变化曲线’
grid on
subplot(2,1,2)
plot(t(1:end),qoutmm(Iv,1:end))
xlabel ‘t’
ylabel ‘出油量’
title ‘高压管出油量变化曲线’
grid on

for i=1:length(Tfm)
    pgi=pgi0;rug1=rug0;
    m1=rug1*v; pgimm(i,1)=pgi;rumm(i,1)=rug1;
    Tf=Tfm(i);qinmm(i,1)=0;qoutmm(i,1)=0;
    for k=1:length(t)-1
        qin=qinfun(t(k),c,Ai,rui,pri,pgi,Tf);
        qout=qoutfun(t(k)-Ty);
        qinmm(i,k+1)=qin; qoutmm(i,k+1)=qout;      [mig,mgr,m2]=mupdatefun(m1,qin,rui,qout,rug1,detat);
        rug2=m2/v;rumm(i,k+1)=rug2;
        pgi=pgi+E(pgi)/rug1*(rug2-rug1);
        m1=m2; rug1=rug2; pgimm(i,k+1)=pgi;
        mim(i,k)=mig;mom(i,k)=mgr;
    end
%稳定到100MPA
%meank2(i)=sum(abs(pgimm(i,:)-pgiob))/size(pgimm,2);
%调整 150Mpa     
meank2(i)=abs(sum(mim(i,:))-sum(mom(i,:))-706.57632);
%压力从100升到150时需要增加的燃油质量
end


function qin=qinfun(t,c,Ai,rui,pri,pgi,Tf)
%t时刻rui高压侧密度；pri泵腔压力；
%pgi?高压管压力?。
dti=t-floor(t/(Tf+10))*(Tf+10);
if dti<Tf 
qin=c*Ai*sqrt(2*(pri-pgi)/rui);
elseif dti>=Tf
qin=0;
end
end
function qout=qoutfun(t)
 %t时刻喷油嘴喷油量
dto=t-floor(t/100)*100;
if dto<0.2&&dto>=0
qout=100*dto;
elseif dto>=0.2&&dto<2.2;
 qout=20;
elseif dto>=2.2&&dto<2.4
 qout=(-100*dto+240);
elseif dto>=2.4&&dto<100
 qout=0;   
end
end
function [mig,mgr,m2]=mupdatefun(m1,qin,rub,qout,rug,detat)
mig=qin*rub*detat;mgr=qout*rug*detat;
m2=m1+(mig-mgr);
end
function Efal=E(x)
%Efal= 3.454e-07 *x^4+(-3.813e-05) *x^3+0.01667*x^2 + 4.688* x +  1540 ;
Efal= 0.0001 *x^3-0.001082*x^2 + 5.474* x +  1532 ;
end
