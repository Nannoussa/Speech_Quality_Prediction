###
# Fichier: QOS_prdictor.py
####

import csv 
 #fname ='mos-2G-Sousse.csv'
#file = open(fname, 'rb')



#extract_list=[]

#fdata= list(freader)
#print (fdata)
#try:
	#freader = csv.reader(open(file, 'rU'), dialect=csv.excel_tab)
	#for row in freader:
		#three_rows = print (row[0], row[1], row[8])
		#extract_list
	#print (extract_list)
#finally:
	#file.close()

	#################### ************************* ######################
		
with open('dataset/MOS.csv', "r") as fsrce:
    with open ('mos_2G_extract.csv', "w") as fdest:
        #my_reader= csv.DictReader(fsrce)
        my_reader=csv.reader(fsrce, delimiter=';')
        my_writer = csv.writer(fdest, delimiter = ';')
        for row in my_reader:
            my_writer.writerow (row[1])



























