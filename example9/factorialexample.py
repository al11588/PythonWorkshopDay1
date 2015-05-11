#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Alvin Lawson
# @Date:   2015-05-11 00:40:55
# @Last Modified by:   Alvin Lawson
# @Last Modified time: 2015-05-11 00:41:02
num = input("Enter the number: ")
 
 
factorial = 1
if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   for i in range(1,num + 1):
        	factorial = factorial*i
 
   print("The factorial of %r, is %r ") % (num, factorial)