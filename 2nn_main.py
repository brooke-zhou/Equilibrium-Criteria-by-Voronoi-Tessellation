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
import edist
from read_tab import read_tab

# global var_g

def main(argv):
    # global var_g

    parser = argparse.ArgumentParser(description=
        'calculate 3-atom distribution from lammps voronoi dump files')

    # arguments
    parser.add_argument('-path2dump', type=str, default='./25GPa_fc_0/', nargs=1, 
        help="path to the directory of dump files")
    parser.add_argument('-full_output', type=bool, default=True, nargs=1,
        help='whether to save all the single-frame dump and tab files')
    parser.add_argument('-ref', type=str, default='calc_avg', nargs=1,
        help='calc_avg: ref dist is avg of traj (usually LJ). require dump.ref.voro;\
              all_0: ref is all zeros;\
              prob: ref is probabilistic;\
              read_from_avg: ref is read from ./3atom_avg.tab')
    parser.add_argument('-path2idtype', type=str,default='../id-type.tab', nargs=1,
        help='path to id-type.tab')

    args = parser.parse_args()

    path_to_dump = args.path2dump
    save_all = args.full_output
    ref = args.ref
    id_type = args.path2idtype

    os.chdir(path_to_dump)
    dump_file_list = glob.glob('dump.'+"*")
    # make ref
    if ref == 'all_0':
        ref_dist = read_tab('./ref.0.tab')
    elif ref == 'prob':
        ref_dist = read_tab('./ref.prob.tab')
    elif ref == 'read_from_avg':
        ref_dist = read_tab('./3atom_avg.tab')
    elif ref == 'calc_avg':
        split_traj_dump.split_traj_dump('dump.ref.voro')
        three_atom_stat.three_atom_stat('ref',id_type)
        three_atom_stat.three_atom_avg('ref')
        ref_dist = read_tab('./3atom_avg.tab')
        os.chdir('../..')
        dump_file_list.remove('dump.ref.voro')

    # calculate 3atom stat for each piece of trajectory
    for dump_file in dump_file_list:
        job_name = dump_file[5:-5]
        split_traj_dump.split_traj_dump(dump_file)
        three_atom_stat.three_atom_stat(job_name,id_type)
        three_atom_stat.three_atom_avg(job_name)
        os.chdir('../..')

    # connect traj pieces of all time and plot edist-t
    # job_name = path2dump.split('/')[-2]+'_connected'
    traj_dirs = edist.connect_all_t()
    edist.save_avg_edist(ref_dist,'../',traj_dirs)
    edist.plot_edist_t(ref_dist,'../connected',show_plot=True)

# Allows the script to run as an exe
if __name__ == "__main__":
     main(sys.argv[1:])
