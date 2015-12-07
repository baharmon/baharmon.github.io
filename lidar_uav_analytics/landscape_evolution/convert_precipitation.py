# -*- coding: utf-8 -*-
"""
Created on Sat Nov 28 10:56:34 2015

@author: Brendan
"""

import os
import csv

precipitation=os.path.abspath('filtered_precipitation.txt')

# open txt file with precipitation data
with open(precipitation) as in_csvfile, open('precipitation.txt', 'wb') as out_csvfile:

    writer = csv.writer(out_csvfile)

    # check for header
    has_header = csv.Sniffer().has_header(in_csvfile.read(1024))
    
    # rewind
    in_csvfile.seek(0)
    
    # skip header
    if has_header:
        next(in_csvfile)
    
    # parse time and precipitation
    precip = csv.reader(in_csvfile, delimiter=',', skipinitialspace=True) 

    # convert rows from inches to mm
    for row in precip:
        row[1] = str(float(row[1])*0.0393701)
        print row
        writer.writerow(row)