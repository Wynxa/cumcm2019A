# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 10:24:27 2023

@author: Administrator
"""

#求解器
import eluer as el 
func1,func2 = input('请输入模型：\n').split(',')
fun1 = eval(func1)
fun2 = eval(func2)
x0,y0,x01,y01 = map(float,input('请输入初值x0,y0，用逗号隔开：\n').split(','))
rangee,h = map(float,input('请输入范围以及步长，用逗号隔开：\n').split(','))
while(True):
    ode = int(input('请选择求解器：\n 1、显式欧拉法\n 2、隐式欧拉法\n 3、改进欧拉法\n 4、四阶龙格——库塔法\n 5、输入0结束求解\n'))
    if ode == 1:
        el. eluer_explicit(rangee,h,fun1,x0,y0)
        el. eluer_explicit(rangee,h,fun2,x01,y01)
    elif ode == 2:
        el.eluer_implicit(rangee, h, fun1, x0, y0)
        el.eluer_implicit(rangee, h, fun2, x01, y01)
    elif ode == 3:
        el.eluer_improvement(rangee, h, fun1, x0, y0)
        el.eluer_improvement(rangee, h, fun2, x01, y01)lambda x1,y:x1,lambda x1,x2,t:-t*x1*3*math.sin(2*t)
    elif ode == 4:
        el.order_4_runge_kutta(rangee, h, fun1, x0, y0)
        el.order_4_runge_kutta(rangee, h, fun2, x01, y01)
    elif ode == 0:
        break
    else:
        print("输入错误请重新输入")
    


