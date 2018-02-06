#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 19:11:47 2018

@author: andrewmccallister
"""

import numpy as np
import scipy
import matplotlib.pyplot as plt

#def TenDQuad(x1,x2,x3,x4,x5,x6,x7,x8,x9,x10):
def NDQuad(x):
    #return (x[1]+x[2]+x[3]+x[4]+x[5]+x[6]+x[7]+x[8]+x[9]+x[10])**2
    return (np.sum(x,1)**2)
limits=np.array([[0,1],[0,1],[0,1],[0,1],[0,1],[0,1],[0,1],[0,1],[0,1],[0,1]])

def NDMC_int(func,limits,D,N):
    rand_vars=np.random.rand(N,D)*(limits[:,1]-limits[:,0])+limits[:,0]
    out=np.mean(func(rand_vars))*np.product((limits[:,1]-limits[:,0]))
    return out

def plot_NDMC_int(func,limits,D,n):
    x=2**np.arange(1,n)
    IntND=np.array([NDMC_int(func,limits,D,x[i]) for i in range(n-1)])
    ErrorND=np.absolute((IntND-(155/6))/(155/6))
    plt.plot(1/np.sqrt(x),ErrorND)

plot_NDMC_int(NDQuad,limits,10,17)