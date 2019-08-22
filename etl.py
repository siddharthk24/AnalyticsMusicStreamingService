#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 18:40:39 2019

@author: siddharth_k
"""
import pandas as pd
import glob

def read_data():
    
    path = '/home/siddharth_k/Siddharth/Data Engineering project/data-modeling-with-postgre-master/data/song_data/A/A/A'
    temp=glob.glob(path + '/*')
    
    for val in temp:
        print (val) 
    
    #temp = pd.read_json('/home/siddharth_k/Siddharth/Data Engineering project/data-modeling-with-postgre-master/data/log_data/2018/11/2018-11-06-events.json',lines = True)
    #temp1 = pd.read_json('/home/siddharth_k/Siddharth/Data Engineering project/data-modeling-with-postgre-master/data/song_data/A/A/A/*.json')
    #print(temp[5:6].to_string())
    #print(temp1.head())

def main(): 
    read_data()

if __name__  == "__main__" :
    main()