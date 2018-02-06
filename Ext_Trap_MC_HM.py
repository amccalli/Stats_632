#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 15:04:31 2018

@author: andrewmccallister
"""

import numpy as np
import scipy
import matplotlib.pyplot as plt

def emx(x):
    return np.exp(-x)

def trap_int(f,a,b,n):
    h=(b-a)/(n-1)
    I=(h/2)*(f(a)+f(b))+h*sum([f(a+(i-1)*h) for i in range(2,n-1)])
    return I

def Romberg2 (f,a,b,n,Min):
    R=np.zeros([n+1,n+1])
    h=[(b-a)/2**(x) for x in range(n)]
    R[1,1]=(b-a)*(f(a)+f(b))/2
    for J in range(2,n+1):
        R[J,1]=R[J-1,1]/2+h[(J-1)]*sum([f(a + (2 * j - 1) * h[(J-1)]) for j in range(1,2**(J-1))])
        for k in range (2,J+1):
            R[J,k] = (4**(k-1) * R[J,k-1] - R[J-1,k-1]) / (4**(k-1) - 1)
            #print(R[J,k])
            if np.absolute(R[J,k]-R[J-1,k-1])<Min and np.absolute(R[J,k])>Min:
                print('converged R[{},{}]={}'.format( J,k,R[J,k]))
                return [R,J,k]
                exit
                
def hit_miss(func,a,b,N):
    hits=0
    x=np.random.random(N)*(b-a)+a
    y=np.random.random(N)*np.max(func(x))
    hits=np.sum(np.array([y < func(x)]).astype(int))
    return (hits/N)*(b-a)*np.max(func(x))

def plot_trapint(func,a,b,n):
    x=2**np.arange(1,n)
    h=(b-a)/(x-1)
    IntT=np.array([trap_int(func,a,b,x[i]) for i in range(n-1)])
    ErrorT=np.absolute([((IntT[j]-((np.e-1)/np.e))/((np.e-1)/np.e)) for j in range(n-1)])
    plt.figure(2)
    plt.plot(np.log(x),np.log(ErrorT))
    return [IntT,ErrorT,h]

def plot_rombint(func,a,b,n,Min):
    [IntR,J,K]=Romberg2(func,a,b,n,Min)
    ErrorR=np.absolute((IntR-((np.e-1)/np.e)/((np.e-1)/np.e)))
    ErrorR2=np.absolute([((IntR[j,j]-((np.e-1)/np.e))/((np.e-1)/np.e)) for j in range(1,J-1)])
    x=2**np.arange(1,J-1)
    h=(b-a)/(x-1)
    plt.figure(3)
    plt.plot(np.log(x),np.log(ErrorR2))
    return [IntR,ErrorR,h]

def plot_mc_hm(func,a,b,n):
    x=2**np.arange(4,n+4)
    IntH=np.array([hit_miss(func,a,b,x[i])for i in range(n)])
    ErrorH=np.absolute([((IntH[j]-((np.e-1)/np.e))/((np.e-1)/np.e)) for j in range(n)])
    plt.figure(4)
    plt.plot(np.log(x),np.log(ErrorH))
    return [IntH,ErrorH,x]
    
x=np.arange(0,10,0.05)
plt.figure(1)
plt.plot(x,emx(x))
[IntT,ErrorT,hT]=plot_trapint(emx,0,1,10)
[IntR,ErrorR,hR]=plot_rombint(emx,0,1,100,1e-5)
[IntH,ErrorH,nH]=plot_mc_hm(emx,0,1,10)