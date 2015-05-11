#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Alvin Lawson
# @Date:   2015-05-11 00:45:15
# @Last Modified by:   Alvin Lawson
# @Last Modified time: 2015-05-11 00:45:18
def Addition(x, y): #Addition formula
        	sum = x + y
        	Additionsentence = 'The sum of {} and {} is {}.'.format(x, y, sum) # .format helps to ensure the string outputs inside of {}
        	print Additionsentence
 
def Product(c, d): # Multiply formula
	product = c * d
    Subtractionsentence = 'The product of {} and {} is {}'.format(c,d, product) # .format helps to ensure the string outputs inside of {}
	print Subtractionsentence
	
 
 
 
#The computer reads the main function first to retrieve the data from the user.
def main():
	#asking the user for integers in addtion
        	a = input("Enter an integer for addition:")
        	b = input("Enter another integer addition:")
        	Addition(a, b)
        	#asking the user for integers in addtion
        	e = input("Enter the integer for product:")
        	f = input("Enter another integer for product:")
        	Product(e, f)
 
main()