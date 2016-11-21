#!/usr/bin/env python

import sys

ip_addr = sys.argv[1]

ip_list = ip_addr.split('.')

bin_list = ip_list[:]

for i,element in enumerate(bin_list):
	bin_list[i] = bin (int (element))

bin_str_list = bin_list[:]

bin_ip = []

for i,element in enumerate(bin_str_list):
	str = list(element)
	str = str[2:]
	count = range(8 - len(str))
	for i in count:
		var = '0'
		str.insert(0,var)
	bin_ip_octet = ''.join(str)
	bin_ip.append(bin_ip_octet)
	
bin_str = '{0}.{1}.{2}.{3}'.format(bin_ip[0], bin_ip[1], bin_ip[2], bin_ip[3])

print '{:20} {:20}'.format('IP address', 'Binary')
print '{:20} {:20}'.format(ip_addr, bin_str)

