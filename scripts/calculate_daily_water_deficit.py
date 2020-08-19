"""
This script calculates daily water deficit for the whole globe. 
Intensive operations! Use aerossol LFA cluster!
"""

# Initial setup.
import glob
import progressbar
import datetime

import xarray as xr
import numpy as np

from dask.diagnostics import ProgressBar

# Read daily data of water balance.
input_folder = "/LFASGI/sandroal/data_sets/ERA_INTERIM/water_balance_daily/"
output_folder = "/LFASGI/sandroal/data_sets/ERA_INTERIM/water_deficit_daily/"

# Absolute paths.
files = sorted(glob.glob(input_folder + "*.nc"))

# Load all data. Daily mean values.
WB_ds = xr.open_mfdataset(files, concat_dim="time", combine="by_coords", chunks={})

# Data array for daily data.
WB_da = WB_ds.wb

# Time, latitude, and longitude.
WB_da = WB_da.transpose("time", "latitude", "longitude")

# Load all data into memory.
print("\n>>> Loading data into memory ...")
with ProgressBar():
    WB_da = WB_da.compute()

# Calculate water deficit. First, extract water balance data as numpy array.
WB_data = WB_da.values

# Initialize numpy array for water deficit data as zeros.
WD_data = np.zeros_like(WB_data)

# First time step.
WD_data[0] = np.minimum(WB_data[0], 0)

# Loop over the remaining time steps:
print("\n>>> Calculating water deficit ...")
with progressbar.ProgressBar(max_value=WB_data.shape[0]) as bar:
    for n in range(1, WB_data.shape[0]):
    
        # Deficit occurs in two consecutive days.
        deficit = WD_data[n - 1] + WB_data[n] < 0
      
        # Accumulate negative number for the current deficit where deficit==True.
        # Otherwise, the numpy array gets zero at the location
        WD_data[n] = np.where(deficit, WD_data[n - 1] + WB_data[n], 0)
    
        bar.update(n)

# First we create a xarray DataArray object that will contain data for the 
# subsequent DataSet object from xarray.
WD_da = xr.DataArray(
    data=WD_data, 
    coords={"time": WB_ds.time, 
            "latitude": WB_ds.latitude,
            "longitude": WB_ds.longitude},
    dims=("time", "latitude", "longitude")
)

# Now we can create DataSet object for water deficit variable.
WD_ds = xr.Dataset(data_vars={"wd": WD_da})
WD_ds.wd.attrs["calculation"] = "Made by Alex Araujo at " + \
                                datetime.datetime.now().strftime("%Y-%m-%d")
WD_ds.wd.attrs["long_name"] = "Cumulative water deficit"
WD_ds.wd.attrs["units"] = "m"

# Make one file per month.
print("\n>>> Saving results for " + "wb" + " at " + output_folder + " ...")
for year in np.unique(WD_ds.time.dt.year):
    for month in np.unique(WD_ds.time.dt.month):
        print("* Date:", str(year) + "-" + str("{:02}").format(month))
        WD_ds.sel(time=str(year) + "-" + str(month)).to_netcdf(
            output_folder + \
            "wd" + "_daily_" + str(year) + "_" + str("{:02}").format(month) + ".nc")