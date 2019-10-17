#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 17 01:54:48 2018

@author: Yacong
"""

import numpy as np
import matplotlib.pyplot as plt

path_to_edist = './25GPa_fc_0/edist_full/edist.txt'
average_range = 19
t_edist = np.loadtxt(path_to_edist)

smooth_edist=[]
for i in range(average_range,len(t_edist)-average_range):
    smooth_edist.append(np.mean(\
        t_edist[i-average_range:i+average_range,1]) )

# plot edist-time
edist_t_fig = plt.figure('smooth_edist')
plt.xlabel('t/fs')
plt.ylabel('Euclidean Distance to Reference Distribution (Smoothed)')
plt.title('Smoothed 2NN - time')
plt.plot(t_edist[average_range:-average_range,0],smooth_edist[:],'b-',\
                marker='o',markersize=5)
plt.grid()
# plt.savefig('../'+name_of_plot)
plt.show()