###
# Fichier: Upload&Extract_Data.py
####

from pyexcel.cookbook import merge_all_to_a_book
import glob
import csv


with open('dataset/MOS_Test.csv', "rb") as fsrce:
    with open ('MOS_EXT.csv', "wb") as fdest:
        reader=csv.reader(fsrce, delimiter=';')
        writer = csv.writer(fdest,delimiter='|',lineterminator = "\n" )
 #       headers=[Rxlev,RXQ_sub,MOS]
        for line in reader:
            #print (row[1],row[8],row[15])
            writer.writerow ([line[1],line[8],line[15]])
            merge_all_to_a_book(glob.glob("MOS_EXT.csv"), "MOS_EXT.xls")
fsrce.close()
fdest.close()





























