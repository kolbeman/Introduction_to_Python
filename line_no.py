#!/usr/bin/env python

import sys  # <1>
print(sys.argv)  # <2>

elements = len(sys.argv)
#print(elements)
#
for file in sys.argv[1:]:
    with open(file) as file_in:
        for i,raw_line in enumerate(file_in,1):
            line = raw_line.rstrip()
            print(i,line)
print('-' * 80)
