#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 28 18:10:40 2018

@author: andrewmccallister
"""

import numpy as np
import scipy as sc
import matplotlib.pyplot as plt

def Poisson (n,N,P):
    return(P*N)**n/(sc.misc.factorial(n))*np.exp(-P*N)
    
def Binomial (n,N,P):
    return (sc.misc.factorial(N)/(sc.misc.factorial((N-n))*sc.misc.factorial(n)))*(P**n)*((1-P)**(N-n))

def Gaussian (n,mean,var):
    return np.exp(-(n-mean)**2/(2*var))/(np.sqrt(2*np.pi*var))

x=np.arange(0,20,0.25)
N=4
P=0.35
y1=Poisson(x,N,P)
y1g=Gaussian(x,(N*P),(N*P*(1-P)))

N=40
P=0.35
y2=Poisson(x,N,P)
y2g=Gaussian(x,(N*P),(N*P*(1-P)))

N=4
P=0.35
y3=Binomial(x,4,0.35)
y3g=Gaussian(x,(N*P),(N*P))

N=40
P=0.35
y4=Binomial(x,40,0.35)
y4g=Gaussian(x,(N*P),(N*P))

plt.figure(1)
plt.subplot(211)
plt.plot(x,y1,x,y1g)
plt.subplot(212)
plt.plot(x,y2,x,y2g)
plt.figure(2)
plt.subplot(211)
plt.plot(x,y3,x,y3g)
plt.subplot(212)
plt.plot(x,y4,x,y4g)


