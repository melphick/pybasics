#!/usr/bin/env python
# -*- coding: utf-8 -*-

show_ver='''Cisco IOS Software, C880 Software (C880DATA-UNIVERSALK9-M), Version 15.0(1)M4, RELEASE SOFTWARE (fc1)
Technical Support:
Copyright (c) 1986-2010 by Cisco Systems, Inc.
Compiled Fri 29-Oct-10 00:02 by prod_rel_team
ROM: System Bootstrap, Version 12.4(22r)YB5, RELEASE SOFTWARE (fc1)

twb-sf-881 uptime is 7 weeks, 5 days, 19 hours, 23 minutes
System returned to ROM by reload at 15:33:36 PST Fri Feb 28 2014
System restarted at 15:34:09 PST Fri Feb 28 2014
System image file is "flash:c880data-universalk9-mz.150-1.M4.bin"
Last reload type: Normal Reload
Last reload reason: Reload Command

Cisco 881 (MPC8300) processor (revision 1.0) with 236544K/25600K bytes of memory.
Processor board ID FTX1000038X

5 FastEthernet interfaces
1 Virtual Private Network (VPN) Module
256K bytes of non-volatile configuration memory.
126000K bytes of ATA CompactFlash (Read/Write)

License Info:
License UDI:
------------------------------------------------
Device#   PID                   SN
------------------------------------------------
*0        CISCO881-SEC-K9       FTX1000038X

License Information for 'c880-data'
    License Level: advipservices   Type: Permanent
    Next reboot license Level: advipservices

Configuration register is 0x2102'''

show_version = unicode(show_ver, "UTF-8")
show_version = show_version.replace(u"\u00A0", " ")

version_lines = show_version.split('\n')

version_dict = {}

for i,element in enumerate(version_lines):
	if ("Cisco IOS Software" in element) and ("Version" in element):
		words = element.split(' ')
		version_dict['vendor'] = words[0]
		for i,element in enumerate(words):
			if element == 'Version':
				print words[i+1]
				version_dict['version'] = words[i+1]
	if ("Device#" in element) and ("PID" in element):
		line = version_lines[i+2]
		collapsedline = ' '.join(line.split())
		words = collapsedline.split(' ')
		version_dict['model'] = words[1]
		version_dict['serial'] = words[2]
		print element
		print words


print version_dict
