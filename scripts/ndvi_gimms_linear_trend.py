"""
Script for calculating statistics of linear trends of NDVI (GIMMS) data in its
original temporal and spatial resolutions. Although it is a RAM memory 
intensive operation, this program can be run locally on my ubuntu 20 GB RAM 
machine. 
"""

# Load packages.
import sys
import os
import xarray as xr
from dask.diagnostics import ProgressBar
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
DS = xr.open_dataset(DATA_FILE)

# Load into memory.
with ProgressBar():
    DS = DS.load()

# Slope, intercept, r value, p value, and standard error.
DA_r = cdlearn.statistics.linear_regression(DS.ndvi, verbose=True)

# Export results for linear trends.
now = datetime.now()
now_str = now.strftime("%B %d, %Y; %Hh:%Mmin:%Ss")
DS = xr.Dataset({"trend": DA_r})
DS.attrs["Description"] = \
    "This dataset contains, for each location grid point, " + \
    "the following statistical results: slope, intercept, " + \
    "r value, p value, and standard error"
DS.attrs["Build"] = "By Alex Araujo"
DS.attrs["Date"] = now_str
DS.attrs["Source"] = os.path.abspath(__file__)

DS.to_netcdf(
    path="/media/alex/ALEXDATA/data_sets/GIMMS/" + \
    "ppdata_ndvi_linear_trend.nc", 
    mode="w"
)
