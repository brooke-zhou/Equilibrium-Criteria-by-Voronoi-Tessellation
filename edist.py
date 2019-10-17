#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 16 17:20:20 2018

@author: Yacong
"""

import glob,os
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import read_tab

def connect_all_t():
    import re
    traj_dirs = []
    all_dirs = os.listdir('./')
    for folder_name in all_dirs:
        if re.search("[A-Za-z]", folder_name) == None:
            traj_dirs.append(folder_name)
    os.makedirs('./connected')
    os.chdir('./connected')
    for traj_piece in traj_dirs:
        os.system('cp ../'+traj_piece+'/3atom_stat/3atom_stat.* .')
    return traj_dirs

def plot_edist_t(ref_stat,path_to_3atom_stat_files,save_edist=False,save_option='by_weights',show_plot=True,weighing_vector='adjusted'):
    import read_tab
    name_of_plot='edist'
    os.chdir(path_to_3atom_stat_files)
    stat_file_head = '3atom_stat.'
    stat_file_list = glob.glob(stat_file_head+'*')
    # stat_file_list.remove(ref_file)
    n_frame = len(stat_file_list)

    all_1_weights = {\
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
    adjusted_weights = {\
        262 :   0.8   ,\
        263 :   0.6   ,\
        264 :   0.2   ,\
        265 :   0.2   ,\
        362 :   0.6   ,\
        363 :   0.6   ,\
        364 :   0.7   ,\
        365 :   0.6   ,\
        462 :   0.2   ,\
        463 :   0.7   ,\
        464 :   0.2   ,\
        465 :   0.2   ,\
        562 :   0.2   ,\
        563 :   0.6   ,\
        564 :   0.2   ,\
        565 :   0.8   ,\
        626 :   0.4   ,\
        636 :   0.6   ,\
        646 :   0.0   ,\
        656 :   0.8   }
    if weighing_vector == 'adjusted':
        weights = adjusted_weights
        timestep_edist = np.zeros([n_frame,2+20])
    elif weighing_vector == 'all_1':
        weights = all_1_weights
        timestep_edist = np.zeros([n_frame,2+125])
    else:
        print('Unknown weighing_vector option!')
        raise ValueError('invalid value: %s' % weighing_vector)

    # create edist-t list 
    for frame_count,stat_file in enumerate(stat_file_list):
        stamp = stat_file.split('.')[1]
        timestep_edist[frame_count,0] = int(stamp)
        with open(stat_file,'r') as stat_individual:
            pair_stat = read_tab.read_tab(stat_file)
            if weighing_vector == 'all_1':
                for center_atom in range(2,7):
                    for cn_1 in range(2,7):
                        for cn_2 in range(2,7):
                            ijk = 100*center_atom+10*cn_1+cn_2
                            id_ijk = 25*(center_atom-2)+5*(cn_1-2)+(cn_2-2)+1
                            timestep_edist[frame_count,id_ijk] = pow((pair_stat[ijk] - ref_stat[ijk]),2)
                            timestep_edist[frame_count,-1] += pow((pair_stat[ijk] - ref_stat[ijk]),2)*weights[ijk]
            elif weighing_vector == 'adjusted':
                for center_atom in range(2,6):
                    cn_1 = 6
                    for cn_2 in range(2,6):
                        ijk = 100*center_atom+10*cn_1+cn_2
                        id_ijk = 4*(center_atom-2)+(cn_2-2)+1
                        timestep_edist[frame_count,id_ijk] = pow((pair_stat[ijk] - ref_stat[ijk]),2)
                        timestep_edist[frame_count,-1] += pow((pair_stat[ijk] - ref_stat[ijk]),2)*weights[ijk]
                center_atom = cn_2 = 6
                for cn_1 in range(2,6):
                    ijk = 100*center_atom+10*cn_1+cn_2
                    id_ijk = 15+cn_1
                    timestep_edist[frame_count,id_ijk] = pow((pair_stat[ijk] - ref_stat[ijk]),2)
                    timestep_edist[frame_count,-1] += pow((pair_stat[ijk] - ref_stat[ijk]),2)*weights[ijk]
    timestep_edist=timestep_edist[timestep_edist[:,0].argsort()]

    # plot edist-time
    edist_t_fig = plt.figure(name_of_plot)
    plt.xlabel('t/fs')
    plt.ylabel('Euclidean Distance to Reference Distribution')
    plt.title('2NN - time')
    plt.plot(timestep_edist[:,0],timestep_edist[:,-1],'b-',\
                    marker='o',markersize=0)
    ax = edist_t_fig.gca()
    # ax.set_xlim([0,10])
    # ax.set_xticks(np.arange(0,11))
    # y_min = 40
    # y_max = 100
    # ax.set_ylim([y_min,y_max])
    # ax.set_yticks(np.arange(y_min,y_max,10))
    plt.grid()
    plt.savefig('../'+name_of_plot)
    if show_plot: plt.show()

    # save edist-t as txt
    if save_edist:
        if weighing_vector == 'all_1':
            delimiter_format = ('%d',\
                '%.8e','%.8e','%.8e','%.8e','%.8e',\
                '%.8e','%.8e','%.8e','%.8e','%.8e',\
                '%.8e','%.8e','%.8e','%.8e','%.8e',\
                '%.8e','%.8e','%.8e','%.8e','%.8e',\
                '%.8e','%.8e','%.8e','%.8e','%.8e',\
                '%.8e','%.8e','%.8e','%.8e','%.8e',\
                '%.8e','%.8e','%.8e','%.8e','%.8e',\
                '%.8e','%.8e','%.8e','%.8e','%.8e',\
                '%.8e','%.8e','%.8e','%.8e','%.8e',\
                '%.8e','%.8e','%.8e','%.8e','%.8e',\
                '%.8e','%.8e','%.8e','%.8e','%.8e',\
                '%.8e','%.8e','%.8e','%.8e','%.8e',\
                '%.8e','%.8e','%.8e','%.8e','%.8e',\
                '%.8e','%.8e','%.8e','%.8e','%.8e',\
                '%.8e','%.8e','%.8e','%.8e','%.8e',\
                '%.8e','%.8e','%.8e','%.8e','%.8e',\
                '%.8e','%.8e','%.8e','%.8e','%.8e',\
                '%.8e','%.8e','%.8e','%.8e','%.8e',\
                '%.8e','%.8e','%.8e','%.8e','%.8e',\
                '%.8e','%.8e','%.8e','%.8e','%.8e',\
                '%.8e','%.8e','%.8e','%.8e','%.8e',\
                '%.8e','%.8e','%.8e','%.8e','%.8e',\
                '%.8e','%.8e','%.8e','%.8e','%.8e',\
                '%.8e','%.8e','%.8e','%.8e','%.8e',\
                '%.8e','%.8e','%.8e','%.8e','%.8e',\
                '%.8e')
            tab_header = ("timestep\t" 
                    "MgMgMg\tMgMgCa\tMgMgAl\tMgMgSi\tMgMgO\t"
                    "MgCaMg\tMgCaCa\tMgCaAl\tMgCaSi\tMgCaO\t"
                    "MgAlMg\tMgAlCa\tMgAlAl\tMgAlSi\tMgAlO\t"
                    "MgSiMg\tMgSiCa\tMgSiAl\tMgSiSi\tMgSiO\t"
                    "MgOMg \tMgOCa \tMgOAl \tMgOSi \tMgOO \t"
                    "CaMgMg\tCaMgCa\tCaMgAl\tCaMgSi\tCaMgO\t"
                    "CaCaMg\tCaCaCa\tCaCaAl\tCaCaSi\tCaCaO\t"
                    "CaAlMg\tCaAlCa\tCaAlAl\tCaAlSi\tCaAlO\t"
                    "CaSiMg\tCaSiCa\tCaSiAl\tCaSiSi\tCaSiO\t"
                    "CaOMg \tCaOCa \tCaOAl \tCaOSi \tCaOO \t"
                    "AlMgMg\tAlMgCa\tAlMgAl\tAlMgSi\tAlMgO\t"
                    "AlCaMg\tAlCaCa\tAlCaAl\tAlCaSi\tAlCaO\t"
                    "AlAlMg\tAlAlCa\tAlAlAl\tAlAlSi\tAlAlO\t"
                    "AlSiMg\tAlSiCa\tAlSiAl\tAlSiSi\tAlSiO\t"
                    "AlOMg \tAlOCa \tAlOAl \tAlOSi \tAlOO \t"
                    "SiMgMg\tSiMgCa\tSiMgAl\tSiMgSi\tSiMgO\t"
                    "SiCaMg\tSiCaCa\tSiCaAl\tSiCaSi\tSiCaO\t"
                    "SiAlMg\tSiAlCa\tSiAlAl\tSiAlSi\tSiAlO\t"
                    "SiSiMg\tSiSiCa\tSiSiAl\tSiSiSi\tSiSiO\t"
                    "SiOMg \tSiOCa \tSiOAl \tSiOSi \tSiOO \t"
                    "OMgMg\tOMgCa\tOMgAl\tOMgSi\tOMgO\t"
                    "OCaMg\tOCaCa\tOCaAl\tOCaSi\tOCaO\t"
                    "OAlMg\tOAlCa\tOAlAl\tOAlSi\tOAlO\t"
                    "OSiMg\tOSiCa\tOSiAl\tOSiSi\tOSiO\t"
                    "OOMg \tOOCa \tOOAl \tOOSi \tOOO \t"
                    "edist")
        elif weighing_vector == 'adjusted':
            delimiter_format = ('%d',\
                '%.8e','%.8e','%.8e','%.8e',\
                '%.8e','%.8e','%.8e','%.8e',\
                '%.8e','%.8e','%.8e','%.8e',\
                '%.8e','%.8e','%.8e','%.8e',\
                '%.8e','%.8e','%.8e','%.8e',\
                '%.8e')
            tab_header = ("timestep\t" 
                    "MgOMg \tMgOCa \tMgOAl \tMgOSi \t"
                    "CaOMg \tCaOCa \tCaOAl \tCaOSi \t"
                    "AlOMg \tAlOCa \tAlOAl \tAlOSi \t"
                    "SiOMg \tSiOCa \tSiOAl \tSiOSi \t"
                    "OMgO\tOCaO\tOAlO\tOSiO\tedist")
        np.savetxt('../edist.txt',timestep_edist,\
            fmt=delimiter_format,\
            delimiter='\t',\
            header=tab_header)
   
        # if save_option == 'by_weights':
        #     np.savetxt('../edist.txt',timestep_edist,
        #         fmt=['%d','%.8e'],header='timestep edist')
        # elif save_option == 'one_by_one':
        #     elements
        # else:
        #     element_id = '23456'
        #     elements = {'1':'Na','2':'Mg','3':'Ca','4':'Al','5':'Si','6':'O'}
        #     if (len(save_option) == 3) and \
        #             (save_option[0] in element_id) and \
        #             (save_option[1] in element_id) and \
        #             (save_option[1] in element_id):
        #         output_name = elements[save_option[0]]+\
        #                       elements[save_option[1]]+\
        #                       elements[save_option[2]]+'.txt'
        #         with open(output_name[:-4]+'-t','w') as output:
        #             header = '# timestep\tedist('+output_name[:-4]+')\n'
        #             output.write(header)
        #             for frame_count,stat_file in enumerate(stat_file_list):
        #                 stamp = stat_file.split('.')[1]
        #                 timestep_edist[frame_count,0] = int(stamp)
        #                 with open(stat_file,'r') as stat_individual:
        #                     pair_stat = read_tab.read_tab(stat_file)
        #                     # for center_atom in range(2,7):
        #                     center_atom = save_option[0]
        #                     cn_1 = save_option[1]
        #                     cn_2 = save_option[2]
        #                     ijk = 100*center_atom+10*cn_1+cn_2
        #                     timestep_edist[frame_count,1] += pow((pair_stat[ijk] - ref_stat[ijk])*weighs[ijk],2)
        #             timestep_edist=timestep_edist[timestep_edist[:,0].argsort()]
        #     else:
        #         print('Unknown save_option for plot_edist_t!')
        #         raise ValueError('invalid value: %s' % save_option)

def save_edist(ref_stat,path_to_dump,traj_dirs,option='avg'):
    # save edist of each 3atom_avg (wrt ref)
    if option == 'avg':
        with open('avg_edist.txt','w') as output:
            header = 'time (ns)\tedist\n'
            output.write(header)
            os.chdir(path_to_dump)
            for traj_dir in traj_dirs:
                stat_avg = read_tab.read_tab(traj_dir+'/3atom_stat/3atom_avg.tab')
                edist_value = 0
                # for center_atom in range(2,7):
                for center_atom in range(2,7):
                    for cn_1 in range(2,7):
                        for cn_2 in range(2,7):
                            ijk = 100*center_atom+10*cn_1+cn_2
                            edist_value += pow((stat_avg[ijk] - ref_stat[ijk]),2)
                content_line = traj_dir+'\t'+"{:.3f}".format(edist_value)+'\n'
                output.write(content_line)
    elif option == 'one_by_one':
        elements = {1:'Na',2:'Mg',3:'Ca',4:'Al',5:'Si',6:'O'}
        for traj_dir in traj_dirs:
            with open('./avg_edist.'+traj_dir+'.txt','w') as output:
                header = '3atom_pairs\tedist\n'
                output.write(header)
                os.chdir(path_to_dump)
                stat_avg = read_tab.read_tab(traj_dir+'/3atom_stat/3atom_avg.tab')
                # for center_atom in range(2,7):
                for center_atom in range(2,7):
                    for cn_1 in range(2,7):
                        for cn_2 in range(2,7):
                            ijk = 100*center_atom+10*cn_1+cn_2
                            edist_value = pow((stat_avg[ijk] - ref_stat[ijk]),2)
                            content_line = elements[center_atom] + elements[cn_1] + elements[cn_2]\
                                         +'\t'+"{:.3f}".format(edist_value)+'\n'
                            output.write(content_line)
    else:
        element_id = '23456'
        elements = {'1':'Na','2':'Mg','3':'Ca','4':'Al','5':'Si','6':'O'}
        if (len(option) == 3) and \
                (option[0] in element_id) and \
                (option[1] in element_id) and \
                (option[1] in element_id):
            output_name = elements[option[0]]+'-'+\
                          elements[option[1]]+'-'+\
                          elements[option[2]]+'.txt'
            with open(output_name[:-4],'w') as output:
                header = 'time (ns)\tedist('+output_name[:-4]+')\n'
                output.write(header)
                os.chdir(path_to_dump)
                for traj_dir in traj_dirs:
                    stat_avg = read_tab.read_tab(traj_dir+'/3atom_stat/3atom_avg.tab')
                    center_atom = option[0]
                    cn_1 = option[1]
                    cn_2 = option[2]
                    ijk = 100*center_atom+10*cn_1+cn_2
                    edist_value = pow((stat_avg[ijk] - ref_stat[ijk]),2)
                    content_line = traj_dir+'\t'+"{:.3f}".format(edist_value)+'\n'
                    output.write(content_line)      
        else:
            print('Unknown option for save_avg_edist!')
            raise ValueError('invalid value: %s' % option)

    
