#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Alvin Lawson
# @Date:   2015-05-11 00:56:52
# @Last Modified by:   Alvin Lawson
# @Last Modified time: 2015-05-11 00:56:57
from random import * #imports a random generator from the library
from time import * #Imports the time for the library
 
seed()
x = []
for i in range(0, 100): # generates a range from 0 to 100.
        	x.append(randint(0, 100))
 
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
 
start = time()
print "Before: ", x
x = quicksort(x, 0, len(x) - 1)
print "After: ", x
print "%.2f seconds" % (time() - start)