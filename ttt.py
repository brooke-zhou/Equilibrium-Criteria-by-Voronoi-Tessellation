#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  4 13:09:05 2018

@author: Yacong
"""
import numpy as np
q_t=[[],[],[],[],[],[]]
for timestep in range(1,4):
    q_by_type=np.asarray([[1., 0., 0., 0.],
            [2.*timestep, 0.1*timestep, 100.*timestep, 10.*timestep],
            [3.*timestep, 0.2*timestep, 200.*timestep, 20.*timestep],
            [4.*timestep, 0.3*timestep, 300.*timestep, 30.*timestep],
            [5.*timestep, 0.4*timestep, 400.*timestep, 40.*timestep],
            [6.*timestep, 0.5*timestep, 500.*timestep, 50.*timestep]])
    for element_type in range(1,7):
        if q_by_type[element_type-1][-1] != 0:
            new_entry = np.append(np.asarray([timestep]),q_by_type[element_type-1][1:])
            if len(q_t[element_type-1])==0:
                q_t[element_type-1] = np.asarray([new_entry])
            else:
                q_t[element_type-1] = np.append(q_t[element_type-1],np.asarray([new_entry]),axis=0)
                