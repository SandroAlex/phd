#!/bin/bash

# Download data:
# MODVI: MODIS/Terra Monthly Vegetation Indices Global 1x1 degree V005

# Link:
# https://disc.gsfc.nasa.gov/datasets/MODVI_005/summary?keywords=EVI

# See dowload intructions using wget:
# https://disc.gsfc.nasa.gov/data-access

# Put here all downloaded files.
OUTPUT_FOLDER="/media/alex/ALEXDATA/data_sets/MODIS/VEGETATION/"

# List with all files to be downloaded.
LIST_FILES="${OUTPUT_FOLDER}links_to_data_files.txt"

# Go to proper location.
cd "${OUTPUT_FOLDER}"

# Download all data.
wget --load-cookies ~/.urs_cookies --save-cookies ~/.urs_cookies \
--auth-no-challenge=on --keep-session-cookies --content-disposition \
--no-clobber --input-file "${LIST_FILES}"
