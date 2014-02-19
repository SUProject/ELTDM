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
import multiprocessing as mltp
import numpy as np
# perso


#####
# Modulus part for import in the main
#####

def chunk(x, m):
        """
        Returns a list() of m subsets of the array x by row
        i.e. the subsets have the same number of columns.
        """
        n = x.shape[0]
        quo, mod = divmod(n, m)
        res = []
        for i in range(0, m):
                if i < m-1:
                        print(i*quo,(i+1)*quo -1)
                        res.append(x[(i*quo):((i+1)*quo),:])
                else:
                        print(i*quo,(i+1)*quo + mod -1)
                        res.append(x[(i*quo):((i+1)*quo + mod),:])
        return(res)



	

#####
# Modulus part for test here
#####

if __name__ == "__main__":
        
        # object to be chunked
        m = 4
        x = np.array([[1,2,3],\
                      [11,12,13],\
                      [21,22,23],\
                      [31,32,33],\
                      [41,42,43],\
                      [51,52,53],\
                      [61,62,63],\
                      [71,72,73],\
                      [81,82,83]])
        c = chunk(x, m)
        print(c)
        ### Build a pool of 8 processes
        ##pool = mltp.Pool(processes=4,)
        ##
        ### Fragment the string data into 8 chunks
        ##partitioned_text = list(chunks(text, len(text) / 8))
        ## 
        ### Generate count tuples for title-cased tokens
        ##single_count_tuples = pool.map(Map, partitioned_text)
        ## 
        ### Organize the count tuples; lists of tuples by token key
        ##token_to_tuples = Partition(single_count_tuples)
        ## 
        ### Collapse the lists of tuples into total term frequencies
        ##term_frequencies = pool.map(Reduce, token_to_tuples.items())
		
		


os.system("pause")
