#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Alvin Lawson
# @Date:   2015-05-11 00:46:43
# @Last Modified by:   Alvin Lawson
# @Last Modified time: 2015-05-11 00:46:46
class MyStuff(object):

	def __init__(self):
    	self.Microsoft = "I Love Windows Xbox One"

	def Sony(self):
    	print "I love Playstation 4"
#Add this line under to show the
thing = MyStuff()
thing.Sony()
print thing.Microsoft