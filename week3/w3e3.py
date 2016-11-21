#!/usr/bin/env python

show_ip_int_brief = '''Interface            IP-Address      OK?     Method      Status     Protocol
FastEthernet0   unassigned      YES     unset          up          up
FastEthernet1   unassigned      YES     unset          up          up
FastEthernet2   unassigned      YES     unset          down      down
FastEthernet3   unassigned      YES     unset          up          up
FastEthernet4    6.9.4.10          YES     NVRAM       up          up
NVI0                  6.9.4.10          YES     unset           up          up
Tunnel1            16.25.253.2     YES     NVRAM       up          down
Tunnel2            16.25.253.6     YES     NVRAM       up          down
Vlan1                unassigned      YES    NVRAM       down      down
Vlan10              10.220.88.1     YES     NVRAM       up          up
Vlan20              192.168.0.1     YES     NVRAM       down      down
Vlan100            10.220.84.1     YES     NVRAM       up          up'''

int_lines = show_ip_int_brief.split('\n')

ints = []

for i,element in enumerate(int_lines):
	entry_list = element.split()
	entry_interface = entry_list[0]
	entry_addr = entry_list[1]
	entry_ok = entry_list[2]
	entry_method = entry_list[3]
	entry_status = entry_list[4]
	entry_protocol = entry_list[5]
	if (entry_status == 'up') and (entry_protocol == 'up'):
		tupple = (entry_interface, entry_addr, entry_status, entry_protocol)
		ints.append(tupple)
print ints