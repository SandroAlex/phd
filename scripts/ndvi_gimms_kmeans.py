"""
Apply KMeans to NDVI (GIMMS) data in its original temporal and spatial 
resolutions. It is a RAM memory intensive operation, so run this program
in aerossol server.
"""

# Load packages.
import os
import numpy as np
import xarray as xr
from datetime import datetime
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

# Local aerossol server adaptation of my cdlearn clustering class.
class LandKmeansClustering:

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

        # Note that we will next reshape data in order to each pixel represent
        # an instance of dimension given by time range.
        self.data_array = data_array
        Xt = self.data_array.values.reshape((self.initial_shape[0], -1))
        
        # Normalize data.
        if scaler:

            # Along time dimension.
            transformer = scaler.fit(Xt)
            Xt = transformer.transform(Xt)
            self.X = Xt.T # Each time series is an instance.
            
        # Do not normalize data.
        else:
            self.X = Xt.T # Each time series is an instance.

    def run(self, hparameters):

        # K-means object. 
        self.kmeans = KMeans(**hparameters).fit(self.X)
        
        # Reshaping results in order to plot them on maps. 
        clusters = self.kmeans.labels_
        clusters = clusters.reshape(*self.initial_shape[1:])
        
        # Save results as a xarray DataArray object.
        clusters = xr.DataArray(
            data=clusters, 
            dims=[self.dim1, self.dim2],
            coords={self.dim1: self.data_array[self.dim1], 
                    self.dim2: self.data_array[self.dim2]}
        )
    
        # Put land mask as coordinate.
        if "land_mask" in list(self.data_array.coords):
            clusters = clusters.assign_coords(
                coords={"land_mask": self.data_array.land_mask}
            )

        # Let's reorganize clusters labels according to their occurrences.
        old_values = np.copy(clusters.values) 
        new_values = np.copy(clusters.values)
        old_labels, counts = np.unique(
            old_values.flatten(), return_counts=True,
        )
        new_order = np.argsort(counts)[ : : -1] 
        translate = {}
        
        for k, v in zip(old_labels[new_order], np.arange(0, len(old_labels))):
            translate[k] = v
        
        for old, new in translate.items():
            new_values[old_values == old] = new 

        clusters.values = new_values

        # Instance's attribute.
        self.clusters = clusters

# Read preprocessed data.
DATA_FILE = "/LFASGI/sandroal/data_sets/GIMMS/ppdata_ndvi.nc" 
DS = xr.open_dataset(DATA_FILE)

# Scale data along time axis.
scaler = StandardScaler()

# Initialize an instance of my clusteing object.
clu = LandKmeansClustering(data_array=DS.ndvi, scaler=scaler)

# Hyper parameters for sklearn.cluster.KMeans.
hparams = {
    "n_clusters": 9 + 1,  # From previous results (+ 1 spurious sea cluster). 
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

# Save results as an xarray DataSet object.
DS = xr.Dataset({"clusters": clu.clusters})

# Some attributes.
now = datetime.now()
now_str = now.strftime("%B %d, %Y; %Hh:%Mmin:%Ss")
DS.attrs["Description"] = \
    "This data set is the result of clustering K-Means algorithm along " + \
    "time axis. The results are integer numbers representing cluster " + \
    "number. Note that we selected K=9 hyper parameter based on previous " + \
    "results." 
DS.attrs["Build"] = "By Alex Araujo"
DS.attrs["Date"] = now_str
DS.attrs["Source"] = os.path.abspath(__file__)

# Export results as a netcdf file.
DS.to_netcdf(
    path="/LFASGI/sandroal/data_sets/GIMMS/" + \
         "ppdata_ndvi_kmeans.nc", 
    mode="w" 
)
