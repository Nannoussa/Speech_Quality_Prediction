###
# Fichier:Upload_Data.py
####
import csv
import pandas as pd

#with open('dataset/MOS_Test.csv', "rb") as fsrce:
#fsrce=open('dataset/MOS_Test.csv', "rb")
#reader=csv.reader(fsrce, delimiter=';') #reader object which iterates over an input csv file(MOS_Test.csv)

data=pd.read_csv('dataset/MOS_Test.csv')
print("Total rows: {0}".format(len(data)))














