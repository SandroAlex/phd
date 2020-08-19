"""
Script for applying empirical orthogonal functions to NDVI (GIMMS) data in its
original temporal and spatial resolutions. It is a RAM memory intensive 
operation, so run this program in aerossol server.
"""  

# Load packages.
import xarray as xr
from eofs.xarray import Eof
import datetime
import os

# Read preprocessed data.
DATA_FILE = "/LFASGI/sandroal/data_sets/GIMMS/ppdata_ndvi.nc" 
DS = xr.open_dataset(DATA_FILE)

# Create an EOF solver to do the EOF analysis. Memory intensive operation.
solver = Eof(DS.ndvi)

# Retrieve EOFs, principal component time series, fraction of explained 
# variance, and eigenvalues as xarray DataArray objects for all modes.
EOFs = solver.eofs() 
PCs = solver.pcs()  
FRACs = solver.varianceFraction() 
EIGs = solver.eigenvalues() 

# Attributes for xarray DataSet objects.
attrs = {}
attrs["Description"] = "Empirical orthogonal functions to NDVI (GIMMS) " + \
                       "in its original temporal and spatial resolutions"
attrs["Build"] = "By Alex Araujo"
attrs["Date"] = datetime.datetime.now().strftime("%B %d, %Y; %Hh:%Mmin:%Ss")
attrs["Source"] = os.path.abspath(__file__)

# Set these attributes to results. Must transform from xarray DataArray to 
# DataSets before exporting results as netcdf files.
DAs = [EOFs, PCs, FRACs, EIGs]
names = ["eofs", "pcs", "fracs", "eigs"]
files = ["ppdata_ndvi_eofs_eofs.nc", 
         "ppdata_ndvi_eofs_pcs.nc",
         "ppdata_ndvi_eofs_fracs.nc",
         "ppdata_ndvi_eofs_eigs.nc"]
for DA, name, file in zip(DAs, names, files):
    path = "/LFASGI/sandroal/data_sets/GIMMS/" + file
    DS = DA.to_dataset(name=name)
    DS = DS.assign_attrs(attrs)
    DS.to_netcdf(path=path, mode="w")
