#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 29 11:08:45 2018

@author: Yacong
"""

def make_pair_dict(dump_file):
    # create 2-pair dictionary (pair_dict: id of each atom in AB pairs)
    pair_dict = {}
    with open(dump_file,'r') as neighbor_raw:
        for lc,lines in enumerate(neighbor_raw):
            if lc >= 9:
                id_center_atom = int(lines.split()[1])
                id_coord_atom = int(lines.split()[2])
                if id_coord_atom != 0:
                    if id_center_atom in pair_dict:
                        pair_dict[id_center_atom] = pair_dict[id_center_atom] + [id_coord_atom]
                    else:
                        pair_dict[id_center_atom] = [id_coord_atom]
    return pair_dict

def dl_per_atom(dump_file):
    """
    create per-atom double-layer dict of lists using a single frame
    """
    pair_dict = make_pair_dict(dump_file)
    # create double-layer dictionary (dl_dict: id of each atom in B and C layers)
    dl_dict = {}
    for id_center_atom in pair_dict:
        layer_1 = pair_dict[id_center_atom]
        dl_dict[id_center_atom] = [layer_1,[]]
        for id_coord_atom_1 in layer_1:
            for id_coord_atom_2 in pair_dict[id_coord_atom_1]:
                if (id_coord_atom_2 not in layer_1) and \
                    (id_coord_atom_2 not in dl_dict[id_center_atom][1]) and \
                    (id_coord_atom_2 != id_center_atom):
                    dl_dict[id_center_atom][1] = dl_dict[id_center_atom][1] + [id_coord_atom_2]
    return dl_dict

def multi_layer_dict_per_atom(n_layer,dump_file):
    """
    create per-atom multi-layer dict of lists using a single frame
    """
    if n_layer >= 1:
        pair_dict = make_pair_dict(dump_file)
        # create multi-layer dictionary (ml_dict: id of each atom in 1st, 2nd, ..., n-th layers)
        ml_dict = {}
        for id_center_atom in pair_dict:
            layer_1 = pair_dict[id_center_atom]
            ml_dict[id_center_atom] = [layer_1]
        n_layer -= 1
        n_current_layer = 1
        n_atom = sorted(ml_dict.keys())[-1]
        while(n_layer>0):
            for id_center_atom in range(1,n_atom+1):
                current_layer = ml_dict[id_center_atom][n_current_layer-1]
                if n_current_layer == 1:
                    previous_layer = [id_center_atom]
                else:
                    previous_layer = ml_dict[id_center_atom][n_current_layer-2]
                next_layer = []
                for id_atom_current in current_layer:
                    for id_atom_next in pair_dict[id_atom_current]:
                        if (id_atom_next not in current_layer) and \
                                (id_atom_next not in next_layer) and \
                                (id_atom_next not in previous_layer):
                            next_layer += [id_atom_next]
                ml_dict[id_center_atom] += [next_layer]
            n_layer -= 1
            n_current_layer += 1
        return ml_dict
    else:
        print('Unknown option for initialize_dict!')
        raise ValueError('invalid number of layers: %s' % str(n))

def multi_layer_q_per_atom(dl_dict,type_table,n_layer=2):
    """“
    output: 
        q_per_atom=np.array([q_layer_1, q_layer_2, q_l1+l2], ...)
    Note:
        output array does not contain id and charge of center atom!
    ”“"""
    import numpy as np
    type_q_table = {1:1,2:2,3:2,4:3,5:4,6:-2}
    n_atom = sorted(dl_dict.keys())[-1]
    # per-atom charge. q_per_atom[id_center_atom - 1] = [q(layer_1）, q(layer_2), q(l1+l2)]
    q_per_atom = np.zeros([n_atom,n_layer+1])
    for id_center_atom_m1 in range(n_atom):
        id_center_atom = id_center_atom_m1 + 1
        for layer_m1 in range(n_layer):
            for id_coord_atom in dl_dict[id_center_atom][layer_m1]:
                q_per_atom[id_center_atom_m1][layer_m1] += type_q_table[type_table[id_coord_atom]]
            q_per_atom[id_center_atom_m1][-1] += q_per_atom[id_center_atom_m1][layer_m1]
    return q_per_atom

def multi_layer_q_by_type(q_per_atom,type_table):
    """
    return:
        q_by_type=numpy_array([q0,q1,...qn,sum(q0-qn)],[],...)
    Note:
        output array contains id of center atom!
        sum column in q_by_type includes charge of center atom
        if count_atom is 0 for an element, its row is removed
    """
    import numpy as np
    n_layer = len(q_per_atom[0]) - 1
    type_q_table = {1:1,2:2,3:2,4:3,5:4,6:-2}
    count_by_type = {1:0,2:0,3:0,4:0,5:0,6:0}
    q_by_type = np.zeros([6,n_layer+3])
    q_by_type[:,0]=np.arange(1,7)
    n_total_atom = len(q_per_atom)
    for id_center_atom in range(1,n_total_atom+1):
        center_type = type_table[id_center_atom]
        count_by_type[center_type] += 1
        q_by_type[center_type-1,1] += type_q_table[center_type]
        for n_current_layer_m1 in range(n_layer+1):
            q_by_type[center_type-1,n_current_layer_m1+2] += \
                q_per_atom[id_center_atom-1,n_current_layer_m1]
    for atom_type in range(1,len(count_by_type)+1):
        if np.dot(q_by_type[atom_type-1,1:],q_by_type[atom_type-1,1:]) != 0:
            q_by_type[atom_type-1,1:] /= count_by_type[atom_type]
    return q_by_type

# def fast_q_by_type(dump_file,type_table,n_layer=2):
#     """
#     Notes:
#         this is not fast... 
#         beucase Nth_layer_dict requires dict of N-1th and N-2th layer
#     """
#     import numpy as np
#     type_q_table = {1:1,2:2,3:2,4:3,5:4,6:-2}
#     count_by_type = {1:0,2:0,3:0,4:0,5:0,6:0}
#     q_by_type = np.zeros([6,n_layer+3])
#     q_by_type[:,0]=np.arange(1,7)
#     if n_layer >= 1:
#         pair_dict = make_pair_dict(dump_file)
#         n_total_atom = len(pair_dict)
#         n_current_layer = 1
#         while n_current_layer < n_layer:
#             layer_dict = {}
#     else:
#         print('Unknown option for initialize_dict!')
#         raise ValueError('invalid number of layers: %s' % str(n))

