"""
K-Mean along space dimensions.
"""

# Load packages.
import os
import numpy as np
import xarray as xr
from dask.diagnostics import ProgressBar
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from datetime import datetime

class LandKmeansSpaceClustering:

    def __init__(self, data_array, scaler=None):

        # Time, latitude, and longitude.
        self.dim0, self.dim1, self.dim2 = "time", "lat", "lon" 
        ndims = [self.dim0, self.dim1, self.dim2]  

        # Just guarantee that time is the first dimension. 
        # Ascending ordered dimensions.
        data_array = data_array.transpose(self.dim0, self.dim1, self.dim2)
        data_array = data_array.sortby(self.dim0)
        data_array = data_array.sortby(self.dim1)
        data_array = data_array.sortby(self.dim2) 

        # Original shape.
        self.initial_shape = data_array.shape

        # Each pixel is a time instance of a map.
        self.data_array = data_array

        # Only land pixels.
        X = self.data_array.\
            where(self.data_array.land_mask==True).\
            values.reshape((self.initial_shape[0], -1))
        cols = ~np.isnan(X[0, :])
        X = X[:, cols]
        
        # Normalize data.
        if scaler:

            # Along space dimension.
            transformer = scaler.fit(X)
            self.X = transformer.transform(X)
            
        # Do not normalize data.
        else:
            self.X = X

    def run(self, hparameters):

        # K-means object. 
        self.kmeans = KMeans(**hparameters).fit(self.X)
                
        # Save results as a xarray DataArray object.
        self.clusters = xr.DataArray(
            data=self.kmeans.labels_,
            dims=[self.dim0],
            coords={self.dim0: self.data_array[self.dim0]}
        )

# Load data of anomalies.
file_path = "/LFASGI/sandroal/data_sets/GIMMS/ppdata_ndvi_anomaly.nc"
DSNDVI = xr.open_dataset(file_path)

# Load data into memory.
with ProgressBar():
    DSNDVI = DSNDVI.compute()

# Scale data along time axis.
scaler = StandardScaler()
    
# Initialize an instance of my clusteing object.
clu = LandKmeansSpaceClustering(data_array=DSNDVI.anomalies, scaler=scaler)

# Number of clusters.
ks = [2, 3, 4]
names = ["twok", "threek", "fourk"]

# Loop over these numbers.
DAs = []
for k, name in zip(ks, names):

    # Hyper parameters for sklearn.cluster.KMeans.
    hparams = {
        "n_clusters": k, 
        "init": "k-means++",
        "n_init": 8,
        "max_iter": 300,
        "tol": 0.0001,
        "precompute_distances": "auto",
        "verbose": 1,
        "random_state": None,
        "copy_x": True,
        "n_jobs": -1,
        "algorithm": "auto"
    }

    # Do it.
    clu.run(hparameters=hparams)

    # Fill list.
    DA = clu.clusters
    DA.name = name
    DAs.append(DA)

# Save results as an xarray Dataset object.    
DS = xr.merge(DAs)
    
# Some attributes.
now = datetime.now()
now_str = now.strftime("%B %d, %Y; %Hh:%Mmin:%Ss")
DS.attrs["Description"] = \
    "This data set is the result of clustering K-Means algorithm along " + \
    "space axes. The results are integer numbers representing cluster " + \
    "number." 
DS.attrs["Build"] = "By Alex Araujo"
DS.attrs["Date"] = now_str
DS.attrs["Source"] = os.path.abspath(__file__)

# Export results as a netcdf file.
DS.to_netcdf(
    path="/LFASGI/sandroal/data_sets/GIMMS/" + \
         "ppdata_ndvi_kmeans_space.nc", 
    mode="w" 
)
