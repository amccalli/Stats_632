#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 28 13:17:30 2018

@author: andrewmccallister
"""

import numpy as np
import matplotlib.pyplot as plt


N=5
Runs=100000
Success=np.zeros(Runs)
N_Successes=np.zeros(Runs)
for x in range(Runs) :
    flip=0;
    for y in range(N*5) :
        Coins=np.random.randint(0,2,N)
        flip=flip+1
        if (np.sum(Coins)==(N-1) or np.sum(Coins)==1) :
            Success[x]=flip
            #print(Coins)
            break
    counter=0;
#    for z in range(x) :
#        Coins=np.random.randint(0,2,N)
#        if (np.sum(Coins)==(N-1) or np.sum(Coins)==1) :
#            counter=counter+1
#    N_Successes[x]=counter               
average=np.average(Success)
#plt.plot(N_Successes)

N2=5
B=0.9
Runs2=100000
Success2=np.zeros(Runs)
for x in range(Runs) :
    flip=0;
    for y in range(N*5) :
        Coins=np.random.randint(0,2,N-1)
        l=np.random.random(1)
        if (l<B) :
            l=0
        else :
            l=1
        Coins=np.append(Coins,l)
        flip=flip+1
        if (np.sum(Coins)==(N-1) or np.sum(Coins)==1) :
            Success2[x]=flip
            #print(Coins)
            break
average_skewed=np.average(Success2)
