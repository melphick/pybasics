#!/usr/bin/env python

bgp_text = '''*  1.0.192.0/18   157.130.10.233        0 701 38040 9737 i
*  1.0.192.0/18     157.130.10.233       0 701 1299 15169 i
*  1.0.192.0/18    157.130.10.233        0 701 9505 17408 2.1465 i
*  1.0.192.0/18      157.130.10.233        0 701 6762 6762 6762 6762 38040 9737 i'''

print bgp_text

print '{:20} {:20}'.format('ip_prefix', 'as_path')

bgp_lines = bgp_text.split('\n')

for i,element in enumerate(bgp_lines):
	entry_list = element.split()
	entry_route = entry_list[1]
	entry_path = entry_list[4:]
	print '{:20} {:20}'.format(entry_route, entry_path)
