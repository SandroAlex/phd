#!/bin/bash

# Download data:
# OMI/Aura NO2 Cloud-Screened Total and Tropospheric Column L3 Global Gridded 
# 0.25 degree x 0.25 degree V3

# Link:
# https://disc.gsfc.nasa.gov/datasets/OMNO2d_003/summary

# See dowload intructions using wget:
# https://disc.gsfc.nasa.gov/data-access

# Put here all downloaded files.
OUTPUT_FOLDER="/media/alex/ALEXDATA/data_sets/AURA_OMI_NO2/L3/"

# List with all files to be downloaded.
LIST_FILES="${OUTPUT_FOLDER}links_to_data_files.txt"

# Go to proper location.
cd "${OUTPUT_FOLDER}"

# Download all data.
wget --load-cookies ~/.urs_cookies --save-cookies ~/.urs_cookies \
--auth-no-challenge=on --keep-session-cookies --content-disposition \
--no-clobber --input-file "${LIST_FILES}"
