#!/usr/bin/env python

user_network = "234.210.134.4"
print "You input: %s" % user_network

network_list = user_network.split('.')

print network_list

network_string = network_list[0]+"."+network_list[1]+"."+network_list[2]+"."+network_list[3]

print "The IP network is %s" % network_string

a = 'first_octet' 
b = 'second_octet'
c = 'third_octet'
d = 'fourth_octet'

print '{:20} {:20} {:20} {:20}'.format(a, b, c, d)

a = bin (int (network_list[0]))
b = bin (int (network_list[1]))
c = bin (int (network_list[2]))
d = bin (int (network_list[3]))

print '{:20} {:20} {:20} {:20}'.format(a, b, c, d)
