#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Alvin Lawson
# @Date:   2015-05-11 01:02:29
# @Last Modified by:   Alvin Lawson
# @Last Modified time: 2015-05-11 01:02:32
from bs4 import BeautifulSoup
import csv
import urllib2

url="http://www.conakat.com/states/new_york/road_maps/streets_a/"

page=urllib2.urlopen(url)

soup = BeautifulSoup(page.read())

f = csv.writer(open("NewYorknamesandzipcodes.csv", "w"))
f.writerow(["Name", "ZipCodes"]) # Write column headers as the first line

links = soup.find_all('a')

for link in links:
	i = link.find_next_sibling('i')
	if getattr(i, 'name', None):
    	a, i = link.string, i.string
    	f.writerow([a, i])
