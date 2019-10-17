#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  4 00:29:20 2018

@author: Yacong
"""

import glob,os
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

ref_file = '3atom_all0.ref.tab'
# ref_file = '3atom_probabilistic.ref.tab'
# ref_file = '3atom_stat.ref.tab'
stat_file_head = '3atom_stat.'
path_to_3atom_stat_files = '/Users/Yacong/Dropbox/Caltech/PA/01-MD_MC/03-DiAn/01-npt/1.5GPa/voronoi_results/connected_1.5GPa_0_0.05_threshold_0_dt_1000/'
# path_to_3atom_stat_files = './5GPa_0-0.05_threshold_0.1_/3atom_stat/'
name_of_plot = '1.5GPa_all0_threshold_0_all1'

os.chdir(path_to_3atom_stat_files)
stat_file_list = glob.glob(stat_file_head+'*')
stat_file_list.remove('3atom_stat.ref.tab')
# stat_file_list.remove(ref_file)
n_frame = len(stat_file_list)

ref_stat  = {222: 0,\
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

weighs = {\
    222 :   1   ,\
    223 :   1   ,\
    224 :   1   ,\
    225 :   1   ,\
    226 :   1   ,\
    232 :   1   ,\
    233 :   1   ,\
    234 :   1   ,\
    235 :   1   ,\
    236 :   1   ,\
    242 :   1   ,\
    243 :   1   ,\
    244 :   1   ,\
    245 :   1   ,\
    246 :   1   ,\
    252 :   1   ,\
    253 :   1   ,\
    254 :   1   ,\
    255 :   1   ,\
    256 :   1   ,\
    262 :   1   ,\
    263 :   1   ,\
    264 :   1   ,\
    265 :   1   ,\
    266 :   1   ,\
    322 :   1   ,\
    323 :   1   ,\
    324 :   1   ,\
    325 :   1   ,\
    326 :   1   ,\
    332 :   1   ,\
    333 :   1   ,\
    334 :   1   ,\
    335 :   1   ,\
    336 :   1   ,\
    342 :   1   ,\
    343 :   1   ,\
    344 :   1   ,\
    345 :   1   ,\
    346 :   1   ,\
    352 :   1   ,\
    353 :   1   ,\
    354 :   1   ,\
    355 :   1   ,\
    356 :   1   ,\
    362 :   1   ,\
    363 :   1   ,\
    364 :   1   ,\
    365 :   1   ,\
    366 :   1   ,\
    422 :   1   ,\
    423 :   1   ,\
    424 :   1   ,\
    425 :   1   ,\
    426 :   1   ,\
    432 :   1   ,\
    433 :   1   ,\
    434 :   1   ,\
    435 :   1   ,\
    436 :   1   ,\
    442 :   1   ,\
    443 :   1   ,\
    444 :   1   ,\
    445 :   1   ,\
    446 :   1   ,\
    452 :   1   ,\
    453 :   1   ,\
    454 :   1   ,\
    455 :   1   ,\
    456 :   1   ,\
    462 :   1   ,\
    463 :   1   ,\
    464 :   1   ,\
    465 :   1   ,\
    466 :   1   ,\
    522 :   1   ,\
    523 :   1   ,\
    524 :   1   ,\
    525 :   1   ,\
    526 :   1   ,\
    532 :   1   ,\
    533 :   1   ,\
    534 :   1   ,\
    535 :   1   ,\
    536 :   1   ,\
    542 :   1   ,\
    543 :   1   ,\
    544 :   1   ,\
    545 :   1   ,\
    546 :   1   ,\
    552 :   1   ,\
    553 :   1   ,\
    554 :   1   ,\
    555 :   1   ,\
    556 :   1   ,\
    562 :   1   ,\
    563 :   1   ,\
    564 :   1   ,\
    565 :   1   ,\
    566 :   1   ,\
    622 :   1   ,\
    623 :   1   ,\
    624 :   1   ,\
    625 :   1   ,\
    626 :   1   ,\
    632 :   1   ,\
    633 :   1   ,\
    634 :   1   ,\
    635 :   1   ,\
    636 :   1   ,\
    642 :   1   ,\
    643 :   1   ,\
    644 :   1   ,\
    645 :   1   ,\
    646 :   1   ,\
    652 :   1   ,\
    653 :   1   ,\
    654 :   1   ,\
    655 :   1   ,\
    656 :   1   ,\
    662 :   1   ,\
    663 :   1   ,\
    664 :   1   ,\
    665 :   1   ,\
    666 :   1   }

timestep_edist = np.zeros([n_frame,2])

with open(ref_file,'r') as stat_individual:
    for lc,lines in enumerate(stat_individual):
        if lc == 12:
            fields = lines.split()
            ref_stat[222] = float(fields[2])
            ref_stat[223] = float(fields[3])
            ref_stat[224] = float(fields[4])
            ref_stat[225] = float(fields[5])
            ref_stat[226] = float(fields[6])
        elif lc == 13:
            fields = lines.split()
            ref_stat[232] = float(fields[2])
            ref_stat[233] = float(fields[3])
            ref_stat[234] = float(fields[4])
            ref_stat[235] = float(fields[5])
            ref_stat[236] = float(fields[6])
        elif lc == 14:
            fields = lines.split()
            ref_stat[242] = float(fields[2])
            ref_stat[243] = float(fields[3])
            ref_stat[244] = float(fields[4])
            ref_stat[245] = float(fields[5])
            ref_stat[246] = float(fields[6])
        elif lc == 15:
            fields = lines.split()
            ref_stat[252] = float(fields[2])
            ref_stat[253] = float(fields[3])
            ref_stat[254] = float(fields[4])
            ref_stat[255] = float(fields[5])
            ref_stat[256] = float(fields[6])
        elif lc == 16:
            fields = lines.split()
            ref_stat[262] = float(fields[2])
            ref_stat[263] = float(fields[3])
            ref_stat[264] = float(fields[4])
            ref_stat[265] = float(fields[5])
            ref_stat[266] = float(fields[6])
        elif lc == 21:
            fields = lines.split()
            ref_stat[322] = float(fields[2])
            ref_stat[323] = float(fields[3])
            ref_stat[324] = float(fields[4])
            ref_stat[325] = float(fields[5])
            ref_stat[326] = float(fields[6])
        elif lc == 22:
            fields = lines.split()
            ref_stat[332] = float(fields[2])
            ref_stat[333] = float(fields[3])
            ref_stat[334] = float(fields[4])
            ref_stat[335] = float(fields[5])
            ref_stat[336] = float(fields[6])
        elif lc == 23:
            fields = lines.split()
            ref_stat[342] = float(fields[2])
            ref_stat[343] = float(fields[3])
            ref_stat[344] = float(fields[4])
            ref_stat[345] = float(fields[5])
            ref_stat[346] = float(fields[6])
        elif lc == 24:
            fields = lines.split()
            ref_stat[352] = float(fields[2])
            ref_stat[353] = float(fields[3])
            ref_stat[354] = float(fields[4])
            ref_stat[355] = float(fields[5])
            ref_stat[356] = float(fields[6])
        elif lc == 25:
            fields = lines.split()
            ref_stat[362] = float(fields[2])
            ref_stat[363] = float(fields[3])
            ref_stat[364] = float(fields[4])
            ref_stat[365] = float(fields[5])
            ref_stat[366] = float(fields[6])
        elif lc == 30:
            fields = fields = lines.split()
            ref_stat[422] = float(fields[2])
            ref_stat[423] = float(fields[3])
            ref_stat[424] = float(fields[4])
            ref_stat[425] = float(fields[5])
            ref_stat[426] = float(fields[6])
        elif lc == 31:
            fields = fields = lines.split()
            ref_stat[432] = float(fields[2])
            ref_stat[433] = float(fields[3])
            ref_stat[434] = float(fields[4])
            ref_stat[435] = float(fields[5])
            ref_stat[436] = float(fields[6])
        elif lc == 32:
            fields = fields = lines.split()
            ref_stat[442] = float(fields[2])
            ref_stat[443] = float(fields[3])
            ref_stat[444] = float(fields[4])
            ref_stat[445] = float(fields[5])
            ref_stat[446] = float(fields[6])
        elif lc == 33:
            fields = fields = lines.split()
            ref_stat[452] = float(fields[2])
            ref_stat[453] = float(fields[3])
            ref_stat[454] = float(fields[4])
            ref_stat[455] = float(fields[5])
            ref_stat[456] = float(fields[6])
        elif lc == 34:
            fields = fields = lines.split()
            ref_stat[462] = float(fields[2])
            ref_stat[463] = float(fields[3])
            ref_stat[464] = float(fields[4])
            ref_stat[465] = float(fields[5])
            ref_stat[466] = float(fields[6])
        elif lc == 39:
            fields = fields = lines.split()
            ref_stat[522] = float(fields[2])
            ref_stat[523] = float(fields[3])
            ref_stat[524] = float(fields[4])
            ref_stat[525] = float(fields[5])
            ref_stat[526] = float(fields[6])
        elif lc == 40:
            fields = fields = lines.split()
            ref_stat[532] = float(fields[2])
            ref_stat[533] = float(fields[3])
            ref_stat[534] = float(fields[4])
            ref_stat[535] = float(fields[5])
            ref_stat[536] = float(fields[6])
        elif lc == 41:
            fields = fields = lines.split()
            ref_stat[542] = float(fields[2])
            ref_stat[543] = float(fields[3])
            ref_stat[544] = float(fields[4])
            ref_stat[545] = float(fields[5])
            ref_stat[546] = float(fields[6])
        elif lc == 42:
            fields = fields = lines.split()
            ref_stat[552] = float(fields[2])
            ref_stat[553] = float(fields[3])
            ref_stat[554] = float(fields[4])
            ref_stat[555] = float(fields[5])
            ref_stat[556] = float(fields[6])
        elif lc == 43:
            fields = fields = lines.split()
            ref_stat[562] = float(fields[2])
            ref_stat[563] = float(fields[3])
            ref_stat[564] = float(fields[4])
            ref_stat[565] = float(fields[5])
            ref_stat[566] = float(fields[6])
        elif lc == 48:
            fields = fields = lines.split()
            ref_stat[622] = float(fields[2])
            ref_stat[623] = float(fields[3])
            ref_stat[624] = float(fields[4])
            ref_stat[625] = float(fields[5])
            ref_stat[626] = float(fields[6])
        elif lc == 49:
            fields = fields = lines.split()
            ref_stat[632] = float(fields[2])
            ref_stat[633] = float(fields[3])
            ref_stat[634] = float(fields[4])
            ref_stat[635] = float(fields[5])
            ref_stat[636] = float(fields[6])
        elif lc == 50:
            fields = fields = lines.split()
            ref_stat[642] = float(fields[2])
            ref_stat[643] = float(fields[3])
            ref_stat[644] = float(fields[4])
            ref_stat[645] = float(fields[5])
            ref_stat[646] = float(fields[6])
        elif lc == 51:
            fields = fields = lines.split()
            ref_stat[652] = float(fields[2])
            ref_stat[653] = float(fields[3])
            ref_stat[654] = float(fields[4])
            ref_stat[655] = float(fields[5])
            ref_stat[656] = float(fields[6])
        elif lc == 52:
            fields = fields = lines.split()
            ref_stat[662] = float(fields[2])
            ref_stat[663] = float(fields[3])
            ref_stat[664] = float(fields[4])
            ref_stat[665] = float(fields[5])
            ref_stat[666] = float(fields[6])

for frame_count,stat_file in enumerate(stat_file_list):
    stamp = stat_file.split('.')[1]
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
    timestep_edist[frame_count,0] = int(stamp)
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
        for center_atom in range(2,7):
            for cn_1 in range(2,7):
                for cn_2 in range(2,7):
                    ijk = 100*center_atom+10*cn_1+cn_2
                    timestep_edist[frame_count,1] += pow((pair_stat[ijk] - ref_stat[ijk])*weighs[ijk],2)
timestep_edist=timestep_edist[timestep_edist[:,0].argsort()]

# plot distance to reference - time
edist_t_fig = plt.figure(name_of_plot)
plt.xlabel('t/fs')
plt.ylabel('Euclidean Distance')
plt.title('2NN - time')
plt.plot(timestep_edist[:,0],timestep_edist[:,-1],'b-',\
                marker='o',markersize=5)
#         ax = log_fig.gca()
#         ax.set_xlim([0,10])
#         ax.set_ylim([0,3])
#         ax.set_xticks(np.arange(0,11))
#         ax.set_yticks(np.arange(0,3))
plt.grid()
plt.show()
#        plt.savefig('edist')