#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: alvinlawson
# @Date:   2015-05-11 00:28:37
# @Last Modified by:   alvinlawson
# @Last Modified time: 2015-05-11 00:30:10
UsersName = raw_input("What is the users name:") # Asks the user what is there name
 
 
UserPassword = raw_input("what is the users password:") #Asks what the users password
 
if UsersName == "Alvin" and UserPassword == "Lawson":
	print "Good Evening Alvin" #Outputs Good Evening Alvin
 
elif UsersName == "John" and UserPassword == "Doe":
    print "Good Evening John" #Outputs Good Evening John
 
else:
	print "Invalid person" # if the person puts the wrong first name and last name.