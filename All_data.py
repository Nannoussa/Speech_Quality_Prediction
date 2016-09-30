###
# Fichier: Upload&Extract_Data.py
####

import pandas as pd
import glob
import csv


with open('dataset/MOS_Test.csv', "rb") as fsrce:
    with open ('dataset/MOS_EXT.csv', "wb") as fdest:
        #reader object which iterates over an input csv file(MOS_Test.csv)
        reader=csv.reader(fsrce, delimiter=';')
        #writer object which writes over an output csv file(MOS_EXT.csv')
        writer = csv.writer(fdest,delimiter=',',lineterminator = "\n" )
 #       headers=[Rxlev,RXQ_sub,MOS]
        for line in reader: #for each row in the reader object
            #print (line[1],line[8],line[15])
            writer.writerow ([line[1],line[8],line[15]])
            #merge_all_to_a_book(glob.glob("MOS_EXT.csv"), "MOS_EXT.xls")
        
 ##### *******************************************************************************************************
#Location = 'dataset/MOS_EXT_tab.csv'
#data=pd.read_csv(Location)
data=pd.read_csv('dataset/MOS_EXT_tab.csv','r')
for i,line in data.loc[data.MOS==0,:].iterlines():
    pd.writer_csv("Mos_Slots.csv",'w')





                                 
  ##### *******************************************************************************************************                                
fsrce.close()
fdest.close()











