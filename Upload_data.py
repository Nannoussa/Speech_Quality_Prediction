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
		
with open('dataset/MOS.csv', "rb") as fsrce:
    with open ('MOS_EXT.csv', "wb") as fdest:
        #my_reader= csv.DictReader(fsrce)
        reader=csv.reader(fsrce, delimiter=';')
        writer = csv.writer(fdest,delimiter='',quotechar='"', quoting=csv.QUOTE_ALL)
 #       headers=[Rxlev,RXQ_sub,MOS]
        for row in reader:
            #print (row[1],row[8],row[15])
            writer.writerows ([row[1]])
            writer.writerows ([row[8]])
            writer.writerows ([row[15]])
fsrce.close()
fdest.close()


























