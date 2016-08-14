import os, sys
import csv
 
with open("mos-2G-Sousse.csv", "r") as fsrce:
    with open("mos-2G-ext_test", "w") as fdest:
        my_reader = csv.reader(fsrce, delimiter = ';')
        my_writer = csv.writer(fdest, delimiter = ';')
        for ligne in my_reader: # ligne est une liste de valeurs de colonnes
            my_writer.writerow([ligne[0]]) # ligne[0] est la valeur de la 1ere colonne de la ligne considere