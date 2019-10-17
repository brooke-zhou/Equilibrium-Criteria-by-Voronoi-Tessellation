#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 27 13:53:37 2018

@author: Yacong
"""
import glob

type_lookup_file = 'id-type.tab'
dump_file_head = 'dump.neighbors'
output_file_head = '2pair_stat.'

dividing = '-------------------------------\n'
elements = {1:'Na',2:'Mg',3:'Ca',4:'Al',5:'Si',6:'O'}

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

dump_file_list = glob.glob(dump_file_head+'*')
if len(dump_file_list) == 1:
    print('Found only 1 dump file!')
    dump_file = dump_file_list[0]
    output_file = output_file_head + '.tab'
    sum_count = {1:0,\
                 2:0,\
                 3:0,\
                 4:0,\
                 5:0,\
                 6:0}

    pair_stat = {11: 0,\
                 21: 0,\
                 31: 0,\
                 41: 0,\
                 51: 0,\
                 61: 0,\
                 12: 0,\
                 22: 0,\
                 32: 0,\
                 42: 0,\
                 52: 0,\
                 62: 0,\
                 13: 0,\
                 23: 0,\
                 33: 0,\
                 43: 0,\
                 53: 0,\
                 63: 0,\
                 14: 0,\
                 24: 0,\
                 34: 0,\
                 44: 0,\
                 54: 0,\
                 64: 0,\
                 15: 0,\
                 25: 0,\
                 35: 0,\
                 45: 0,\
                 55: 0,\
                 65: 0,\
                 16: 0,\
                 26: 0,\
                 36: 0,\
                 46: 0,\
                 56: 0,\
                 66: 0}

    with open(dump_file,'r') as neighbor_raw:
        for lc,lines in enumerate(neighbor_raw):
            if lc >= 9:
                center_atom = type_table[int(lines.split()[1])]
                coord_atom = type_table[int(lines.split()[2])]
                if center_atom*coord_atom != 0:
                    pair_stat[10*center_atom+coord_atom] += 1
        for i in range(1,6):
            for j in range(1,6):
                sum_count[i+1] += pair_stat[10*(i+1)+(j+1)]
                
    with open(output_file,'w') as stat_table:
        for i in range(1,6):
            center_atom = elements[i+1]
            stat_table.write(center_atom+'\n')
            stat_table.write(dividing)
            header_line ='Pair\tCount\t%\tCN\n'
            stat_table.write(header_line)
            for j in range(1,6):
                coord_atom = elements[j+1]
                content_line = center_atom+'-'+coord_atom+'\t'+\
                               "{:d}".format(pair_stat[10*(i+1)+(j+1)])+'\t'+\
                               "{:.2f}".format(pair_stat[10*(i+1)+(j+1)]/sum_count[i+1]*100)+'\t'+\
                               "{:.2f}".format(pair_stat[10*(i+1)+(j+1)]/atom_count[i+1])+'\n'
                stat_table.write(content_line)
            sum_line = 'Sum('+center_atom+')\t'+"{:d}".format(sum_count[i+1])+'\t100\t'+\
                       "{:.2f}".format(sum_count[i+1] / atom_count[i+1])+'\n\n'
            stat_table.write(sum_line)

else:
    dump_file_list.remove('dump.neighbors')
    for dump_file in dump_file_list:
        timestep = dump_file.split('.')[-1]
        output_file = output_file_head+timestep+'.tab'
        sum_count = {1:0,\
                     2:0,\
                     3:0,\
                     4:0,\
                     5:0,\
                     6:0}

        pair_stat = {11: 0,\
                     21: 0,\
                     31: 0,\
                     41: 0,\
                     51: 0,\
                     61: 0,\
                     12: 0,\
                     22: 0,\
                     32: 0,\
                     42: 0,\
                     52: 0,\
                     62: 0,\
                     13: 0,\
                     23: 0,\
                     33: 0,\
                     43: 0,\
                     53: 0,\
                     63: 0,\
                     14: 0,\
                     24: 0,\
                     34: 0,\
                     44: 0,\
                     54: 0,\
                     64: 0,\
                     15: 0,\
                     25: 0,\
                     35: 0,\
                     45: 0,\
                     55: 0,\
                     65: 0,\
                     16: 0,\
                     26: 0,\
                     36: 0,\
                     46: 0,\
                     56: 0,\
                     66: 0}

        with open(dump_file,'r') as neighbor_raw:
            for lc,lines in enumerate(neighbor_raw):
                if lc >= 9:
                    center_atom = type_table[int(lines.split()[1])]
                    coord_atom = type_table[int(lines.split()[2])]
                    if center_atom*coord_atom != 0:
                        pair_stat[10*center_atom+coord_atom] += 1
            for i in range(6):
                for j in range(6):
                    sum_count[i+1] += pair_stat[10*(i+1)+(j+1)]
                    
        with open(output_file,'w') as stat_table:
            for i in range(1,6):
                center_atom = elements[i+1]
                stat_table.write(center_atom+'\n')
                stat_table.write(dividing)
                header_line ='Pair\tCount\t%\tCN\n'
                stat_table.write(header_line)
                for j in range(1,6):
                    coord_atom = elements[j+1]
                    content_line = center_atom+'-'+coord_atom+'\t'+\
                                   "{:d}".format(pair_stat[10*(i+1)+(j+1)])+'\t'+\
                                   "{:.2f}".format(pair_stat[10*(i+1)+(j+1)]/sum_count[i+1]*100)+'\t'+\
                                   "{:.2f}".format(pair_stat[10*(i+1)+(j+1)]/atom_count[i+1])+'\n'
                    stat_table.write(content_line)
                sum_line = 'Sum('+center_atom+')\t'+"{:d}".format(sum_count[i+1])+'\t100\t'+\
                           "{:.2f}".format(sum_count[i+1] / atom_count[i+1])+'\n\n'
                stat_table.write(sum_line)