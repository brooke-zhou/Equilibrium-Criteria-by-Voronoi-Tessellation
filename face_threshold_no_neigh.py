#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 26 22:19:58 2018

Plot cutoff - CN
using a series of dump.voro files (dump.fc_x.x.voro')

@author: Yacong
"""
import numpy as np
import matplotlib.pyplot as plt

test_range = 2
scan_range = 11
increment = 0.1
elements = ['Na','Mg','Ca','Al','Si','O']

for file in range(scan_range):
    filename = 'dump.fc_'+"{:.1f}".format(file*increment)+'.voro'
    with open(filename,'r') as lammps_voro:
        cn = {'1':0,'2':0,'3':0,'4':0,'5':0,'6':0}
        n = {'1':0,'2':0,'3':0,'4':0,'5':0,'6':0}
        for lc,lines in enumerate(lammps_voro):
            if lc >= 9:
                atom_type = lines.split()[1]
                nface = lines.split()[-1]
                cn[atom_type] = cn[atom_type] + int(nface)
                n[atom_type] = n[atom_type] + 1
        file_summary = np.asarray([file*increment])
        for atom_type in range(1,7):
            cn[str(atom_type)] = cn[str(atom_type)] / n[str(atom_type)]
            file_summary = np.append(file_summary,[cn[str(atom_type)]])
        print(cn)
        if file == 0:
            summary = np.expand_dims(file_summary,axis=0)
        else:
            summary = np.append(summary,np.expand_dims(file_summary,axis=0),axis=0)
        
print(summary)
for i in range(1,7):
    element = elements[i-1]
    plt.figure(element)
    plt.xlabel('face area cutoff / Ang^2')
    plt.ylabel('average coordination number')
    plt.title(element+'-cutoff')
    plt.plot(summary[:,0],summary[:,i],'ro-')
    plt.show() 