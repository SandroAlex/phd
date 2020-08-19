#!/bin/bash

# Data details:
# https://psl.noaa.gov/data/gridded/data.noaa.oisst.v2.highres.html

# Main URL.
data_source='ftp://ftp.cdc.noaa.gov/Datasets/noaa.oisst.v2.highres/'

# Where to put downloaded data files.
data_folder='/media/alex/ALEXDATA/data_sets/NOAA_OI_SST_V2/'

# Initial and final years. 
yr=1981
fyr=2020

# Loop over years.
while [ $yr -le $fyr ]
do

  # Daily mean sst data list.
  file_name='sst.day.mean.'$yr'.nc'	  
  file_url=$data_source$file_name
  file_path=$data_folder$file_name	

  # Download file.
  wget $file_url --show-progress --no-clobber -O $file_path
	
  # Update year.
  yr=$(expr $yr + 1)

done
