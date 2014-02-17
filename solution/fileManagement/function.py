# -*-coding:Latin-1 -*

#########################################################
# Functions for file management
# ELADM Project
#########################################################
# Needs the numpy module
#########################################################

#####
# Modulus part for import in the main
#####
def featureDictFromCsv(filePath):
	"""
	Builds a dictionary from a csv file
	THAT STRICTLY CORRESPONDS TO THE SIMPLEST CASE
	Many improvement can be done but it works for our simple data.csv
	Also returns the names, usefull for the output.
	"""

	# input file
	inFile = open(filePath, "r") # class TextIoWrapper

	print("Reading file...")
	inFileContent = inFile.read() # class str

	# split by lines and cleaning
	inFileContent = inFileContent.split("\n")
	inFileContent.remove('')

	# variables names
	names = inFileContent[0].split(",")

	# dictionary from the features (optimizable !!!)
	x = {}
	for indRow in range(1, len(inFileContent)):
	    s = inFileContent[indRow].split(",")
	    for indCol in range(0, len(names)):
	        x[(indRow, indCol)] = float(s[indCol])
	
	# close the file
	inFile.close()

	return(x, names, inFileContent)


def csvFromFeatureDictAndClust(filePath, names, inFileContent, cluster):
	"""
	Builds a csv file with the features and the cluster
	Needs improvement if the import function is improved
	"""

	# open the file
	outFile = open(filePath, "w") # overwrites if exists, creates if not

	# rewritting
	names.append("cluster")
	outFileContent = ",".join(names)
	for indRow in range(1, len(inFileContent) - 1):
	    s = inFileContent[indRow] + "," + str(cluster[indRow])
	    outFileContent = outFileContent + "\n" + s

	print("Writing file...")
	outFile.write(outFileContent) #only works with str objects

	# close the file
	outFile.close()


#####
# Modulus part for test here
#####

#if __name__ == "__main__":

       
