#!/usr/bin/python3

'''
A simple No-Fly tile generator.

Copyright Sebastian Quilter 2015
Released under the GNU GPL version 3 or later

'''

import os
import argparse

from urllib import request

parser = argparse.ArgumentParser(description='This script generates no-fly tiles')

parser.add_argument('-o','--output',default='./output',\
    help='the output directory to write the tiles to',action='store')

args = parser.parse_args()

if not os.path.exists(args.output):
    print("Creating output directory at " + args.output);
    os.makedirs(args.output)

#TODO Create lots of empty files for tiles.  Depends how big tiles are, and the formula to calculate tile numbers from lat/lon

#World Airports
#ourairports.com has a well-maintained list that is updated frequently.
airport_file_handle = request.urlopen("http://ourairports.com/data/airports.csv")
while(True):
    line = airport_file_handle.readline().decode("utf-8")
    if(len(line)<=0):
        break

    split = line.split(',')
    airport_type = split[2]
    if(airport_type == '\"large_airport\"'):
        print(line)
        #TODO write to relevant tiles.  Depends on protocol used to write tiles.
    elif(airport_type == '\"medium_airport\"'):
        print(line)
        #TODO
    elif(airport_type == '\"small_airport\"'):
        print(line)
        #TODO
    elif(airport_type == '\"heliport\"'):
        print(line)
        #TODO
    elif(airport_type == '\"closed\"'):
        print(line)
        #TODO
    elif(airport_type == '\"seaplane_base\"'):
        print(line)
        #TODO


airport_file_handle.close()

#Temporary Flight Restrictions - web scraping may be required
#http://tfr.faa.gov/tfr2/list.html

#Parks managed by the National Park Services
#https://catalog.data.gov/dataset/national-park-boundariesf0a4c
#https://github.com/nationalparkservice/park-tiles/tree/master/data-import/data
#http://www.nps.gov/npmap/tools/park-tiles/#4/39.06/-96.02

#Sports Stadiums
#Not sure where to find this data.
