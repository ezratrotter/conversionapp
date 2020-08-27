import numpy as np
import csv, pyodbc
import pandas as pd
from pyproj import Transformer

def conv(x,y,from_epsg, to_epsg, filePath):
       
    MDB = str(filePath)
    DRV = '{Microsoft Access Driver (*.mdb, *.accdb)}'
    PWD = ''

    # connect to db
    con = pyodbc.connect('DRIVER={};DBQ={};PWD={}'.format(DRV,MDB,PWD))
    cur = con.cursor()

    # run a query and get the results 
    SQL = 'SELECT ID, {}, {} FROM Knude WHERE {} IS NOT NULL AND {} IS NOT NULL;'.format(x,y,x,y) # your query goes here
    data = cur.execute(SQL).fetchall()
    
    #separate id's from coords
    ids = [i for i,_,_ in data]
    coords = [[x,y] for _,x,y in data]
    
    print(from_epsg, type(from_epsg))
    transformer = Transformer.from_crs(int(from_epsg), int(to_epsg), always_xy=True)
    newCoords = list(transformer.itransform(coords))
   
    
    #update table in a for loop. once for each row
    for i in range(len(ids)):

        SQL = 'UPDATE Knude SET {}={}, {}={} WHERE id={}'.format(x, newCoords[i][0], y, newCoords[i][1], ids[i])
        
        cur.execute(SQL)

    con.commit()
    cur.close()
    con.close()

def converter(from_epsg, to_epsg, filePath):
        conv("XKoordinat", "YKoordinat", from_epsg, to_epsg, filePath)
        conv("XLabel", "YLabel", from_epsg, to_epsg, filePath)
