#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 23:02:35 2018

@author: fatm400
"""

import pandas as pd
import numpy as np

def media_movil(mylist, longitud):
    cumsum, moving_aves = [0], []
    
    for i, x in enumerate(mylist, 1):
        cumsum.append(cumsum[i-1] + x)
        if i>=N:
            moving_ave = (cumsum[i] - cumsum[i-N])/N
            #can do stuff with moving_ave here
            moving_aves.append(moving_ave)
    return moving_aves

mylist = [1., 2., 3., 4., 5., 6., 7.]
N = 3

a = np.asarray(mylist)

pd.rolling_mean(a, N)[N-1:]

x = media_movil(mylist, N)