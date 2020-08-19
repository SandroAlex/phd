#!/bin/bash

echo 
echo "=================================================================================================================="
echo 
echo "Get AVDC data from public directories"
echo 
echo "=================================================================================================================="
echo 

if [ $# -ne 1 ]; then
	echo
	echo "usage: get_avdc_data_pub.sh [AVDC web dir]"
	echo
	echo "------------------------------------------------------------------------------------------"
	echo "1: AVDC web dir: e.g. https://avdc.gsfc.nasa.gov/pub/data/satellite/Aura/OMI/V03/L3/OMNO2d_HR/"
	echo "------------------------------------------------------------------------------------------"
	exit
fi

DIRHTTP=$1

# Only netcdf files (by Alex Araujo).
cd /media/alex/ALEXDATA/data_sets/AURA_OMI_NO2/L3_monthly_010/
wget -r -m -e robots=off -nH -np --cut-dirs=10 --reject "*.html*" -A.nc \
$DIRHTTP
