# -*-coding:Latin-1 -*

#########################################################
# Main commentaire secret
# ELADM project
# WORKS ONLY on windows
#########################################################
# import other files:
# http://fr.openclassrooms.com/informatique/cours/apprenez-a-programmer-en-python/je-viens-pour-conquerir-le-monde-et-creer-mes-propres-modules
# warning on copy of objects and modifications on them
# http://fr.openclassrooms.com/informatique/cours/apprenez-a-programmer-en-python/la-portee-des-variables-2
#numpy unofficial for 64 bits
# http://www.lfd.uci.edu/~gohlke/pythonlibs/#numpy
# tutorial numpy
# http://wiki.scipy.org/Tentative_NumPy_Tutorial#head-c5f4ceae0ab4b1313de41aba9104d0d7648e35cc
#########################################################

#####
# packages import & seed
#####

## Common
import os
# import pickle # to save / load any object (not used here)
import csv
import numpy as np

## Perso
import fileManagement.function as fmf
import monoKMeans.function as monokmf
import random as rd


## seed
rd.seed(8)

#####
# input import
#####

# folder with the input file. we put it as working directory as we write the output in it.
inOutFolder = input("Enter working directory (currently ../input/ please): ")
print(inOutFolder)
os.chdir(inOutFolder)

# number of clusters and method
k = input("Enter number of clusters (only positive integers please): ")
k = int(k)
method = input("Enter distribution method (mono or mutli please): ")

# building a dictionary x from csv file
(x, varName, inFileRow) = fmf.featureArrayFromCsv("data.csv")


#####
# clustering mono thread
#####
if method == "mono":
    center = monokmf.initialize(x, k)
    hasConverged = False

    while not hasConverged:
        centerOld = center
        matDist = monokmf.allDistance(x, center)
        vecAlloc = monokmf.alloc(matDist)
        center = monokmf.newCenter(x, vecAlloc, k)
        hasConverged = (center == centerOld).all()


#####
# clustering multi thread
#####
elif method == "multi":
    None


#####
# output export
#####
else:
    print("Error: Wrong method type provided.")

          
# writing the result with a new column

xAugmented = np.hstack((x, vecAlloc)) # argument is a real tuple => (,) inside the ().
fmf.csvFromFeatureArrayAndClust("data_clustered_" + method + str(k) + ".csv",\
                               varName,\
                               xAugmented)










#####
# test zone
#####



# test of bissextile() in sequentialKmeans
#monokmtf.bissextile()

# Pause of the system
os.system("pause")

