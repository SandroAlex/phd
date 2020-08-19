#!/bin/bash
# Script intended to download ndvi data.
# Example of usage:
#
# >>> to_folder="/media/alex/ALEXDATA/data_sets/GIMMS/"	
# >>> bash ndvi_gimms_download.sh $to_folder

# File containing all web links to data files.
data_file="./ndvi_gimms_data_list.txt"

# Where data will be put.
output_folder=$1

# Download data.
wget --no-clobber -i $data_file --directory-prefix=$output_folder
