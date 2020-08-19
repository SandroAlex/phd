#!/bin/bash
# Script intended to downloading evaporation data from ERA-INTERIM.
#
# Usage:
# >>> bash evaporation.sh

# Initial and final years. 
yr=1981
fyr=2017

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

	# Last day of this month in this year.
	ld=$(python last_day.py $yr $nm)

	# Initial and final dates.
	di=$yr-$nm-01
	df=$yr-$nm-$ld

	# Name of the output file.
	tg=evaporation"_"$yr"_"$nm.grb
	
	# Get data.
	python evaporation.py $di $df $tg 
	
	# Update month.
	nm=`expr $nm + 1`

    done

    # Update year.
    yr=`expr $yr + 1`

done
