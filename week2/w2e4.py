#!/usr/bin/env python

cisco_ios = "Cisco IOS Software, C880 Software (C880DATA-UNIVERSALK9-M), Version 15.0(1)M4, RELEASE SOFTWARE (fc1)"

cisco_ios_list = cisco_ios.split(",")

version_string = cisco_ios_list[2]

version_list = version_string.split()

version = version_list[1]

print version