#     # below need edit....
#     for id_center_atom in range(1,n_total_atom+1):
#         center_type = type_table[id_center_atom]
#         count_by_type[center_type] += 1
#         q_by_type[center_type-1,1] += type_q_table[center_type]
#         for n_current_layer_m1 in range(n_layer+1):
#             q_by_type[center_type-1,n_current_layer_m1+2] += \
#                 q_per_atom[id_center_atom-1,n_current_layer_m1]
#     for atom_type in range(1,len(count_by_type)+1):
#         if np.dot(q_by_type[atom_type-1,1:],q_by_type[atom_type-1,1:]) != 0:
#             q_by_type[atom_type-1,1:] /= count_by_type[atom_type]
#     return q_by_type

def id_to_types(dl_dict,type_lookup_file):
    import three_atom_stat
    dl_element = {}
    type_element_table = {1:'Na',2:'Mg',3:'Ca',4:'Al',5:'Si',6:'O'}
    type_table = three_atom_stat.create_type_table(type_lookup_file)
    n_atom = sorted(dl_dict.keys())[-1]
    for id_center_atom_m1 in range(n_atom):
        id_center_atom = id_center_atom_m1 + 1
        center_element = type_element_table[type_table[id_center_atom]]
        dl_element[str(id_center_atom)+'_'+center_element] = [[],[]]
        for id_coord_atom_1 in dl_dict[id_center_atom][0]:
            cn1_element = type_element_table[type_table[id_coord_atom_1]]
            dl_element[str(id_center_atom)+'_'+center_element][0] = \
                dl_element[str(id_center_atom)+'_'+center_element][0] + [str(id_coord_atom_1)+'_'+cn1_element]
        for id_coord_atom_2 in dl_dict[id_center_atom][1]:
            cn2_element = type_element_table[type_table[id_coord_atom_2]]
            dl_element[str(id_center_atom)+'_'+center_element][1] = \
                dl_element[str(id_center_atom)+'_'+center_element][1] + [str(id_coord_atom_2)+'_'+cn2_element]
    return dl_element

