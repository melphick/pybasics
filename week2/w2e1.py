#!/usr/bin/env python

user_network = "234.210.134.4"
print "You input: %s" % user_network

network_list = user_network.split('.')

network_list = network_list[0:3]

print network_list

network_list.append('0')

print network_list

type(network_list)

network_string = network_list[0]+"."+network_list[1]+"."+network_list[2]+"."+network_list[3]

print "The IP network is %s" % network_string

a = 'NETWORK_NUMBER' 
b = 'FIRST_OCTET_BINARY'
c = 'FIRST_OCTECT_HEX'

print '{:20} {:20} {:20}'.format(a, b, c)

a = network_string
b = bin (int (network_list[0]))
c = hex (int (network_list[0]))

print '{:20} {:20} {:20}'.format(a, b, c)
