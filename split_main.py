# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 21:42:43 2022

@author: Plaban
"""

import mne
import os

#importing the required libraries

dir_str = "D:\\Ubuntu-backup\\projectVII\\chb01"
dir_cropped = "D:\\Ubuntu-backup\\projectVII\\cropped"

#setting the input and output directories

directory = os.fsdecode(dir_str)
directory_cropped = os.fsencode(dir_cropped)
patients = 1

for file in os.listdir(directory):
    if(patients == 6):
        break
    filename = os.fsencode(file)
    filename = str(filename)
    filename = filename[2:len(filename)-1:]
    if filename.endswith('.edf'):
        path_input = os.path.join(directory, filename)
    else:
        continue
        
    count = 1
    time = 0
    while(time <= 3580):
        
        raw_input = mne.io.read_raw_edf(path_input)
        
        raw_output = raw_input.crop(tmin = float(time), tmax = float(time + 20), include_tmax = True)
        if(time == 3560):
            time = time + 19.9
        else:
            time = time + 20
        
        
# =============================================================================
        filename_cropped = filename[:len(filename)-4:] + "part" + str(count) + ".edf"
 

        path_output = os.path.join(dir_cropped, filename_cropped)
         
# =============================================================================
# =============================================================================
        mne.export.export_raw(path_output, raw_output, fmt = 'edf', physical_range = 'auto', overwrite = True)
        count += 1

    patients += 1         
  
# =============================================================================
        