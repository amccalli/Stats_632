#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 13:09:19 2018

@author: andrewmccallister
"""

import numpy as np
import scipy
import matplotlib.pyplot as plt


def trap_int(f,a,b,n):
    h=(b-a)/(n-1)
    I=(h/2)*(f(a)+f(b))+h*sum([f(a+(i-1)*h) for i in range(2,n-1)])
    return I

def Romberg (f,a,b,n,conv):
    R=np.zeros([n+1,n+1])
    R[1,1]=(b-a)*(f(a)+f(b))/2
    for J in range(2,n+1):
        R[J,1]=trap_int(f,a,b,(2**(J-1)+1))
        for k in range (2,J+1):
            R[J,k] = (4**(k-1) * R[J,k-1] - R[J-1,k-1]) / (4**(k-1) - 1)
            #print(R[J,k])
            if np.absolute(R[J,k]-R[J-1,k-1])<conv and np.absolute(R[J,k])>conv:
                print('converged R[{},{}]={}'.format( J,k,R[J,k]))
            else:
                print('not converged R[{},{}]={}'.format( J,k,R[J,k]))
            
    return R
                
           
            
    
def sinsq(x):
    return np.sin(x)**2

def emx(x):
    return np.exp(-x)
            
R=Romberg(sinsq,0,4*np.pi,11,1e-5)
Error=(R-(2*np.pi))/(2*np.pi)

R2=Romberg(sinsq,0,4*np.pi,15,1e-6)
Error2=(R2-(2*np.pi))/(2*np.pi)