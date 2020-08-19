#!/bin/bash
# Script intended for retrieving data.
# Example of usage:
#
# >>> to_folder="/media/alex/ALEXDATA/data_sets/CFSR-LAND/"	
# >>> bash get_data.sh $to_folder

# Where data will be put.
output_folder=$1

# Initial and final years. 
yr=1979
fyr=2009

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
	wget --no-clobber --directory-prefix=$output_folder \
	http://hydrology.princeton.edu/data/lst/NetCDF_format/LST_PU_$yr$nm.nc4

	# Update month.
	nm=`expr $nm + 1`

    done

    # Update year.
    yr=`expr $yr + 1`

done
