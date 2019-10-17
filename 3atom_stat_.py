#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 28 16:21:22 2018

@author: Yacong
"""
import glob,os

type_lookup_file = 'id-type.tab'
dump_file_head = 'dump.fc_0.'
output_file_head = '3atom_stat.'
# path_to_splitted_dump = './'
# folder_of_stat_files = '3atom_stat'
path_to_splitted_dump = './tt/'
folder_of_stat_files = '2nn_corrected'

dividing = '-----------------------------------------------------------------\n'
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

os.chdir(path_to_splitted_dump)
dump_file_list = glob.glob(dump_file_head+'*')
if len(dump_file_list) == 1:
    print('Found only 1 dump file!')
    dump_file = dump_file_list[0]
    output_file = output_file_head + '.tab'
    sum_count = {2:0,\
                 3:0,\
                 4:0,\
                 5:0,\
                 6:0}

    pair_stat2 = {22: 0,\
                 32: 0,\
                 42: 0,\
                 52: 0,\
                 62: 0,\
                 23: 0,\
                 33: 0,\
                 43: 0,\
                 53: 0,\
                 63: 0,\
                 24: 0,\
                 34: 0,\
                 44: 0,\
                 54: 0,\
                 64: 0,\
                 25: 0,\
                 35: 0,\
                 45: 0,\
                 55: 0,\
                 65: 0,\
                 26: 0,\
                 36: 0,\
                 46: 0,\
                 56: 0,\
                 66: 0}

    pair_stat = {222: 0,\
                 223: 0,\
                 224: 0,\
                 225: 0,\
                 226: 0,\
                 232: 0,\
                 233: 0,\
                 234: 0,\
                 235: 0,\
                 236: 0,\
                 242: 0,\
                 243: 0,\
                 244: 0,\
                 245: 0,\
                 246: 0,\
                 252: 0,\
                 253: 0,\
                 254: 0,\
                 255: 0,\
                 256: 0,\
                 262: 0,\
                 263: 0,\
                 264: 0,\
                 265: 0,\
                 266: 0,\
                 322: 0,\
                 323: 0,\
                 324: 0,\
                 325: 0,\
                 326: 0,\
                 332: 0,\
                 333: 0,\
                 334: 0,\
                 335: 0,\
                 336: 0,\
                 342: 0,\
                 343: 0,\
                 344: 0,\
                 345: 0,\
                 346: 0,\
                 352: 0,\
                 353: 0,\
                 354: 0,\
                 355: 0,\
                 356: 0,\
                 362: 0,\
                 363: 0,\
                 364: 0,\
                 365: 0,\
                 366: 0,\
                 422: 0,\
                 423: 0,\
                 424: 0,\
                 425: 0,\
                 426: 0,\
                 432: 0,\
                 433: 0,\
                 434: 0,\
                 435: 0,\
                 436: 0,\
                 442: 0,\
                 443: 0,\
                 444: 0,\
                 445: 0,\
                 446: 0,\
                 452: 0,\
                 453: 0,\
                 454: 0,\
                 455: 0,\
                 456: 0,\
                 462: 0,\
                 463: 0,\
                 464: 0,\
                 465: 0,\
                 466: 0,\
                 522: 0,\
                 523: 0,\
                 524: 0,\
                 525: 0,\
                 526: 0,\
                 532: 0,\
                 533: 0,\
                 534: 0,\
                 535: 0,\
                 536: 0,\
                 542: 0,\
                 543: 0,\
                 544: 0,\
                 545: 0,\
                 546: 0,\
                 552: 0,\
                 553: 0,\
                 554: 0,\
                 555: 0,\
                 556: 0,\
                 562: 0,\
                 563: 0,\
                 564: 0,\
                 565: 0,\
                 566: 0,\
                 622: 0,\
                 623: 0,\
                 624: 0,\
                 625: 0,\
                 626: 0,\
                 632: 0,\
                 633: 0,\
                 634: 0,\
                 635: 0,\
                 636: 0,\
                 642: 0,\
                 643: 0,\
                 644: 0,\
                 645: 0,\
                 646: 0,\
                 652: 0,\
                 653: 0,\
                 654: 0,\
                 655: 0,\
                 656: 0,\
                 662: 0,\
                 663: 0,\
                 664: 0,\
                 665: 0,\
                 666: 0}

    two_stat3 = {22: 0,\
                 32: 0,\
                 42: 0,\
                 52: 0,\
                 62: 0,\
                 23: 0,\
                 33: 0,\
                 43: 0,\
                 53: 0,\
                 63: 0,\
                 24: 0,\
                 34: 0,\
                 44: 0,\
                 54: 0,\
                 64: 0,\
                 25: 0,\
                 35: 0,\
                 45: 0,\
                 55: 0,\
                 65: 0,\
                 26: 0,\
                 36: 0,\
                 46: 0,\
                 56: 0,\
                 66: 0}

    # extract 2-atom information
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
                
    # create 3-atom distribution, i.e., fill in pair_stat
    # corrected double counting of [A1-B-A2 where A1==A2]
    # NOT counting atoms in 1st cn layer as 2nd NN's
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
    with open(output_file,'w') as stat_table:
        stat_table.write(
    '''======================================================
3-Atom Distribution Analysis. 
------------------------------------------------------
Top-Left Cornor = Center Atom 
Vertical increase (rows) = 1st Coordination Atom 
Horizontal increase (columns) = 2nd Coordination Atom
Contents = Percenntage of [A-B-C] 
======================================================\n\n\n''')
        
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
                    if two_stat3[ij] == 0 or pair_stat[ijk] == 0:
                        if two_stat3[ij] == 0:
                            value_write = "-\t"  # replace zeros by dashes
                        else:
                            value_write = "{:.6f}".format(0) # keep zeros 
                    else:
                        # value_write = "{:d}".\
                        value_write = "{:.6f}".\
                            format(round(pair_stat[ijk]/two_stat3[ij]*100*percent_sum[ij],6))
                            # format(pair_stat[ijk])
                    if coord_atom_2 != 'O':
                        content_line += value_write+'\t'
                    else:
                        content_line += value_write+'\n'
                stat_table.write(content_line)
            sum_line = '\n\n'
            stat_table.write(sum_line)
else:
    # dump_file_list.remove('dump.neighbors')
    # dump_file_list.remove('dump.fc_0.voro')
    for dump_file in dump_file_list:
        timestep = dump_file.split('.')[-1]
        output_file = output_file_head+timestep+'.tab'
        sum_count = {2:0,\
                     3:0,\
                     4:0,\
                     5:0,\
                     6:0}

        pair_stat2 = {22: 0,\
                     32: 0,\
                     42: 0,\
                     52: 0,\
                     62: 0,\
                     23: 0,\
                     33: 0,\
                     43: 0,\
                     53: 0,\
                     63: 0,\
                     24: 0,\
                     34: 0,\
                     44: 0,\
                     54: 0,\
                     64: 0,\
                     25: 0,\
                     35: 0,\
                     45: 0,\
                     55: 0,\
                     65: 0,\
                     26: 0,\
                     36: 0,\
                     46: 0,\
                     56: 0,\
                     66: 0}

        pair_stat = {222: 0,\
                     223: 0,\
                     224: 0,\
                     225: 0,\
                     226: 0,\
                     232: 0,\
                     233: 0,\
                     234: 0,\
                     235: 0,\
                     236: 0,\
                     242: 0,\
                     243: 0,\
                     244: 0,\
                     245: 0,\
                     246: 0,\
                     252: 0,\
                     253: 0,\
                     254: 0,\
                     255: 0,\
                     256: 0,\
                     262: 0,\
                     263: 0,\
                     264: 0,\
                     265: 0,\
                     266: 0,\
                     322: 0,\
                     323: 0,\
                     324: 0,\
                     325: 0,\
                     326: 0,\
                     332: 0,\
                     333: 0,\
                     334: 0,\
                     335: 0,\
                     336: 0,\
                     342: 0,\
                     343: 0,\
                     344: 0,\
                     345: 0,\
                     346: 0,\
                     352: 0,\
                     353: 0,\
                     354: 0,\
                     355: 0,\
                     356: 0,\
                     362: 0,\
                     363: 0,\
                     364: 0,\
                     365: 0,\
                     366: 0,\
                     422: 0,\
                     423: 0,\
                     424: 0,\
                     425: 0,\
                     426: 0,\
                     432: 0,\
                     433: 0,\
                     434: 0,\
                     435: 0,\
                     436: 0,\
                     442: 0,\
                     443: 0,\
                     444: 0,\
                     445: 0,\
                     446: 0,\
                     452: 0,\
                     453: 0,\
                     454: 0,\
                     455: 0,\
                     456: 0,\
                     462: 0,\
                     463: 0,\
                     464: 0,\
                     465: 0,\
                     466: 0,\
                     522: 0,\
                     523: 0,\
                     524: 0,\
                     525: 0,\
                     526: 0,\
                     532: 0,\
                     533: 0,\
                     534: 0,\
                     535: 0,\
                     536: 0,\
                     542: 0,\
                     543: 0,\
                     544: 0,\
                     545: 0,\
                     546: 0,\
                     552: 0,\
                     553: 0,\
                     554: 0,\
                     555: 0,\
                     556: 0,\
                     562: 0,\
                     563: 0,\
                     564: 0,\
                     565: 0,\
                     566: 0,\
                     622: 0,\
                     623: 0,\
                     624: 0,\
                     625: 0,\
                     626: 0,\
                     632: 0,\
                     633: 0,\
                     634: 0,\
                     635: 0,\
                     636: 0,\
                     642: 0,\
                     643: 0,\
                     644: 0,\
                     645: 0,\
                     646: 0,\
                     652: 0,\
                     653: 0,\
                     654: 0,\
                     655: 0,\
                     656: 0,\
                     662: 0,\
                     663: 0,\
                     664: 0,\
                     665: 0,\
                     666: 0}

        two_stat3 = {22: 0,\
                     32: 0,\
                     42: 0,\
                     52: 0,\
                     62: 0,\
                     23: 0,\
                     33: 0,\
                     43: 0,\
                     53: 0,\
                     63: 0,\
                     24: 0,\
                     34: 0,\
                     44: 0,\
                     54: 0,\
                     64: 0,\
                     25: 0,\
                     35: 0,\
                     45: 0,\
                     55: 0,\
                     65: 0,\
                     26: 0,\
                     36: 0,\
                     46: 0,\
                     56: 0,\
                     66: 0}


        # extract 2-atom information
        pair_dict = {}
        with open(dump_file,'r') as neighbor_raw:
            for lc,lines in enumerate(neighbor_raw):
                if lc >= 9:
                    # calculate 2-atom distriburion
                    center_atom = type_table[int(lines.split()[1])]
                    coord_atom = type_table[int(lines.split()[2])]
                    if coord_atom != 0:
                        pair_stat2[10*center_atom+coord_atom] += 1
                        # create 2-pair dictionary
                        id_center_atom = int(lines.split()[1])
                        id_coord_atom = int(lines.split()[2])
                        if id_center_atom in pair_dict:
                            pair_dict[id_center_atom] = pair_dict[id_center_atom] + [id_coord_atom]
                        else:
                            pair_dict[id_center_atom] = [id_coord_atom]
            for i in range(2,7):
                for j in range(2,7):
                    sum_count[i] += pair_stat2[10*i+j]

        # calculate sum of 2-atom percantage
        percent_sum = {}
        for n_center_atom in range(2,7):
            for n_coord_1 in range(2,7):
                ij = 10*n_center_atom+n_coord_1
                percent_sum[ij] = pair_stat2[ij]/sum_count[n_center_atom]
                    
        # create 3-atom distribution, i.e., fill in pair_stat
        # corrected double counting of [A1-B-A2 where A1==A2]
        # NOT counting atoms in 1st cn layer as 2nd NN's
        with open(dump_file,'r') as neighbor_raw:
            for lc,lines in enumerate(neighbor_raw):
                if lc >= 9:
                    n_center_atom = int(lines.split()[1])
                    center_atom = type_table[n_center_atom]
                    n_coord_atom_1 = int(lines.split()[2])
                    coord_atom_1 = type_table[n_coord_atom_1]
                    corrected = False
                    if coord_atom_1 != 0:
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
        with open(output_file,'w') as stat_table:
            stat_table.write(
        '''======================================================
3-Atom Distribution Analysis. 
------------------------------------------------------
Top-Left Cornor = Center Atom 
Vertical increase (rows) = 1st Coordination Atom 
Horizontal increase (columns) = 2nd Coordination Atom
Contents = Percenntage of [A-B-C] 
======================================================\n\n\n''')
            
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
                        if two_stat3[ij] == 0 or pair_stat[ijk] == 0:
                            if two_stat3[ij] == 0:
                                value_write = "-\t"  # replace zeros by dashes
                            else:
                                value_write = "{:.6f}".format(0) # keep zeros
                        else:
                            value_write = "{:.6f}".\
                                format(round(pair_stat[ijk]/two_stat3[ij]*100*percent_sum[ij],6))
                        if coord_atom_2 != 'O':
                            content_line += value_write+'\t'
                        else:
                            content_line += value_write+'\n'
                    stat_table.write(content_line)
                sum_line = '\n\n'
                stat_table.write(sum_line)

os.makedirs('./'+folder_of_stat_files)       
os.system('mv *.tab ./'+folder_of_stat_files)
        