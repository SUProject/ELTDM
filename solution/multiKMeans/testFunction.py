# -*-coding:Latin-1 -*

#########################################################
# Test functions
# ELADM Project
#########################################################

#####
# packages import
#####
# common
import os
# perso


#####
# Modulus part for import in the main
#####

def Map(x):
	""" length of an objects """
	return len(x)

def Reduce(x,y):
	""" sum of two objects """
	return x + y
	

#####
# Modulus part for test here
#####
if __name__ == "__main__":
		print(" Calculate the length of two lists of objects ")
		z = eval(input("vector of objects:"))
		y = eval(input("vector of objects:"))
		L = Map(z)
		K = Map(y)
		print(L, K)
		
		print("Give the the length of the combined elements ")
		N = Reduce(L,K)
		print(N)
		
		
        #fruits = {"pommes":21, "melons":3, "poires":31}
        #print(fruits.keys())

		
os.system("pause")
