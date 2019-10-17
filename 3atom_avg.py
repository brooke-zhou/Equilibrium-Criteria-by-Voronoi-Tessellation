#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 26 14:40:56 2018

Post-processing for 3atom_stat_.py
To average all the 3atom_stat.xxx.tab files

@author: Yacong
"""

import glob,os

stat_file_head = '3atom_stat.'
output_file_name = '3atom_avg.tab'
# path_to_3atom_stat_files = './debug/'
path_to_3atom_stat_files = './25GPa_1.05-2.05_threshold_0.1_/3atom_stat/'

os.chdir(path_to_3atom_stat_files)
stat_file_list = glob.glob(stat_file_head+'*')
n_frame = len(stat_file_list)

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

for stat_file in stat_file_list:
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

dividing = '-----------------------------------------------------------------\n'
elements = {1:'Na',2:'Mg',3:'Ca',4:'Al',5:'Si',6:'O'}
with open(output_file_name,'w') as output_file:
    header = '''==========================================================
3-Atom Distribution Analysis (averaged over all frames). 
---------------------------------------------------------
Top-Left Cornor = Center Atom 
Vertical increase (rows) = 1st Coordination Atom 
Horizontal increase (columns) = 2nd Coordination Atom
Contents = Percenntage of [A-B-C] 
==========================================================\n\n\n'''
    output_file.write(header)
    for n_center_atom in range(2,7):
        header_line = elements[n_center_atom]+\
        '\t|\tMg\t\t\tCa\t\t\tAl\t\t\tSi\t\t\tO\n'
        output_file.write(header_line)
        output_file.write(dividing)
        for n_coord_atom_1 in range(2,7):
            coord_atom_1 = elements[n_coord_atom_1]
            content_line = coord_atom_1+'\t|\t'
            for n_coord_atom_2 in range(2,7):
                coord_atom_2 = elements[n_coord_atom_2]
                ijk = 100*n_center_atom+10*n_coord_atom_1+n_coord_atom_2
                if pair_stat[ijk] == 0:
                    # value_write = "-\t"  # replace zeros by dashes
                    value_write = "{:.6f}".format(0) # keep zeros
                else:
                    value_write = "{:.6f}".\
                        format(round(pair_stat[ijk]/n_frame,6))
                if coord_atom_2 != 'O':
                    content_line += value_write+'\t'
                else:
                    content_line += value_write+'\n'
            output_file.write(content_line)
        sum_line = '\n\n'
        output_file.write(sum_line)