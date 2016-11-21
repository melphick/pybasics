#!/usr/bin/env python

addr = 'FE80:0000:0000:0000:0101:A3EF:EE1E:1719'

ipv6_split = addr.split(':')

print ipv6_split

addr = ":".join(ipv6_split)

print addr