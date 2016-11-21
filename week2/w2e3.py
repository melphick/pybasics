#!/usr/bin/env python

entry1 = "*  1.0.192.0/18   157.130.10.233        0 701 38040 9737 i"
entry2 = "*  1.0.192.0/18     157.130.10.233       0 701 1299 15169 i"
entry3 = "*  1.0.192.0/18    157.130.10.233        0 701 9505 17408 2.1465 i"
entry4 = "*  1.0.192.0/18      157.130.10.233        0 701 6762 6762 6762 6762 38040 9737 i"

entry1_list = entry1.split()
entry2_list = entry2.split()
entry3_list = entry3.split()
entry4_list = entry4.split()

entry1_route = entry1_list[1]
entry2_route = entry2_list[1]
entry3_route = entry3_list[1]
entry4_route = entry4_list[1]

entry1_path = entry1_list[4:]
entry2_path = entry2_list[4:]
entry3_path = entry3_list[4:]
entry4_path = entry4_list[4:]

print '{:20} {:20}'.format('ip_prefix', 'as_path')
print '{:20} {:20}'.format(entry1_route, entry1_path)
print '{:20} {:20}'.format(entry2_route, entry2_path)
print '{:20} {:20}'.format(entry3_route, entry3_path)
print '{:20} {:20}'.format(entry4_route, entry4_path)