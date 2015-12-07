# -*- coding: utf-8 -*-
"""
Created on Sat Nov 28 10:56:34 2015

@author: Brendan
"""

import os
import csv

precipitation=os.path.abspath('Harmon_Brendan_LAKE_Hourly_Precip.txt')

# open txt file with precipitation data
with open(precipitation) as in_csvfile, open('filtered_precipitation.txt', 'wb') as out_csvfile:

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

    # filter for values greater than or equal to 0.05 (inches)
    for row in precip:
        if row[1] >= "0.05":
            print row
            writer.writerow(row)