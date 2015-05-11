#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Alvin Lawson
# @Date:   2015-05-11 01:01:29
# @Last Modified by:   Alvin Lawson
# @Last Modified time: 2015-05-11 01:01:32
from lxml import html
import requests
 
page = requests.get('http://econpy.pythonanywhere.com/ex/001.html')
tree = html.fromstring(page.text)
 
 
#This will create a list of buyers:
buyers = tree.xpath('//div[@title="buyer-name"]/text()')
#This will create a list of prices
prices = tree.xpath('//span[@class="item-price"]/text()')
 
print 'Buyers: ', buyers
print 'Prices: ', prices
