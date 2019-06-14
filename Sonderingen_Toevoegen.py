# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 15:30:25 2019

@author: c.rasch
"""

def GEF_uitlezen(f):
    
    gef = open(f, "r")
    gef_data = gef.read().splitlines()
    gef.close
    
    return gef_data


def GEF_toevoegen(f):
    
    geflines = GEF_uitlezen(f)
    
    mv=None
    for line in geflines:
        if "ZID" in line:
            mv=float(line.split()[-2][:-1])
            break
    
    x = None
    y = None
    for line in geflines:
        
        if "XYID" in line:
            x = float(line.split(',')[1][1:])
            y = float(line.split(',')[2][1:])
    
    ID = None
    for line in geflines:
        
        if "TESTID" in line:
            ID = line.split()[-1][:]

    for line in geflines:

        if "FILEDATE" in line:

            date = line.split('=')[1][:]
            dag = int(date.split(',')[2][:])
            maand = int(date.split(',')[1][:])
            jaar = int(date.split(',')[0][:])

            date = "{:04d}-{:02d}-{:02d}".format(jaar,maand,dag)

    return(x, y, mv, ID, date)


import os
import glob
import fnmatch
import xlwt
import pandas as pd


path = r'D:\ONTWIKKELING\Grondonderzoek\GEF Bestanden'

bestand = []
aantal_bestanden = len(fnmatch.filter(os.listdir(path), '*.gef'))
for filename in glob.glob(os.path.join(path, '*.gef')):
#    bestand[count] = filename
    bestand.append(filename)


df = pd.read_csv("Database_Sonderingen.csv",sep= ";")


for xx in range(len(bestand)):

    x,y,mv,ID,date   = GEF_toevoegen(bestand[xx])
    # print(x,y,mv,ID,date)
    

        



for index, row in df.iterrows():
    print(row["x"], row["y"])


# for index, row in df.iterrows():

    # print(row[0],index[1])

#for index, row in df.iterrows():
##    print(index,row)
#    print(row[0])

# for row in df.itertuples(index=True, name='Pandas'):
    





