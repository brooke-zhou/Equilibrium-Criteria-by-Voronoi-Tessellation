#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  6 12:55:42 2018

@author: Yacong
"""

import glob,os
import numpy as np
import matplotlib.pyplot as plt
import math

type_lookup_file = 'id-type.tab'
dump_file_head = 'dump.fc_0.'
path_to_splitted_dump = './25GPa_threshold_0_ref/'
bin_width = 0.1
# plot_axis_lim[Element] = [x_lo_hist, x_hi_hist, y_lo_hist, y_hi_hist,x_lo_cn, x_hi_cn,  y_lo_cn, y_hi_cn]
plot_axis_lim = {'Mg':[-0.5, 12, 0, 3200, 0, 12, 0, 10],
                 'Ca':[-0.5, 12, 0, 5760, 0, 12, 0, 10],
                 'Al':[-0.5, 10, 0, 3200, 0, 8, 0, 6],
                 'Si':[-0.5, 10, 0, 10000, 0, 5, 0, 8],}

atom_count = {1:0,\
              2:64,\
              3:100,\
              4:72,\
              5:200,\
              6:672}

# create type_table (id-type)
type_table = {0:0}
with open(type_lookup_file,'r') as type_lookup:
    for lc,lines in enumerate(type_lookup):
        if lc > 0:
            type_table[int(lines.split()[0])] = int(lines.split()[1])

os.chdir(path_to_splitted_dump)

# do statistics and make plots
dump_file_list = glob.glob(dump_file_head+'*')
if len(dump_file_list) == 1:
    print('Found only 1 dump file!')
    dump_file = dump_file_list[0]
    with open(dump_file,'r') as neighbor_raw:
        # read face area array into memory
        face_stat_mg = np.asarray([])
        face_stat_ca = np.asarray([])
        face_stat_al = np.asarray([])
        face_stat_si = np.asarray([])
        for lc,lines in enumerate(neighbor_raw):
            if lc > 9:
                center_atom = type_table[int(lines.split()[1])]
                coord_atom = type_table[int(lines.split()[2])]
                face_area = float(lines.split()[3])
                if coord_atom == 6:
                    if center_atom == 2:
                        face_stat_mg = np.append(face_stat_mg,[face_area])
                    elif center_atom == 3:
                        face_stat_ca = np.append(face_stat_ca,[face_area])
                    elif center_atom == 4:
                        face_stat_al = np.append(face_stat_al,[face_area])
                    elif center_atom == 5:
                        face_stat_si = np.append(face_stat_si,[face_area])
        # sort large->small and compute cn
        face_stat_mg[::-1].sort()
        face_stat_ca[::-1].sort()
        face_stat_al[::-1].sort()
        face_stat_si[::-1].sort()
        cn_mg = (np.expand_dims(np.arange(1,len(face_stat_mg)+1),axis=1)) / atom_count[2]
        cn_ca = (np.expand_dims(np.arange(1,len(face_stat_ca)+1),axis=1)) / atom_count[3]
        cn_al = (np.expand_dims(np.arange(1,len(face_stat_al)+1),axis=1)) / atom_count[4]
        cn_si = (np.expand_dims(np.arange(1,len(face_stat_si)+1),axis=1)) / atom_count[5]

        # bin plot of Mg
        hist_fig = plt.figure('Mg-O')
        plt.xlabel('face area / Angstrom^2')
        plt.ylabel('Count')
        plt.title('Histogram of voronoi face area')
        ax = hist_fig.gca()
        ax.set_xlim(plot_axis_lim['Mg'][0:2])
        ax.set_ylim(plot_axis_lim['Mg'][2:4])
        ax.set_xticks(np.arange(0,math.ceil(plot_axis_lim['Mg'][1]),10))
        ax.set_yticks(np.arange(plot_axis_lim['Mg'][2],plot_axis_lim['Mg'][3]),1000)
        n,bins,patches=plt.hist(face_stat_mg,int(face_stat_mg[0]//bin_width))
        plt.show()
        # cn plot of Mg
        cn_fig = plt.figure('CN(Mg-O)')
        plt.xlabel('threshold / Angstrom^2')
        plt.ylabel('CN')
        plt.title('CN(Mg-O) - threshold of face area')
        plt.plot(face_stat_mg,cn_mg,'b-')
        ax = cn_fig.gca()
        ax.set_xlim(plot_axis_lim['Mg'][4:6])
        ax.set_ylim(plot_axis_lim['Mg'][6:])
        ax.set_xticks(np.arange(plot_axis_lim['Mg'][4],plot_axis_lim['Mg'][5],10))
        ax.set_yticks(np.arange(plot_axis_lim['Mg'][6],plot_axis_lim['Mg'][7]))
        plt.grid()
        plt.show()

        # bin plot of Ca
        hist_fig = plt.figure('Ca-O')
        plt.xlabel('face area / Angstrom^2')
        plt.ylabel('Count')
        plt.title('Histogram of voronoi face area')
        ax = hist_fig.gca()
        ax.set_xlim(plot_axis_lim['Ca'][0:2])
        ax.set_ylim(plot_axis_lim['Ca'][2:4])
        ax.set_xticks(np.arange(0,math.ceil(plot_axis_lim['Ca'][1])))
        ax.set_yticks(np.arange(plot_axis_lim['Ca'][2],plot_axis_lim['Ca'][3]),10)
        n,bins,patches=plt.hist(face_stat_ca,int(face_stat_ca[0]//bin_width))
        plt.show()
        # cn plot of Ca
        cn_fig = plt.figure('CN(Ca-O)')
        plt.xlabel('threshold / Angstrom^2')
        plt.ylabel('CN')
        plt.title('CN(Ca-O) - threshold of face area')
        plt.plot(face_stat_ca,cn_ca,'b-')
        ax = cn_fig.gca()
        ax.set_xlim(plot_axis_lim['Ca'][4:6])
        ax.set_ylim(plot_axis_lim['Ca'][6:])
        ax.set_xticks(np.arange(plot_axis_lim['Ca'][4],plot_axis_lim['Ca'][5]))
        ax.set_yticks(np.arange(plot_axis_lim['Ca'][6],plot_axis_lim['Ca'][7]))
        plt.grid()
        plt.show()

        # bin plot of Al
        hist_fig = plt.figure('Al-O')
        plt.xlabel('face area / Angstrom^2')
        plt.ylabel('Count')
        plt.title('Histogram of voronoi face area')
        ax = hist_fig.gca()
        ax.set_xlim(plot_axis_lim['Al'][0:2])
        ax.set_ylim(plot_axis_lim['Al'][2:4])
        ax.set_xticks(np.arange(0,math.ceil(plot_axis_lim['Al'][1])))
        ax.set_yticks(np.arange(plot_axis_lim['Al'][2],plot_axis_lim['Al'][3]),10)
        n,bins,patches=plt.hist(face_stat_al,int(face_stat_al[0]//bin_width))
        plt.show()
        # cn plot of Al
        cn_fig = plt.figure('CN(Al-O)')
        plt.xlabel('threshold / Angstrom^2')
        plt.ylabel('CN')
        plt.title('CN(Al-O) - threshold of face area')
        plt.plot(face_stat_al,cn_al,'b-')
        ax = cn_fig.gca()
        ax.set_xlim(plot_axis_lim['Al'][4:6])
        ax.set_ylim(plot_axis_lim['Al'][6:])
        ax.set_xticks(np.arange(plot_axis_lim['Al'][4],plot_axis_lim['Al'][5]))
        ax.set_yticks(np.arange(plot_axis_lim['Al'][6],plot_axis_lim['Al'][7]))
        plt.grid()
        plt.show()

        # bin plot of Si
        hist_fig = plt.figure('Si-O')
        plt.xlabel('face area / Angstrom^2')
        plt.ylabel('Count')
        plt.title('Histogram of voronoi face area')
        ax = hist_fig.gca()
        ax.set_xlim(plot_axis_lim['Si'][0:2])
        ax.set_ylim(plot_axis_lim['Si'][2:4])
        ax.set_xticks(np.arange(0,math.ceil(plot_axis_lim['Si'][1])))
        ax.set_yticks(np.arange(plot_axis_lim['Si'][2],plot_axis_lim['Si'][3]),10)
        n,bins,patches=plt.hist(face_stat_si,int(face_stat_si[0]//bin_width))
        plt.show()
        # cn plot of Si
        cn_fig = plt.figure('CN(Si-O)')
        plt.xlabel('threshold / Angstrom^2')
        plt.ylabel('CN')
        plt.title('CN(Si-O) - threshold of face area')
        plt.plot(face_stat_si,cn_si,'b-')
        ax = cn_fig.gca()
        ax.set_xlim(plot_axis_lim['Si'][4:6])
        ax.set_ylim(plot_axis_lim['Si'][6:])
        ax.set_xticks(np.arange(plot_axis_lim['Si'][4],plot_axis_lim['Si'][5]))
        ax.set_yticks(np.arange(plot_axis_lim['Si'][6],plot_axis_lim['Si'][7]))
        plt.grid()
        plt.show()

else:
    dump_file_list.remove('dump.fc_0.voro')
    n_frame = len(dump_file_list)
    # print(len(dump_file_list))
    traj_face_stat_mg = np.asarray([])
    traj_face_stat_ca = np.asarray([])
    traj_face_stat_al = np.asarray([])
    traj_face_stat_si = np.asarray([])
    for dump_file in dump_file_list:
        timestep = dump_file.split('.')[-1]
        with open(dump_file,'r') as neighbor_raw:
            # read face area array into memory
            face_stat_mg = np.asarray([])
            face_stat_ca = np.asarray([])
            face_stat_al = np.asarray([])
            face_stat_si = np.asarray([])
            for lc,lines in enumerate(neighbor_raw):
                if lc > 9:
                    center_atom = type_table[int(lines.split()[1])]
                    coord_atom = type_table[int(lines.split()[2])]
                    face_area = float(lines.split()[3])
                    if coord_atom == 6:
                        if center_atom == 2:
                            face_stat_mg = np.append(face_stat_mg,[face_area])
                        elif center_atom == 3:
                            face_stat_ca = np.append(face_stat_ca,[face_area])
                        elif center_atom == 4:
                            face_stat_al = np.append(face_stat_al,[face_area])
                        elif center_atom == 5:
                            face_stat_si = np.append(face_stat_si,[face_area])
            
            traj_face_stat_mg = np.concatenate((traj_face_stat_mg,face_stat_mg))
            traj_face_stat_ca = np.concatenate((traj_face_stat_ca,face_stat_ca))
            traj_face_stat_al = np.concatenate((traj_face_stat_al,face_stat_al))
            traj_face_stat_si = np.concatenate((traj_face_stat_si,face_stat_si))

    # sort large->small and compute cn
    traj_face_stat_mg[::-1].sort()
    traj_face_stat_ca[::-1].sort()
    traj_face_stat_al[::-1].sort()
    traj_face_stat_si[::-1].sort()
    cn_mg = (np.expand_dims(np.arange(1,len(traj_face_stat_mg)+1),axis=1)) / atom_count[2] / n_frame
    cn_ca = (np.expand_dims(np.arange(1,len(traj_face_stat_ca)+1),axis=1)) / atom_count[3] / n_frame
    cn_al = (np.expand_dims(np.arange(1,len(traj_face_stat_al)+1),axis=1)) / atom_count[4] / n_frame
    cn_si = (np.expand_dims(np.arange(1,len(traj_face_stat_si)+1),axis=1)) / atom_count[5] / n_frame


    # # bin plot of Mg
    # hist_fig = plt.figure('Mg-O')
    # plt.xlabel('face area / Angstrom^2')
    # plt.ylabel('Count')
    # plt.title('Histogram of voronoi face area')
    # ax = hist_fig.gca()
    # ax.set_xlim(plot_axis_lim['Mg'][0:2])
    # ax.set_ylim(plot_axis_lim['Mg'][2:4])
    # ax.set_xticks(np.arange(0,math.ceil(plot_axis_lim['Mg'][1])))
    # ax.set_yticks(np.arange(plot_axis_lim['Mg'][2],plot_axis_lim['Mg'][3]),10)
    # n,bins,patches=plt.hist(traj_face_stat_mg,int(traj_face_stat_mg[0]//bin_width))
    # # plt.show()
    # plt.savefig('Mg-O_hist.png')
    # cn plot of Mg
    cn_fig = plt.figure('CN(Mg-O)')
    plt.xlabel('threshold / Angstrom^2')
    plt.ylabel('CN')
    plt.title('CN(Mg-O) - threshold of face area')
    plt.plot(traj_face_stat_mg,cn_mg,'b-')
    ax = cn_fig.gca()
    ax.set_xlim(plot_axis_lim['Mg'][4:6])
    ax.set_ylim(plot_axis_lim['Mg'][6:])
    ax.set_xticks(np.arange(plot_axis_lim['Mg'][4],plot_axis_lim['Mg'][5]))
    ax.set_yticks(np.arange(plot_axis_lim['Mg'][6],plot_axis_lim['Mg'][7]))
    plt.grid()
    # plt.show()
    plt.savefig('Mg-O_cn.png')

    # # bin plot of Ca
    # hist_fig = plt.figure('Ca-O')
    # plt.xlabel('face area / Angstrom^2')
    # plt.ylabel('Count')
    # plt.title('Histogram of voronoi face area')
    # ax = hist_fig.gca()
    # ax.set_xlim(plot_axis_lim['Ca'][0:2])
    # ax.set_ylim(plot_axis_lim['Ca'][2:4])
    # ax.set_xticks(np.arange(0,math.ceil(plot_axis_lim['Ca'][1])))
    # ax.set_yticks(np.arange(plot_axis_lim['Ca'][2],plot_axis_lim['Ca'][3]),10)
    # n,bins,patches=plt.hist(traj_face_stat_ca,int(traj_face_stat_ca[0]//bin_width))
    # # plt.show()
    # plt.savefig('Ca-O_hist.png')
    # cn plot of Ca
    cn_fig = plt.figure('CN(Ca-O)')
    plt.xlabel('threshold / Angstrom^2')
    plt.ylabel('CN')
    plt.title('CN(Ca-O) - threshold of face area')
    plt.plot(traj_face_stat_ca,cn_ca,'b-')
    ax = cn_fig.gca()
    ax.set_xlim(plot_axis_lim['Ca'][4:6])
    ax.set_ylim(plot_axis_lim['Ca'][6:])
    ax.set_xticks(np.arange(plot_axis_lim['Ca'][4],plot_axis_lim['Ca'][5]))
    ax.set_yticks(np.arange(plot_axis_lim['Ca'][6],plot_axis_lim['Ca'][7]))
    plt.grid()
    # plt.show()
    plt.savefig('Ca-O_cn.png')

    # # bin plot of Al
    # hist_fig = plt.figure('Al-O')
    # plt.xlabel('face area / Angstrom^2')
    # plt.ylabel('Count')
    # plt.title('Histogram of voronoi face area')
    # ax = hist_fig.gca()
    # ax.set_xlim(plot_axis_lim['Al'][0:2])
    # ax.set_ylim(plot_axis_lim['Al'][2:4])
    # ax.set_xticks(np.arange(0,math.ceil(plot_axis_lim['Al'][1])))
    # ax.set_yticks(np.arange(plot_axis_lim['Al'][2],plot_axis_lim['Al'][3]),10)
    # n,bins,patches=plt.hist(traj_face_stat_al,int(traj_face_stat_al[0]//bin_width))
    # # plt.show()
    # plt.savefig('Al-O_hist.png')
    # cn plot of Al
    cn_fig = plt.figure('CN(Al-O)')
    plt.xlabel('threshold / Angstrom^2')
    plt.ylabel('CN')
    plt.title('CN(Al-O) - threshold of face area')
    plt.plot(traj_face_stat_al,cn_al,'b-')
    ax = cn_fig.gca()
    ax.set_xlim(plot_axis_lim['Al'][4:6])
    ax.set_ylim(plot_axis_lim['Al'][6:])
    ax.set_xticks(np.arange(plot_axis_lim['Al'][4],plot_axis_lim['Al'][5]))
    ax.set_yticks(np.arange(plot_axis_lim['Al'][6],plot_axis_lim['Al'][7]))
    plt.grid()
    # plt.show()
    plt.savefig('Al-O_cn.png')

    # # bin plot of Si
    # hist_fig = plt.figure('Si-O')
    # plt.xlabel('face area / Angstrom^2')
    # plt.ylabel('Count')
    # plt.title('Histogram of voronoi face area')
    # ax = hist_fig.gca()
    # ax.set_xlim(plot_axis_lim['Si'][0:2])
    # ax.set_ylim(plot_axis_lim['Si'][2:4])
    # ax.set_xticks(np.arange(0,math.ceil(plot_axis_lim['Si'][1])))
    # ax.set_yticks(np.arange(plot_axis_lim['Si'][2],plot_axis_lim['Si'][3]),10)
    # n,bins,patches=plt.hist(traj_face_stat_si,int(traj_face_stat_si[0]//bin_width))
    # # plt.show()
    # plt.savefig('Si-O_hist.png')
    # cn plot of Si
    cn_fig = plt.figure('CN(Si-O)')
    plt.xlabel('threshold / Angstrom^2')
    plt.ylabel('CN')
    plt.title('CN(Si-O) - threshold of face area')
    plt.plot(traj_face_stat_si,cn_si,'b-')
    ax = cn_fig.gca()
    ax.set_xlim(plot_axis_lim['Si'][4:6])
    ax.set_ylim(plot_axis_lim['Si'][6:])
    ax.set_xticks(np.arange(plot_axis_lim['Si'][4],plot_axis_lim['Si'][5]))
    ax.set_yticks(np.arange(plot_axis_lim['Si'][6],plot_axis_lim['Si'][7]))
    plt.grid()
    # plt.show()
    plt.savefig('Si-O_cn.png')

