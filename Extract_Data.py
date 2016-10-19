###
# Fichier: Extract_Data.py
####
import pandas as pd
from Upload_Data import *

fdest=open ('dataset/MOS_EXT.csv', "wb")
writer = csv.writer(fdest,delimiter=',',lineterminator = "\n" ) ####  Writer object which writes over an output csv file(MOS_EXT.csv')
for line in reader:#### For each line in the reader object in the Upload_Data.py file
    writer.writerow ([line[15],line[8],line[1]]) 
### Write the extracted colomns to the output file named as"MOS_EXT.csv"
#### the 3 indexes specified in the writer function are respectively for: "RxLev","RXQ","MOS"
