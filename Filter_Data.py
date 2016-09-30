###
# Fichier: Filter_Data.py
####
import csv
import pandas as pd
import numpy as np

data=pd.read_csv('dataset/MOS_EXT.csv')
time_slots=[]
print("Total rows: {0}".format(len(data)))
print(list(data)) # See which headers are available
#print data.dtypes
#print data['MOS']

#for i,line in data.loc[data.MOS.notnull(),:].iterrows():
time_slots=data[(data.MOS.notnull())]
print(time_slots)
time_slots.to_csv("dataset/Time_Slots.csv",index=None)
print("Total rows after filtering: {0}".format(len(time_slots)))

#for line in data:
#    if (data.MOS) != null
#    pd.write_csv("Mos_Slots.csv",'w')
#    else
#    line.next()