def plot_layer_q_by_type(q_by_type,n_layer=2):
    import numpy as np
    import matplotlib.pyplot as plt
    type_element={1:'Na',2:'Mg',3:'Ca',4:'Al',5:'Si',6:'O'}
    x=np.arange(1,n_layer+1)
    for atom_type in range(2,7):
        y=q_by_type[atom_type-1][1:-2]
        name_of_plot=type_element[atom_type]+'_layer_q'
        edist_t_fig = plt.figure(name_of_plot)
        plt.xlabel('Coordination Layer')
        plt.ylabel('Total Charge in Layer (averaged)')
        plt.title(type_element[atom_type]+': Charge in Coordination Layers')
        plt.plot(x,y,'b-',marker='o',markersize=5)
        # ax = log_fig.gca()
        # ax.set_xlim([0,10])
        # ax.set_ylim([0,3])
        # ax.set_xticks(np.arange(0,11))
        # ax.set_yticks(np.arange(0,3))
        plt.grid()
        # plt.savefig('../'+name_of_plot)
        plt.show()
    
def t_q_by_type(splitted_dump_folder_name,type_table,n_layer=2,merge_seg=False,save_to_file=False):
    """
    Return:
        q_t[element_type-1]=np.array([[timestep=ini,q_l0,q_l1,...,q_lN, q_sum],
                                      [timestep=1st,q_l0,q_l1,...,q_lN, q_sum],
                                      ...
                                      [timestep=end,q_l0,q_l1,...,q_lN, q_sum]])
    """
    import os
    import glob
    import numpy as np
    dump_file_head = 'dump.'
    path_to_splitted_dump = './'+splitted_dump_folder_name
    os.chdir(path_to_splitted_dump)
    if merge_seg == False:
        dump_file_list = glob.glob(dump_file_head+'*')
    elif merge_seg == True:
        import re
        traj_dirs = []
        dump_file_list = []
        all_dirs = os.listdir('./')
        for folder_name in all_dirs:
            if re.search("[A-Za-z]", folder_name) == None:
                traj_dirs.append(folder_name)
        for traj_dir in traj_dirs:
            for file in os.listdir(traj_dir):
                if file.startswith(dump_file_head):
                    dump_file_list += [os.path.join(traj_dir,file)]
        # return dump_file_list
    q_t=[[],[],[],[],[],[]]
    # q_t_Na=q_t_Mg=q_t_Ca=q_t_Al=q_t_Si=q_t_O=np.asarray([])
    for dump_file in dump_file_list:
        timestep = int(dump_file.split('.')[-1])
        ml_dict = multi_layer_dict_per_atom(n_layer,dump_file)
        q_per_atom = multi_layer_q_per_atom(ml_dict,type_table,n_layer)
        q_by_type = multi_layer_q_by_type(q_per_atom,type_table)
        for element_type in range(1,7):
            if q_by_type[element_type-1][-1] != 0:
                new_entry = np.append(np.asarray([timestep]),\
                    q_by_type[element_type-1][1:])
                if len(q_t[element_type-1])==0:
                    q_t[element_type-1] = np.asarray([new_entry])
                else:
                    q_t[element_type-1] = np.append(q_t[element_type-1],\
                        np.asarray([new_entry]),axis=0)
    for type_m1 in range(6):
        if len(q_t[type_m1]) != 0:
            q_t[type_m1]=q_t[type_m1][q_t[type_m1][:,0].argsort()]
    if save_to_file:
        type_element={1:'Na',2:'Mg',3:'Ca',4:'Al',5:'Si',6:'O'}
        for type_m1 in range(6):
            if len(q_t[type_m1]) != 0:
                center_element = type_element[type_m1+1]
                delimiter_format='%d'+'\t%.8e'*(2+n_layer)
                tab_header = 'timestep\t'
                for i in range(1+n_layer):
                    tab_header += 'layer_'+str(i)+'\t'
                tab_header += 'sum'
                np.savetxt('./'+center_element+'_q-t.txt',q_t[type_m1],\
                    fmt=delimiter_format,\
                    header=tab_header)
    return q_t

