"""
Calculate anomalies of NDVI GIMMS data in its original temporal and spatial 
resolutions. It is a RAM intensive operation, but can be run on my local 
20 GB RAM machine.
"""

# Load packages.
import os
import sys
import xarray as xr
from datetime import datetime

# My repository.
repository = "/home/alex/Dropbox/repositories/"

# Include once my repository in the path for searching libraries.
if repository not in sys.path:
    sys.path.append(repository)

# Import my package.
import cdlearn

# Read preprocessed data.
DATA_FILE = "/media/alex/ALEXDATA/data_sets/GIMMS/ppdata_ndvi.nc" 
DS_GIMMS = xr.open_dataset(DATA_FILE)

# Calculate anomalies.
DA = cdlearn.statistics.anomalies(DS_GIMMS.ndvi)

# Save results as an xarray DataSet object.
DS = xr.Dataset({"anomalies": DA})

# Some attributes.
now = datetime.now()
now_str = now.strftime("%B %d, %Y; %Hh:%Mmin:%Ss")
DS.attrs["Description"] = \
    "Anomalies of ndvi gimms data in its original spatial and temporal " + \
    "resolutions." 
DS.attrs["Build"] = "By Alex Araujo"
DS.attrs["Date"] = now_str
DS.attrs["Source"] = os.path.abspath(__file__)

# Export results as a netcdf file.
DS.to_netcdf(
    path="/media/alex/ALEXDATA/data_sets/GIMMS/" + \
         "ppdata_ndvi_anomaly.nc", 
    mode="w" 
)