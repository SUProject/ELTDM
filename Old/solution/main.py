# -*-coding:Latin-1 -*

#########################################################
# Main
# ELADM project
# WORKS ONLY on windows
#########################################################
# import other files:
# http://fr.openclassrooms.com/informatique/cours/apprenez-a-programmer-en-python/je-viens-pour-conquerir-le-monde-et-creer-mes-propres-modules
# warning on copy of objects and modifications on them
# http://fr.openclassrooms.com/informatique/cours/apprenez-a-programmer-en-python/la-portee-des-variables-2
#numpy unofficial for 64 bits
# http://www.lfd.uci.edu/~gohlke/pythonlibs/#numpy
#########################################################

#####
# packages import
#####

## Common
import os
# import pickle # to save / load any object (not used here)
# import numpy as np # for numerical calculations(not used here)
import csv

## Perso
import fileManagement.function as fmf
import monoKMeans.testFunction as monokmtf


#####
# input import
#####

# folder with the input file. we put it as working directory as we write the output in it.
inOutFolder = input("Enter working directory (currently ../input/ please): ")
os.chdir(inOutFolder)

# number of clusters and method
k = input("Enter number of clusters (only positive integers please): ")
method = input("Enter distribution method (mono or mutli please): ")

# building a dictionary x from csv file
(x, names, inFileContent) = fmf.featureDictFromCsv("data.csv")


#####
# clustering mono thread
#####

y = [i   for i in range(1, len(inFileContent))] # just to test the output

#####
# clustering multi thread
#####



#####
# output export
#####

# writing the result with a new column
fmf.csvFromFeatureDictAndClust("data_clustered_" + method + ".csv",\
                               names,\
                               inFileContent,\
                               y)










#####
# test zone
#####



# test of bissextile() in sequentialKmeans
#monokmtf.bissextile()

# Pause of the system
os.system("pause")

