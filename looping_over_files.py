#!/usr/bin/env python
import sys

search_term = sys.argv[1]
print("Looking for", search_term)

for file_name in sys.argv[2:]:  # loop over sys.argv but skip script name
    print("file_name:", file_name)
