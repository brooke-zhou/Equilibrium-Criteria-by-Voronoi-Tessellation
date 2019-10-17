#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Split a single lammps dump file into differnt timesteps

Created on Tue May 15 16:44:44 2018

@author: Yacong
"""
#dump_file = 'dump.neighbors'
#output_name_head = 'dump.neighbors.'

import glob,os

def split_traj_dump(dump_file):
    job_name = dump_file[5:-5]
    output_name_head = 'dump.'
    folder_of_splitted_files = job_name

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
    os.chdir('..')
    