def plot_q_t(q_t,n_layer,option='lines'):
    import matplotlib.pyplot as plt
    import numpy as np
    type_element={1:'Na',2:'Mg',3:'Ca',4:'Al',5:'Si',6:'O'}
    if option == 'stack':
        for type_m1 in range(6):
            if len(q_t[type_m1]) != 0:
                name_of_plot = type_element[type_m1+1]+'_q-t'
                labels=[]
                x=q_t[type_m1][:,0]
                y=np.asarray([])
                for layer_walker in range(1,n_layer+2):
                    if len(y) == 0:
                        y = np.asarray(q_t[type_m1][:,layer_walker])
                        labels = ['Center']
                    else:
                        y = np.vstack([y,q_t[type_m1][:,layer_walker]])
                        labels += ['Layer_'+str(layer_walker-1)]
                q_t_fig = plt.figure(name_of_plot)
                plt.xlabel('t / fs')
                plt.ylabel('Charge / e')
                plt.title('q(layer) - time: '+type_element[type_m1+1])
                plt.stackplot(x, y,labels=labels)
                plt.show()
    elif option == 'lines':
        for type_m1 in range(6):
            if len(q_t[type_m1]) != 0:
                name_of_plot = type_element[type_m1+1]+'_q-t'
                labels=[]
                x=q_t[type_m1][:,0]
                y=np.asarray([])
                for layer_walker in range(1,n_layer+2):
                    # print('ha '+str(layer_walker))
                    if len(y) == 0:
                        y = np.asarray([q_t[type_m1][:,layer_walker]])
                    else:
                        # print(layer_walker)
                        y = np.append(y,[q_t[type_m1][:,layer_walker]],axis=0)
                        labels += ['Layer_'+str(layer_walker-1)]
                q_t_fig = plt.figure(name_of_plot)
                for layer_walker in range(1,len(y)):  
                    plt.plot(x,y[layer_walker])
                    plt.legend(labels)  
                plt.xlabel('t / fs')
                plt.ylabel('Charge / e')
                plt.title('q(layer) - time: '+type_element[type_m1+1])  
                plt.show()
    else:
        print('Unknown option for plot_q_t!')
        raise ValueError('invalid value: %s' % option)
                
def avg_t_q_by_type(splitted_dump_folder_name,type_table):
    sth


import three_atom_stat
type_lookup_file='./id-type.tab'
type_table = three_atom_stat.create_type_table(type_lookup_file)
n_layer=2
# pair_dict=make_pair_dict('./dump.1041000')
# dl_dict=dl_per_atom('./dump.1041000')
# dl_dict2=multi_layer_dict_per_atom(n_layer,'./dump.1050000')
#dl_dict2=multi_layer_dict_per_atom(2,'./dump.debug')
# q_per_atom = multi_layer_q_per_atom(dl_dict2,type_table,n_layer)
#dl_element = id_to_types(dl_dict,'./id-type.tab')
# q_by_type = multi_layer_q_by_type(q_per_atom,type_table)
#plot_layer_q_by_type(q_by_type,n_layer)
#q_t=plot_t_q_by_type('1.5GPa_fc_0/0.05-1.05/',type_table,n_layer=2)
q_t=t_q_by_type('25GPa_fc_0/',type_table,n_layer,merge_seg=True,save_to_file=True)
#for type_m1 in range(6):
#    if len(q_t[type_m1]) != 0:
#        plt.plot(q_t[type_m1][:,0],q_t[type_m1][:,2], 'b-',\
#                 q_t[type_m1][:,0],q_t[type_m1][:,3], 'g-',\
#                 q_t[type_m1][:,0],q_t[type_m1][:,4], 'r-')
#        plt.plot(q_t[type_m1][:,0],q_t[type_m1][:,3], 'g-')
plot_q_t(q_t,n_layer,option='lines')