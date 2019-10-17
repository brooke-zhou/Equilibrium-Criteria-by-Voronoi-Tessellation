#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 15 22:20:22 2018

@author: Yacong
"""
import glob,os
from initialize_dict import initialize_dict

def create_type_table(type_lookup_file):
    type_table = {0:0}
    # os.system('ls')
    with open(type_lookup_file,'r') as type_lookup:
        for lc,lines in enumerate(type_lookup):
            if lc > 0:
                type_table[int(lines.split()[0])] = int(lines.split()[1])
    return type_table

def two_atom_stat(dump_file,type_table):
    # extract 2-atom information
    sum_count, pair_stat2 = initialize_dict('2atom')
    pair_dict = {}
    with open(dump_file,'r') as neighbor_raw:
        for lc,lines in enumerate(neighbor_raw):
            if lc >= 9:
                # calculate 2-atom distriburion (pair_stat2: count of AB pairs)
                center_atom = type_table[int(lines.split()[1])]
                coord_atom = type_table[int(lines.split()[2])]
                if coord_atom != 0:
                    pair_stat2[10*center_atom+coord_atom] += 1
                    # create 2-pair dictionary (pair_dict: id of each atom in AB pairs)
                    id_center_atom = int(lines.split()[1])
                    id_coord_atom = int(lines.split()[2])
                    if id_center_atom in pair_dict:
                        pair_dict[id_center_atom] = pair_dict[id_center_atom] + [id_coord_atom]
                    else:
                        pair_dict[id_center_atom] = [id_coord_atom]
        for center_atom in range(2,7):
            for coord_atom in range(2,7):
                sum_count[center_atom] += pair_stat2[10*center_atom+coord_atom]
        # calculate sum of 2-atom percantage
        percent_sum = {}
        for n_center_atom in range(2,7):
            for n_coord_1 in range(2,7):
                ij = 10*n_center_atom+n_coord_1
                percent_sum[ij] = pair_stat2[ij]/sum_count[n_center_atom]
    return pair_dict, pair_stat2, sum_count, percent_sum

def three_atom_calc(dump_file,type_table,pair_dict):
    # create 3-atom distribution, i.e., fill in pair_stat
    # corrected double counting of [A1-B-A2 where A1==A2]
    # NOT counting atoms in 1st cn layer as 2nd NN's
    pair_stat, two_stat3 = initialize_dict('3atom')
    with open(dump_file,'r') as neighbor_raw:
        for lc,lines in enumerate(neighbor_raw):
            if lc >= 9:
                n_center_atom = int(lines.split()[1])
                center_atom = type_table[n_center_atom]
                n_coord_atom_1 = int(lines.split()[2])
                coord_atom_1 = type_table[n_coord_atom_1]
                if n_coord_atom_1 != 0:
                    corrected = False
                    for n_coord_atom_2 in pair_dict[n_coord_atom_1]:
                        coord_atom_2 = type_table[n_coord_atom_2]
                        list_of_coord_1=pair_dict[n_center_atom]
                        # if coord_atom_2 != 0:
                        if (coord_atom_2 != 0) and (n_coord_atom_2 not in list_of_coord_1):
                            tri = 100*center_atom+10*coord_atom_1+coord_atom_2
                            pair_stat[tri] += 1
                            if center_atom == coord_atom_2 and not corrected:
                                pair_stat[tri] -= 1
                                corrected = True
    for n_center_atom in range(2,7):
            for n_coord_atom_1 in range(2,7):
                for n_coord_atom_2 in range(2,7):
                    two_stat3[10*n_center_atom+n_coord_atom_1] += \
                    pair_stat[100*n_center_atom+10*n_coord_atom_1+n_coord_atom_2]
    return pair_stat, two_stat3

def write_stat_tab(option,output_file,two_stat3,pair_stat,percent_sum,n_frame=1):
    stat_table_header = ('======================================================\n'
                         '3-Atom Distribution Analysis. \n'
                         '------------------------------------------------------\n'
                         'Top-Left Cornor = Center Atom \n'
                         'Vertical increase (rows) = 1st Coordination Atom \n'
                         'Horizontal increase (columns) = 2nd Coordination Atom\n'
                         'Contents = Percenntage of [A-B-C] \n'
                         '======================================================\n\n\n')
    dividing = '-----------------------------------------------------------------\n'
    elements = {1:'Na',2:'Mg',3:'Ca',4:'Al',5:'Si',6:'O'}
    with open(output_file,'w') as stat_table:
         stat_table.write(stat_table_header)
         for n_center_atom in range(2,7):
            header_line = elements[n_center_atom]+\
            '\t|\tMg\t\t\tCa\t\t\tAl\t\t\tSi\t\t\tO\n'
            stat_table.write(header_line)
            stat_table.write(dividing)
            for n_coord_atom_1 in range(2,7):
               coord_atom_1 = elements[n_coord_atom_1]
               content_line = coord_atom_1+'\t|\t'
               for n_coord_atom_2 in range(2,7):
                  coord_atom_2 = elements[n_coord_atom_2]
                  ijk = 100*n_center_atom+10*n_coord_atom_1+n_coord_atom_2
                  ij = 10*n_center_atom+n_coord_atom_1
                  if option == 'calc':
                     if two_stat3[ij] == 0 or pair_stat[ijk] == 0:
                        if two_stat3[ij] == 0:
                           value_write = "{:.6f}".format(0) # keep zeros 
                           # value_write = "-\t"  # replace zeros by dashes
                        else:
                           value_write = "{:.6f}".format(0) # keep zeros 
                     else:
                        value_write = "{:.6f}".\
                           format(round(pair_stat[ijk]/two_stat3[ij]*100*percent_sum[ij],6))
                  elif option == 'face_count':
                     if two_stat3[ij] == 0 or pair_stat[ijk] == 0:
                        if two_stat3[ij] == 0:
                           value_write = "{:.6f}".format(0) # keep zeros 
                           # value_write = "-\t"  # replace zeros by dashes
                        else:
                           value_write = "{:.6f}".format(0) # keep zeros 
                     else:
                        value_write = "{:.6f}".format(pair_stat[ijk])
                  elif option == 'avg':
                     value_write = "{:.6f}".format(round(pair_stat[ijk]/n_frame,6))
                  if coord_atom_2 != 'O':
                     content_line += value_write+'\t'
                  else:
                     content_line += value_write+'\n'
               stat_table.write(content_line)
            sum_line = '\n\n'
            stat_table.write(sum_line)

def three_atom_stat(splitted_dump_folder_name,type_lookup_file):
    dump_file_head = 'dump.'
    output_file_head = '3atom_stat.'
    path_to_splitted_dump = './'+splitted_dump_folder_name
    folder_of_stat_files = '3atom_stat'

    atom_count = {1:0,\
                  2:64,\
                  3:100,\
                  4:72,\
                  5:200,\
                  6:672}

    # create type_table (id-type)
    type_table = create_type_table(type_lookup_file)

    os.chdir(path_to_splitted_dump)
    dump_file_list = glob.glob(dump_file_head+'*')
    if len(dump_file_list) == 1:
        print('Found only 1 dump file!')
        dump_file = dump_file_list[0]
        output_file = output_file_head + '.tab'
        # extract 2-atom information
        pair_dict, pair_stat2, sum_count, percent_sum = two_atom_stat(dump_file,type_table)
        # create 3-atom distribution
        pair_stat, two_stat3 = three_atom_calc(dump_file,type_table,pair_dict)
        # write output file
        write_stat_tab('calc',output_file,two_stat3,pair_stat,percent_sum)
    else:
        for dump_file in dump_file_list:
            timestep = dump_file.split('.')[-1]
            output_file = output_file_head+timestep+'.tab'
            # extract 2-atom information
            pair_dict, pair_stat2, sum_count, percent_sum = two_atom_stat(dump_file,type_table)
            # create 3-atom distribution
            pair_stat, two_stat3 = three_atom_calc(dump_file,type_table,pair_dict)
            # write output file
            write_stat_tab('calc',output_file,two_stat3,pair_stat,percent_sum)
        os.makedirs('./'+folder_of_stat_files)       
        os.system('mv *.tab ./'+folder_of_stat_files)
            
def three_atom_avg(splitted_dump_folder_name):
   stat_file_head = '3atom_stat.'
   output_file = '3atom_avg.tab'
   path_to_3atom_stat_files = './3atom_stat/'

   os.chdir(path_to_3atom_stat_files)
   stat_file_list = glob.glob(stat_file_head+'*')
   n_frame = len(stat_file_list)

   pair_stat = initialize_dict('pair_stat')

   for stat_file in stat_file_list:
      # print(stat_file)
      with open(stat_file,'r') as stat_individual:
         for lc,lines in enumerate(stat_individual):
            if lc == 12:
                fields = lines.split()
                pair_stat[222] += float(fields[2])
                pair_stat[223] += float(fields[3])
                pair_stat[224] += float(fields[4])
                pair_stat[225] += float(fields[5])
                pair_stat[226] += float(fields[6])
            elif lc == 13:
                fields = lines.split()
                pair_stat[232] += float(fields[2])
                pair_stat[233] += float(fields[3])
                pair_stat[234] += float(fields[4])
                pair_stat[235] += float(fields[5])
                pair_stat[236] += float(fields[6])
            elif lc == 14:
                fields = lines.split()
                pair_stat[242] += float(fields[2])
                pair_stat[243] += float(fields[3])
                pair_stat[244] += float(fields[4])
                pair_stat[245] += float(fields[5])
                pair_stat[246] += float(fields[6])
            elif lc == 15:
                fields = lines.split()
                pair_stat[252] += float(fields[2])
                pair_stat[253] += float(fields[3])
                pair_stat[254] += float(fields[4])
                pair_stat[255] += float(fields[5])
                pair_stat[256] += float(fields[6])
            elif lc == 16:
                fields = lines.split()
                pair_stat[262] += float(fields[2])
                pair_stat[263] += float(fields[3])
                pair_stat[264] += float(fields[4])
                pair_stat[265] += float(fields[5])
                pair_stat[266] += float(fields[6])
            elif lc == 21:
                fields = lines.split()
                pair_stat[322] += float(fields[2])
                pair_stat[323] += float(fields[3])
                pair_stat[324] += float(fields[4])
                pair_stat[325] += float(fields[5])
                pair_stat[326] += float(fields[6])
            elif lc == 22:
                fields = lines.split()
                pair_stat[332] += float(fields[2])
                pair_stat[333] += float(fields[3])
                pair_stat[334] += float(fields[4])
                pair_stat[335] += float(fields[5])
                pair_stat[336] += float(fields[6])
            elif lc == 23:
                fields = lines.split()
                pair_stat[342] += float(fields[2])
                pair_stat[343] += float(fields[3])
                pair_stat[344] += float(fields[4])
                pair_stat[345] += float(fields[5])
                pair_stat[346] += float(fields[6])
            elif lc == 24:
                fields = lines.split()
                pair_stat[352] += float(fields[2])
                pair_stat[353] += float(fields[3])
                pair_stat[354] += float(fields[4])
                pair_stat[355] += float(fields[5])
                pair_stat[356] += float(fields[6])
            elif lc == 25:
                fields = lines.split()
                pair_stat[362] += float(fields[2])
                pair_stat[363] += float(fields[3])
                pair_stat[364] += float(fields[4])
                pair_stat[365] += float(fields[5])
                pair_stat[366] += float(fields[6])
            elif lc == 30:
                fields = fields = lines.split()
                pair_stat[422] += float(fields[2])
                pair_stat[423] += float(fields[3])
                pair_stat[424] += float(fields[4])
                pair_stat[425] += float(fields[5])
                pair_stat[426] += float(fields[6])
            elif lc == 31:
                fields = fields = lines.split()
                pair_stat[432] += float(fields[2])
                pair_stat[433] += float(fields[3])
                pair_stat[434] += float(fields[4])
                pair_stat[435] += float(fields[5])
                pair_stat[436] += float(fields[6])
            elif lc == 32:
                fields = fields = lines.split()
                pair_stat[442] += float(fields[2])
                pair_stat[443] += float(fields[3])
                pair_stat[444] += float(fields[4])
                pair_stat[445] += float(fields[5])
                pair_stat[446] += float(fields[6])
            elif lc == 33:
                fields = fields = lines.split()
                pair_stat[452] += float(fields[2])
                pair_stat[453] += float(fields[3])
                pair_stat[454] += float(fields[4])
                pair_stat[455] += float(fields[5])
                pair_stat[456] += float(fields[6])
            elif lc == 34:
                fields = fields = lines.split()
                pair_stat[462] += float(fields[2])
                pair_stat[463] += float(fields[3])
                pair_stat[464] += float(fields[4])
                pair_stat[465] += float(fields[5])
                pair_stat[466] += float(fields[6])
            elif lc == 39:
                fields = fields = lines.split()
                pair_stat[522] += float(fields[2])
                pair_stat[523] += float(fields[3])
                pair_stat[524] += float(fields[4])
                pair_stat[525] += float(fields[5])
                pair_stat[526] += float(fields[6])
            elif lc == 40:
                fields = fields = lines.split()
                pair_stat[532] += float(fields[2])
                pair_stat[533] += float(fields[3])
                pair_stat[534] += float(fields[4])
                pair_stat[535] += float(fields[5])
                pair_stat[536] += float(fields[6])
            elif lc == 41:
                fields = fields = lines.split()
                pair_stat[542] += float(fields[2])
                pair_stat[543] += float(fields[3])
                pair_stat[544] += float(fields[4])
                pair_stat[545] += float(fields[5])
                pair_stat[546] += float(fields[6])
            elif lc == 42:
                fields = fields = lines.split()
                pair_stat[552] += float(fields[2])
                pair_stat[553] += float(fields[3])
                pair_stat[554] += float(fields[4])
                pair_stat[555] += float(fields[5])
                pair_stat[556] += float(fields[6])
            elif lc == 43:
                fields = fields = lines.split()
                pair_stat[562] += float(fields[2])
                pair_stat[563] += float(fields[3])
                pair_stat[564] += float(fields[4])
                pair_stat[565] += float(fields[5])
                pair_stat[566] += float(fields[6])
            elif lc == 48:
                fields = fields = lines.split()
                pair_stat[622] += float(fields[2])
                pair_stat[623] += float(fields[3])
                pair_stat[624] += float(fields[4])
                pair_stat[625] += float(fields[5])
                pair_stat[626] += float(fields[6])
            elif lc == 49:
                fields = fields = lines.split()
                pair_stat[632] += float(fields[2])
                pair_stat[633] += float(fields[3])
                pair_stat[634] += float(fields[4])
                pair_stat[635] += float(fields[5])
                pair_stat[636] += float(fields[6])
            elif lc == 50:
                fields = fields = lines.split()
                pair_stat[642] += float(fields[2])
                pair_stat[643] += float(fields[3])
                pair_stat[644] += float(fields[4])
                pair_stat[645] += float(fields[5])
                pair_stat[646] += float(fields[6])
            elif lc == 51:
                fields = fields = lines.split()
                pair_stat[652] += float(fields[2])
                pair_stat[653] += float(fields[3])
                pair_stat[654] += float(fields[4])
                pair_stat[655] += float(fields[5])
                pair_stat[656] += float(fields[6])
            elif lc == 52:
                fields = fields = lines.split()
                pair_stat[662] += float(fields[2])
                pair_stat[663] += float(fields[3])
                pair_stat[664] += float(fields[4])
                pair_stat[665] += float(fields[5])
                pair_stat[666] += float(fields[6])
   write_stat_tab('avg',output_file,{},pair_stat,{},n_frame)
