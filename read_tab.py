#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 16 20:50:20 2018

@author: Yacong
"""
from initialize_dict import initialize_dict

def read_tab(stat_file):
    pair_stat = initialize_dict('pair_stat')
    with open(stat_file,'r') as stat_individual:
        for lc,lines in enumerate(stat_individual):
            if lc == 12:
                fields = lines.split()
                pair_stat[222] = float(fields[2])
                pair_stat[223] = float(fields[3])
                pair_stat[224] = float(fields[4])
                pair_stat[225] = float(fields[5])
                pair_stat[226] = float(fields[6])
            elif lc == 13:
                fields = lines.split()
                pair_stat[232] = float(fields[2])
                pair_stat[233] = float(fields[3])
                pair_stat[234] = float(fields[4])
                pair_stat[235] = float(fields[5])
                pair_stat[236] = float(fields[6])
            elif lc == 14:
                fields = lines.split()
                pair_stat[242] = float(fields[2])
                pair_stat[243] = float(fields[3])
                pair_stat[244] = float(fields[4])
                pair_stat[245] = float(fields[5])
                pair_stat[246] = float(fields[6])
            elif lc == 15:
                fields = lines.split()
                pair_stat[252] = float(fields[2])
                pair_stat[253] = float(fields[3])
                pair_stat[254] = float(fields[4])
                pair_stat[255] = float(fields[5])
                pair_stat[256] = float(fields[6])
            elif lc == 16:
                fields = lines.split()
                pair_stat[262] = float(fields[2])
                pair_stat[263] = float(fields[3])
                pair_stat[264] = float(fields[4])
                pair_stat[265] = float(fields[5])
                pair_stat[266] = float(fields[6])
            elif lc == 21:
                fields = lines.split()
                pair_stat[322] = float(fields[2])
                pair_stat[323] = float(fields[3])
                pair_stat[324] = float(fields[4])
                pair_stat[325] = float(fields[5])
                pair_stat[326] = float(fields[6])
            elif lc == 22:
                fields = lines.split()
                pair_stat[332] = float(fields[2])
                pair_stat[333] = float(fields[3])
                pair_stat[334] = float(fields[4])
                pair_stat[335] = float(fields[5])
                pair_stat[336] = float(fields[6])
            elif lc == 23:
                fields = lines.split()
                pair_stat[342] = float(fields[2])
                pair_stat[343] = float(fields[3])
                pair_stat[344] = float(fields[4])
                pair_stat[345] = float(fields[5])
                pair_stat[346] = float(fields[6])
            elif lc == 24:
                fields = lines.split()
                pair_stat[352] = float(fields[2])
                pair_stat[353] = float(fields[3])
                pair_stat[354] = float(fields[4])
                pair_stat[355] = float(fields[5])
                pair_stat[356] = float(fields[6])
            elif lc == 25:
                fields = lines.split()
                pair_stat[362] = float(fields[2])
                pair_stat[363] = float(fields[3])
                pair_stat[364] = float(fields[4])
                pair_stat[365] = float(fields[5])
                pair_stat[366] = float(fields[6])
            elif lc == 30:
                fields = fields = lines.split()
                pair_stat[422] = float(fields[2])
                pair_stat[423] = float(fields[3])
                pair_stat[424] = float(fields[4])
                pair_stat[425] = float(fields[5])
                pair_stat[426] = float(fields[6])
            elif lc == 31:
                fields = fields = lines.split()
                pair_stat[432] = float(fields[2])
                pair_stat[433] = float(fields[3])
                pair_stat[434] = float(fields[4])
                pair_stat[435] = float(fields[5])
                pair_stat[436] = float(fields[6])
            elif lc == 32:
                fields = fields = lines.split()
                pair_stat[442] = float(fields[2])
                pair_stat[443] = float(fields[3])
                pair_stat[444] = float(fields[4])
                pair_stat[445] = float(fields[5])
                pair_stat[446] = float(fields[6])
            elif lc == 33:
                fields = fields = lines.split()
                pair_stat[452] = float(fields[2])
                pair_stat[453] = float(fields[3])
                pair_stat[454] = float(fields[4])
                pair_stat[455] = float(fields[5])
                pair_stat[456] = float(fields[6])
            elif lc == 34:
                fields = fields = lines.split()
                pair_stat[462] = float(fields[2])
                pair_stat[463] = float(fields[3])
                pair_stat[464] = float(fields[4])
                pair_stat[465] = float(fields[5])
                pair_stat[466] = float(fields[6])
            elif lc == 39:
                fields = fields = lines.split()
                pair_stat[522] = float(fields[2])
                pair_stat[523] = float(fields[3])
                pair_stat[524] = float(fields[4])
                pair_stat[525] = float(fields[5])
                pair_stat[526] = float(fields[6])
            elif lc == 40:
                fields = fields = lines.split()
                pair_stat[532] = float(fields[2])
                pair_stat[533] = float(fields[3])
                pair_stat[534] = float(fields[4])
                pair_stat[535] = float(fields[5])
                pair_stat[536] = float(fields[6])
            elif lc == 41:
                fields = fields = lines.split()
                pair_stat[542] = float(fields[2])
                pair_stat[543] = float(fields[3])
                pair_stat[544] = float(fields[4])
                pair_stat[545] = float(fields[5])
                pair_stat[546] = float(fields[6])
            elif lc == 42:
                fields = fields = lines.split()
                pair_stat[552] = float(fields[2])
                pair_stat[553] = float(fields[3])
                pair_stat[554] = float(fields[4])
                pair_stat[555] = float(fields[5])
                pair_stat[556] = float(fields[6])
            elif lc == 43:
                fields = fields = lines.split()
                pair_stat[562] = float(fields[2])
                pair_stat[563] = float(fields[3])
                pair_stat[564] = float(fields[4])
                pair_stat[565] = float(fields[5])
                pair_stat[566] = float(fields[6])
            elif lc == 48:
                fields = fields = lines.split()
                pair_stat[622] = float(fields[2])
                pair_stat[623] = float(fields[3])
                pair_stat[624] = float(fields[4])
                pair_stat[625] = float(fields[5])
                pair_stat[626] = float(fields[6])
            elif lc == 49:
                fields = fields = lines.split()
                pair_stat[632] = float(fields[2])
                pair_stat[633] = float(fields[3])
                pair_stat[634] = float(fields[4])
                pair_stat[635] = float(fields[5])
                pair_stat[636] = float(fields[6])
            elif lc == 50:
                fields = fields = lines.split()
                pair_stat[642] = float(fields[2])
                pair_stat[643] = float(fields[3])
                pair_stat[644] = float(fields[4])
                pair_stat[645] = float(fields[5])
                pair_stat[646] = float(fields[6])
            elif lc == 51:
                fields = fields = lines.split()
                pair_stat[652] = float(fields[2])
                pair_stat[653] = float(fields[3])
                pair_stat[654] = float(fields[4])
                pair_stat[655] = float(fields[5])
                pair_stat[656] = float(fields[6])
            elif lc == 52:
                fields = fields = lines.split()
                pair_stat[662] = float(fields[2])
                pair_stat[663] = float(fields[3])
                pair_stat[664] = float(fields[4])
                pair_stat[665] = float(fields[5])
                pair_stat[666] = float(fields[6])
    return pair_stat