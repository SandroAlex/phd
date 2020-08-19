#!/usr/bin/env python
# Auxiliary script for downloading evaporation data from ERA-INTERIM.
# The main script is "evaporation.sh".

# Load packages.
import sys, os
from ecmwfapi import ECMWFDataServer

# Initial and final dates.
datei = sys.argv[1]
datef = sys.argv[2]

# Name for the output file.
target = sys.argv[3]

# Test whether a path is a regular file.
# Intended to download only if there is no such file. 
if os.path.isfile(target):
    print("Warning message:", target + " has already been downloaded.")

else:
    # Download data.
    server = ECMWFDataServer()
    server.retrieve({
        "dataset"  : "interim",
        "class"    : "ei",
        "date"     : datei + "/to/" + datef,
        "expver"   : "1",
        "levtype"  : "sfc",
        "stream"   : "oper",
        "time"     : "00:00:00/12:00:00",
        "type"     : "fc",
        "step"     : "12",
        "param"    : "182.128",
        "target"   : target,
        "grid"     : "0.75/0.75",
        })
