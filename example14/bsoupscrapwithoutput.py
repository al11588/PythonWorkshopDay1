#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Alvin Lawson
# @Date:   2015-05-11 01:03:46
# @Last Modified by:   Alvin Lawson
# @Last Modified time: 2015-05-11 01:03:49
from bs4 import BeautifulSoup
import csv
import urllib2

url="http://www.conakat.com/states/new_york/road_maps/streets_a/"

page=urllib2.urlopen(url)

soup = BeautifulSoup(page.read())

f = csv.writer(open("NewYorknamesandzipcodes.csv", "w"))
f.writerow(["Name", "ZipCodes"]) # Write column headers as the first line

links = soup.find_all('a') #finds all links with a's

zipcodes = soup.find_all('i') #finds all the zipcodes.

for link in links:
	i = link.find_next_sibling('i')
	if getattr(i, 'name', None):
    	a, i = link.string, i.string
    	f.writerow([a, i])


    

    	names = link.contents[0]

   	 print (zipcodes)
print (names)
