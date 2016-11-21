#!/usr/bin/python
...
This script definesa function that will take one variable 'ip_address'
and return either True or False (depending on whether 'ip_address' is a
valid IP). 
...

import sys

def ip_check (ip_addr):
    reason = []
    valid = True

    ip_list = ip_addr.split('.')

    if len (ip_list) != 4:
            valid = False
            reason.append('IP Address does not have 4 octets')

    if (int(ip_list[0]) < 1) or (int(ip_list[0]) > 223):
            valid = False
            reason.append('IP Address first octet is not between 1 and 223')

    if (int(ip_list[0]) == 127):
            valid = False
            reason.append('IP Address first octet is 127')

    if (int(ip_list[0]) == 169) and (int(ip_list[1]) == 254):
            valid = False
            reason.append('IP Address first and second octet is 169 and 254')

    if (valid == True) and ((int(ip_list[1]) >= 255) or (int(ip_list[2]) >= 255) or (int(ip_list[3]) >= 255)):
            valid = False
            reason.append('IP Address second third or fourth octet is over 255')

    if (valid == True) and ((int(ip_list[1]) < 0) or (int(ip_list[2]) < 0) or (int(ip_list[3]) < 0)):
            valid = False
            reason.append('IP Address second third or fourth octet is less than 0')

    return valid
