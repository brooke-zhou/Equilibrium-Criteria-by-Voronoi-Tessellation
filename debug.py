#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Split a single lammps dump file into differnt timesteps

Created on Mon May 14 22:06:34 2018

@author: Yacong
"""

import glob,os,sys,argparse
import split_traj_dump
import three_atom_stat
import read_tab
import edist

# global var_g

def main(argv):
    # global var_g

    parser = argparse.ArgumentParser(description=
        'calculate 3-atom distribution from lammps voronoi dump files')

    # arguments
    parser.add_argument('-path2dump', type=str, default='./25GPa_fc_0/', nargs=1, 
        help="path to the directory of dump files")
    parser.add_argument('-full_output', type=bool, default=False, nargs=1,
        help='whether to save all the single-frame dump and tab files')
    parser.add_argument('-ref', type=str, default='LJ', nargs=1,
        help='avg: ref dist is avg of traj (usually LJ). require dump.ref.voro;\
              all_0: ref is all zeros;\
              prob: ref is probabilistic')
    parser.add_argument('-path2idtype', type=str,default='../id-type.tab', nargs=1,
        help='path to id-type.tab')

    args = parser.parse_args()

    path_to_dump = args.path2dump
    save_all = args.full_output
    ref = args.ref
    id_type = args.path2idtype

    os.chdir(path_to_dump)

    # edist.connect_all_t()
    # ref_dist = read_tab.read_tab('./ref/3atom_stat/3atom_avg.tab')
    ref_dist = read_tab.read_tab('../ref.prob.tab')
    edist.plot_edist_t(ref_dist,'./connected',save_edist=False,save_option='by_weights',show_plot=True,weighing_vector='adjusted')
    # os.chdir('../')
    # edist.save_edist(ref_dist,'./',['0-0.05','0.05-1.05'],option='one_by_one')
    # edist.save_edist(ref_dist,'./',['0-0.05','0.05-1.05','1.05-2.05','2.05-3.05'],option='one_by_one')


    # a=os.listdir('./')
    # print(a)
    # import re
    # b=[]
    # for i in a:
        # print(i)
        # k=re.search("[A-Za-z]", i)
        # if k == None:
        #     print(k)
        #     print(i)
        #     b.append(i)
    #     if re.search("[A-Za-z]", i):
    #         print(i)
    #         a.remove(i)
    # print(b)
    # for root, dirs, files in os.walk('./'):
        # print(root)  
        # print(dirs)  
        # print(files)  

# Allows the script to run as an exe
if __name__ == "__main__":
     main(sys.argv[1:])
