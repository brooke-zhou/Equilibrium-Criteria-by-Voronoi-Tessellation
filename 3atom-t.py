#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Summarize outputs of 3atom_stat and 
make %-t tables for all elements

Created on Thu Mar 29 18:06:42 2018

@author: Yacong
"""

import glob

stat_file_head = '3atom_stat.'
output_file_name = '3atom-time.txt'

time = []
NaONa = []
NaOMg = []
NaOCa = []
NaOAl = []
NaOSi = []
MgONa = []
MgOMg = []
MgOCa = []
MgOAl = []
MgOSi = []
CaONa = []
CaOMg = []
CaOCa = []
CaOAl = []
CaOSi = []
AlONa = []
AlOMg = []
AlOCa = []
AlOAl = []
AlOSi = []
SiONa = []
SiOMg = []
SiOCa = []
SiOAl = []
SiOSi = []

stat_file_list = glob.glob(stat_file_head+'*')
for stat_file in stat_file_list:
    time += [int(stat_file.split('.')[-2])*1e-6]
    with open(stat_file,'r') as stat:
        for lc,lines in enumerate(stat):
            if lc == 17:
                fields = lines.split()
                NaONa += [float(fields[2])]
                NaOMg += [float(fields[3])]
                NaOCa += [float(fields[4])]
                NaOAl += [float(fields[5])]
                NaOSi += [float(fields[6])]
            elif lc == 27:
                fields = lines.split()
                MgONa += [float(fields[2])]
                MgOMg += [float(fields[3])]
                MgOCa += [float(fields[4])]
                MgOAl += [float(fields[5])]
                MgOSi += [float(fields[6])]
            elif lc == 37:
                fields = lines.split()
                CaONa += [float(fields[2])]
                CaOMg += [float(fields[3])]
                CaOCa += [float(fields[4])]
                CaOAl += [float(fields[5])]
                CaOSi += [float(fields[6])]
            elif lc == 47:
                fields = lines.split()
                AlONa += [float(fields[2])]
                AlOMg += [float(fields[3])]
                AlOCa += [float(fields[4])]
                AlOAl += [float(fields[5])]
                AlOSi += [float(fields[6])]
            elif lc == 57:
                fields = lines.split()
                SiONa += [float(fields[2])]
                SiOMg += [float(fields[3])]
                SiOCa += [float(fields[4])]
                SiOAl += [float(fields[5])]
                SiOSi += [float(fields[6])]
                
with open(output_file_name,'w') as output_file:
    output_file.write('Na-O-Na\n')
    output_file.write('t/ns\t%\n')
    for i in range(len(time)):
        content_line = "{:.3f}".format(time[i])+'\t'+"{:.2f}".format(NaONa[i])+'\n'
        output_file.write(content_line)
        
    output_file.write('\nNa-O-Mg\n')
    output_file.write('times / ns\t%\n')
    for i in range(len(time)):
        content_line = "{:.3f}".format(time[i])+'\t'+"{:.2f}".format(NaOMg[i])+'\n'
        output_file.write(content_line)
        
    output_file.write('\nNa-O-Ca\n')
    output_file.write('times / ns\t%\n')
    for i in range(len(time)):
        content_line = "{:.3f}".format(time[i])+'\t'+"{:.2f}".format(NaOCa[i])+'\n'
        output_file.write(content_line)
    
    output_file.write('\nNa-O-Al\n')
    output_file.write('times / ns\t%\n')
    for i in range(len(time)):
        content_line = "{:.3f}".format(time[i])+'\t'+"{:.2f}".format(NaOAl[i])+'\n'
        output_file.write(content_line)
    
    output_file.write('\nNa-O-Si\n')
    output_file.write('times / ns\t%\n')
    for i in range(len(time)):
        content_line = "{:.3f}".format(time[i])+'\t'+"{:.2f}".format(NaOSi[i])+'\n'
        output_file.write(content_line)
    
    output_file.write('\nMg-O-Na\n')
    output_file.write('times / ns\t%\n')
    for i in range(len(time)):
        content_line = "{:.3f}".format(time[i])+'\t'+"{:.2f}".format(MgONa[i])+'\n'
        output_file.write(content_line)
        
    output_file.write('\nMg-O-Mg\n')
    output_file.write('times / ns\t%\n')
    for i in range(len(time)):
        content_line = "{:.3f}".format(time[i])+'\t'+"{:.2f}".format(MgOMg[i])+'\n'
        output_file.write(content_line)
    
    output_file.write('\nMg-O-Ca\n')
    output_file.write('times / ns\t%\n')
    for i in range(len(time)):
        content_line = "{:.3f}".format(time[i])+'\t'+"{:.2f}".format(MgOCa[i])+'\n'
        output_file.write(content_line)
    
    output_file.write('\nMg-O-Al\n')
    output_file.write('times / ns\t%\n')
    for i in range(len(time)):
        content_line = "{:.3f}".format(time[i])+'\t'+"{:.2f}".format(MgOAl[i])+'\n'
        output_file.write(content_line)
    
    output_file.write('\nMg-O-Si\n')
    output_file.write('times / ns\t%\n')
    for i in range(len(time)):
        content_line = "{:.3f}".format(time[i])+'\t'+"{:.2f}".format(MgOSi[i])+'\n'
        output_file.write(content_line)
    
    output_file.write('\nCa-O-Na\n')
    output_file.write('times / ns\t%\n')
    for i in range(len(time)):
        content_line = "{:.3f}".format(time[i])+'\t'+"{:.2f}".format(CaONa[i])+'\n'
        output_file.write(content_line)
        
    output_file.write('\nCa-O-Mg\n')
    output_file.write('times / ns\t%\n')
    for i in range(len(time)):
        content_line = "{:.3f}".format(time[i])+'\t'+"{:.2f}".format(CaOMg[i])+'\n'
        output_file.write(content_line)
        
    output_file.write('\nCa-O-Ca\n')
    output_file.write('times / ns\t%\n')
    for i in range(len(time)):
        content_line = "{:.3f}".format(time[i])+'\t'+"{:.2f}".format(CaOCa[i])+'\n'
        output_file.write(content_line)
        
    output_file.write('\nCa-O-Al\n')
    output_file.write('times / ns\t%\n')
    for i in range(len(time)):
        content_line = "{:.3f}".format(time[i])+'\t'+"{:.2f}".format(CaOAl[i])+'\n'
        output_file.write(content_line)
        
    output_file.write('\nCa-O-Si\n')
    output_file.write('times / ns\t%\n')
    for i in range(len(time)):
        content_line = "{:.3f}".format(time[i])+'\t'+"{:.2f}".format(CaOSi[i])+'\n'
        output_file.write(content_line)
        
    output_file.write('\nAl-O-Na\n')
    output_file.write('times / ns\t%\n')
    for i in range(len(time)):
        content_line = "{:.3f}".format(time[i])+'\t'+"{:.2f}".format(AlONa[i])+'\n'
        output_file.write(content_line)
        
    output_file.write('\nAl-O-Mg\n')
    output_file.write('times / ns\t%\n')
    for i in range(len(time)):
        content_line = "{:.3f}".format(time[i])+'\t'+"{:.2f}".format(AlOMg[i])+'\n'
        output_file.write(content_line)
        
    output_file.write('\nAl-O-Ca\n')
    output_file.write('times / ns\t%\n')
    for i in range(len(time)):
        content_line = "{:.3f}".format(time[i])+'\t'+"{:.2f}".format(AlOCa[i])+'\n'
        output_file.write(content_line)
        
    output_file.write('\nAl-O-Al\n')
    output_file.write('times / ns\t%\n')
    for i in range(len(time)):
        content_line = "{:.3f}".format(time[i])+'\t'+"{:.2f}".format(AlOAl[i])+'\n'
        output_file.write(content_line)
        
    output_file.write('\nAl-O-Si\n')
    output_file.write('times / ns\t%\n')
    for i in range(len(time)):
        content_line = "{:.3f}".format(time[i])+'\t'+"{:.2f}".format(AlOSi[i])+'\n'
        output_file.write(content_line)
        
    output_file.write('\nSi-O-Na\n')
    output_file.write('times / ns\t%\n')
    for i in range(len(time)):
        content_line = "{:.3f}".format(time[i])+'\t'+"{:.2f}".format(SiONa[i])+'\n'
        output_file.write(content_line)
        
    output_file.write('\nSi-O-Mg\n')
    output_file.write('times / ns\t%\n')
    for i in range(len(time)):
        content_line = "{:.3f}".format(time[i])+'\t'+"{:.2f}".format(SiOMg[i])+'\n'
        output_file.write(content_line)
        
    output_file.write('\nSi-O-Ca\n')
    output_file.write('times / ns\t%\n')
    for i in range(len(time)):
        content_line = "{:.3f}".format(time[i])+'\t'+"{:.2f}".format(SiOCa[i])+'\n'
        output_file.write(content_line)
        
    output_file.write('\nSi-O-Al\n')
    output_file.write('times / ns\t%\n')
    for i in range(len(time)):
        content_line = "{:.3f}".format(time[i])+'\t'+"{:.2f}".format(SiOAl[i])+'\n'
        output_file.write(content_line)
        
    output_file.write('\nSi-O-Si\n')
    output_file.write('times / ns\t%\n')
    for i in range(len(time)):
        content_line = "{:.3f}".format(time[i])+'\t'+"{:.2f}".format(SiOSi[i])+'\n'
        output_file.write(content_line)