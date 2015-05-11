#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Alvin Lawson
# @Date:   2015-05-11 00:55:41
# @Last Modified by:   Alvin Lawson
# @Last Modified time: 2015-05-11 00:56:05
from random import * #imports a random generator from the library
#from time import * #Imports the time for the library
 
seed() #sets the integer starting value used in generating random numbers.
x = []
for i in range(0, 50): # generates a range from 0 to 50.
        	x.append(randint(0, 50)) #Append adds an item to the end of the list
 
def quicksort(x, l, r):
        	i = l
        	j = r
        	p = x[l + (r - l) / 2] # pivot element in the middle
        	while i <= j:
	    	while x[i] < p: i += 1
	    	while x[j] > p: j -= 1
	    	if i <= j: # swap
    		x[i], x[j] = x[j], x[i]
    		i += 1
    		j -= 1
        	if l < j: # sort left list
	    	quicksort(x, l, j)
        	if i < r: # sort right list
	    	quicksort(x, i, r)
        	return x
 
#start = time()
x = quicksort(x, 0, len(x) - 1)
 
print "Before: ", x
print "After: ", x
#print "%.2f seconds" % (time() - start)