#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Split a single lammps dump file into differnt timesteps

Created on Thu Mar 29 15:23:34 2018

@author: Yacong
"""
#dump_file = 'dump.neighbors'
#output_name_head = 'dump.neighbors.'

import glob,os

dump_file = 'dump.fc_0.voro'
output_name_head = 'dump.fc_0.'
# folder_of_splitted_files = '10GPa_0-0.05_threshold_0.1_'
folder_of_splitted_files = '25GPa_1.05-2.05_threshold_0.1_'

n_frame = 0
found_new_frame = False

with open(dump_file,'r') as neighbor_raw:
    if os.path.isdir('./'+folder_of_splitted_files):
        os.chdir('./'+folder_of_splitted_files)
    else:
        os.makedirs('./'+folder_of_splitted_files)
        os.chdir('./'+folder_of_splitted_files)
    for lc,lines in enumerate(neighbor_raw):
        if lines == 'ITEM: TIMESTEP\n':
            n_frame += 1
            found_new_frame = True
            if('output_file' in vars()):  
                output_file.close()
        elif found_new_frame:
            output_file_name = output_name_head+lines.split()[0]
            found_new_frame = False
            output_file = open(output_file_name,'w')
            output_file.write('ITEM: TIMESTEP\n')
            output_file.write(lines)
        else:
            output_file.write(lines)
output_file.close()
# os.rename('../'+dump_file,'../'+dump_file)
os.rename('../'+dump_file,'./'+dump_file)