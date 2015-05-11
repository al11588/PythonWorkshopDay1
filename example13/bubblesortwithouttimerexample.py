#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Alvin Lawson
# @Date:   2015-05-11 00:59:14
# @Last Modified by:   Alvin Lawson
# @Last Modified time: 2015-05-11 00:59:26
#from time import * #Imports the time for the library
def bubbleSort(alist):
        	for passnum in range(len(alist)-1,0,-1):
	    	for i in range(passnum):
    		if alist[i]>alist[i+1]:
        	        	temp = alist[i]
        	        	alist[i] = alist[i+1]
        	        	alist[i+1] = temp
 
#start = time()
 
alist = [54,26,93,17,77,31,44,55,20]
bubbleSort(alist)
print(alist)
#print "%.2f seconds" % (time() - start) #shows the literal number of a string
