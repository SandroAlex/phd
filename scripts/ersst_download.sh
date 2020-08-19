#!/bin/bash
# NetCDF data files are archived in NCDC Archiving System.
# ERSST data in NetCDF format. Filename convention is:
#    (1): ersst.VERSION.yyyymm.nc
#    (2): yyyy=four digit year
#    (3): mm=two digit month
# How to download data:

# Initial and final years. 
yr=1854
fyr=2018

# Loop over years.
while [ $yr -le $fyr ]; do

    # Month.
    nm=1

    # Loop over months.
    while [ $nm -le 12 ]; do
  
	# Put a zero in front of numbers from 0 to 9: 00, 01, 02, ..., 09
	if [ $nm -lt 10 ]; then 
	    nm=0$nm
	fi

	# Download file.
	wget ftp://ftp.ncdc.noaa.gov/pub/data/cmb/ersst/v5/netcdf/ersst.v5.$yr$nm.nc

	# Update month.
	nm=`expr $nm + 1`

    done

    # Update year.
    yr=`expr $yr + 1`

done
