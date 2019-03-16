# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a script which transfers pickle documents to pcd file.
"""

a = 0 #counter of the number of lines
with open ('rt.pcd','w') as pcd:
    pcd.write('# .PCD v.7 - Point Cloud Data file format\n'+\
              'VERSION .7\n'+\
              'FIELDS x y z\n'+\
              'SIZE 4 4 4\n'+\
              'TYPE F F F\n'+\
              'COUNT 1 1 1\n'+\
              'WIDTH 120\n'+\
              'HEIGHT 1\n'+\
              'VIEWPOINT 0 0 0 1 0 0 0\n'+\
              'POINTS 120\n'+\
              'DATA ascii\n')

with open('1.csv','r') as ep:
    # pcfile = pickle.load(ep)
    with open('rt.pcd','a')as pcd:
        for j in ep:
            j = j.split(',')
            p = '{} {} {}\n'.format(j[1],j[2],j[3])
            pcd.write(p)
                #print p
                
            #line = str(i)
            #line = line.split('[')
            #line = line.split(']')
            #pcd.write(line+'\n')
            a += 1
                #print a
#print a                

        
        
    
    
