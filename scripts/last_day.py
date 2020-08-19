#!/usr/bin/env python
# Get last day number of the given month and year.
#
# First argument: year. Second argument: month.
# Example of usage:
# >>> python last_day.py 2004 10

# Load packages.
import sys, calendar

# Retrieve input data.
year = int(sys.argv[1])
month = int(sys.argv[2])

# Output.
last_day = calendar.monthrange(year, month)[1]
print(last_day)
