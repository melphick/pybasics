#!/usr/bin/env python

import pprint

infile = open('./infile', 'r')

infile_lines = infile.readlines()

uptime_dict = {}

for i,element in enumerate(infile_lines):
	words = element.split()
	total = 0
	for i,element in enumerate(words):
		if ("year" in element):
			total = total + (int(words[i-1]) * 31536000)
		if ("week" in element):
			total = total + (int(words[i-1]) * 604800)
		if ("day" in element):
			total = total + (int(words[i-1]) * 86400)
		if ("hour" in element):
			total = total + (int(words[i-1]) * 3600)
		if ("minute" in element):
			total = total + (int(words[i-1]) * 3600)
	uptime_dict[words[2]] = total
	print total
print uptime_dict
