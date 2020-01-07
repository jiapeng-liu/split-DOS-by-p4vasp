# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pandas as pd
import numpy as np
import os, sys, re

def DOS_transfer(filename):
    
    dos_file = open(filename, 'r')
    lines = dos_file.readlines()
    dos_file.close()
    len_dos = len(lines)
    
    dos_file = open(filename, 'r')
    DOS_data = []
    line_num = 0
    while(1):
        line = dos_file.readline()
        if line != '\n':
            DOS_data.append([float(s) for s in line.rstrip('\n').split()])
            line_num += 1
        else:
            break
    NEDOS = line_num
    DOS_data = np.asarray(DOS_data)
    DOS_case = int(len_dos/(NEDOS+1))
    for t in range(DOS_case-1):
        pDOS = []
        for i in range(NEDOS):
            pDOS.append([float(s) for s in dos_file.readline().rstrip('\n').split()])
        pDOS = np.asarray(pDOS)
        DOS_data = np.concatenate((DOS_data, pDOS), axis=1)
        DOS_data = np.delete(DOS_data, -2, axis=1)
        # skip the space line
        dos_file.readline()
    
    # write the split DOS into csv file
    df = pd.DataFrame(DOS_data)
    df.to_csv('{}.csv'.format(filename[0:-4]), index=False, header=False)


if __name__=="__main__":
    
    filename = sys.argv[1]
    DOS_transfer(filename)
    