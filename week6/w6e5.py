#!/usr/bin/python
"""
This script prompts a user for an IP address, then checks if the IP address is
valid, and then converts the IP address to binary (dotted decimal format).
It re-uses the functions created in exercises 3 and 4
"""

import w6e3
import w6e4

ip_addr = raw_input("please enter an IP: ")

if w6e3.ip_check(ip_addr):
    print "The IP address is valid"
    ip_binary = w6e4.ip_bin_convert(ip_addr)
    print "The IP address in binary is: %s" % ip_binary
else:
    print "The IP address is not valid"
