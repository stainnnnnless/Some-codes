#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 18 10:26:52 2019

@author: shuoshan
"""
import h5py
import os

base_dir = os.path.dirname(os.path.abspath(__file__)) 
h5_filename = os.path.join(base_dir,'indoor3d_sem_seg_hdf5_data','ply_data_all_21.h5')

f = h5py.File(h5_filename)
data = f['data'][:]
label = f['label'][:]

print data

'''
with open('readh5.txt','r') as rh:
    rh.write()
'''