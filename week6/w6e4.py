#!/usr/bin/python
...
This script will take one variable 'ip_address' and return the IP address in
dotted binary format always padded to eight binary digits (for example, 
00001010.01011000.00010001.00010111).
...

import sys

def ip_bin_convert(ip_addr):

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

    return bin_str
