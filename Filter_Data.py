###
# Fichier: Filter_Data.py
####
import csv
import pandas as pd
import numpy as np

##### Read the CSV file using pandas 
data=pd.read_csv('dataset/MOS_EXT.csv')
##### Define a list called "time_slots"
time_slots=[]
##### 
print("Total rows: {0}".format(len(data)))
##### See which headers are available
print(list(data)) 

#search for not null values in the csv file to be extracted into the "time_slots" list
time_slots=data[(data.MOS.notnull())]
print(time_slots)
print("Total rows after filtering: {0}".format(len(time_slots)))
#### Convert the list to a CSV file for further usage
time_slots.to_csv("dataset/Time_Slots.csv",index=None)

