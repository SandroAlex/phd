#!/bin/bash

# Data details:
# https://data.nodc.noaa.gov/cgi-bin/iso?id=gov.noaa.ncdc:C00813

# Data source.
MAIN_URL="https://www.ncei.noaa.gov/data/avhrr-land-normalized-difference-vegetation-index/access/"

# Where to put downloaded data files.
OUTPUT_FOLDER="/LFASGI/sandroal/data_sets/NOAA_NDVI_V4/"

# Where lives this script.
SCRIPT_FOLDER="/LFASGI/sandroal/scripts/"

# Initial and final years. 
yr=1981
fyr=2020

# Loop over years.
while [ $yr -le $fyr ]; do

# Python script for each year. Generate a list of downloadable files.
cat << EOF > noaa_ndvi_v4_download.py
#!/science/anaconda3/envs/deepweather/bin/python

# Load packages.
import requests
from bs4 import BeautifulSoup

# Auxiliary functions.
def list_full_directory(url, extension):
    page = requests.get(url).text
    soup = BeautifulSoup(page, "html.parser")
    files_paths = [\
        url + "/" + node.get("href") for node in soup.find_all("a") \
        if node.get('href').endswith(extension)]
    return sorted(files_paths)

print(">>> Processing year ${yr} ...")

# Extract url.
url = "${MAIN_URL}" + "${yr}"

# Only netcdf files.
extension = "nc"

# Create text file with data links.
f = open("data_sources_${yr}.txt", "w+")
files = list_full_directory(url, extension)
for FILE in files:
    f.write(FILE + "\n")    

f.close()
EOF

# Run python script and then delete it.
chmod 755 noaa_ndvi_v4_download.py
./noaa_ndvi_v4_download.py
rm -f noaa_ndvi_v4_download.py

# Downloadable files.
DFILES="${SCRIPT_FOLDER}data_sources_${yr}.txt"

# One directory for each year.
mkdir "${OUTPUT_FOLDER}${yr}"

# Go to proper directory.
cd "${OUTPUT_FOLDER}${yr}"

# Download files.
for URL in `cat "${DFILES}"`
do
    curl -O "${URL}"
done

# Go back to script folder.                                                  
cd "${SCRIPT_FOLDER}"

# Delete text file.
rm -r "${DFILES}"

# Update year.
yr=`expr $yr + 1`

done
