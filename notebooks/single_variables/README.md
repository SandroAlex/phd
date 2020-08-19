# Description

## Overview

Python notebooks intended to explore and analyze atmospheric and surface variables one at a time.

## Better visualization

- [aod_modis_aqua_means.ipynb](https://nbviewer.jupyter.org/github/SandroAlex/phd/blob/master/notebooks/single_variables/aod_modis_aqua_means.ipynb?flush_cache=true):
    - Visualizing the AOD 550 nm data from AQUA satellite. 

- [aod_modis_terra_means.ipynb](https://nbviewer.jupyter.org/github/SandroAlex/phd/blob/master/notebooks/single_variables/aod_modis_terra_means.ipynb?flush_cache=true):
    - Visualizing the AOD 550 nm data from TERRA satellite.

- [land_cover_modis.ipynb](https://nbviewer.jupyter.org/github/SandroAlex/phd/blob/master/notebooks/single_variables/land_cover_modis.ipynb?flush_cache=true):
    - **Main ideas:**
        - Land cover classes for South America using `MCD12C1 MODIS version 006` product.
        - Spatial resolution is `0.05x0.05` degrees and we show the results for 2018.
        - Data format is `HDF4`.
        - We regrid data to the ERA-INTERIM `0.75x0.75°` grid for `South America` and export the results to a netcdf file.
    - **References:**
        - [MODIS/Terra+Aqua Land Cover Type CMG Yearly L3 Global 0.05 Deg](https://lpdaac.usgs.gov/products/mcd12c1v006/).

- [precipitation_persiann_cdr_msum.ipynb](https://nbviewer.jupyter.org/github/SandroAlex/phd/blob/master/notebooks/single_variables/precipitation_persiann_cdr_msum.ipynb?flush_cache=true):
    - **In this notebook you will find:**
        - Exploration of a single data file (understanding metadata).
        - Daily data analysis for some years in one grid point (time series, onset and demise dates of `dry` seasons).
        - Make monthly sums for all period of data. Export data files to a specific folder.
    - **References:**
        - Arvor, D., Funatsu, B. M., Michot, V., and Dubreuil, V. (2017). Monitoring rainfall patterns in the southern amazon with persiann-cdr data: Long-term characteristics and trends. Remote Sensing, 9(9):889.

- [precipitation_persiann_cdr2.ipynb](https://nbviewer.jupyter.org/github/SandroAlex/phd/blob/master/notebooks/single_variables/precipitation_persiann_cdr2.ipynb?flush_cache=true):
    - **In this notebook you will find:**
        - PERSIANN-CDR precipitation data analysis for South America.
        - Spatial and temporal resolutions are 0.25 x 0.25 (original) and monthly (cumulative), respectively.
        - Monthly means for the period from 1983 to 2019.
        - Time series for some locations of statistical significant trends.
        - Calculate trends for Standardized Precipitation Index (SPI) for the whole period.
        - Droughts of 2005 and 2010 (and 2019).
        - See [this climate data guide page](https://climatedataguide.ucar.edu/climate-data/standardized-precipitation-index-spi) on Standardized Precipitation Index.
    
- [precipitation_trmm.ipynb](https://nbviewer.jupyter.org/github/SandroAlex/phd/blob/master/notebooks/single_variables/precipitation_trmm.ipynb?flush_cache=true):
    - Data from TRMM (TMPA) L3 Daily 0.25 x 0.25 degree (TRMM_3B42_Daily) 1998 - 2017.
    - Maps for monthly cumulative mean data.
    - Empirical orthogonal functions analysis.