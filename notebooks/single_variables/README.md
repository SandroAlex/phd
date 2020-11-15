# Description

## Overview

Python notebooks intended to explore and analyze atmospheric and surface variables one at a time.

## Better visualization

- [aod_modis_aqua_means.ipynb](https://nbviewer.jupyter.org/github/SandroAlex/phd/blob/master/notebooks/single_variables/aod_modis_aqua_means.ipynb?flush_cache=true):
    - Visualizing the AOD 550 nm data from AQUA satellite. 

- [aod_modis_terra_means.ipynb](https://nbviewer.jupyter.org/github/SandroAlex/phd/blob/master/notebooks/single_variables/aod_modis_terra_means.ipynb?flush_cache=true):
    - Visualizing the AOD 550 nm data from TERRA satellite.

- [land_cover_modis.ipynb](https://nbviewer.jupyter.org/github/SandroAlex/phd/blob/master/notebooks/single_variables/land_cover_modis.ipynb?flush_cache=true):
    - **Key ideas:**
        - Land cover classes for South America using `MCD12C1 MODIS version 006` product.
        - Data format is `HDF4` with spatial resolution of 0.05 x 0.05° and `annual` time steps from 2001 to 2019.
        - We regrid land cover data to the GIMMS NDVI3g 1/12 x 1/12° grid for South America and export the results (2001-2019) to a netcdf file.
        - Pixel-wise area calculation.
        - Time evolution of land cover regridded data.
    - **References:**
        - [MODIS/Terra+Aqua Land Cover Type CMG Yearly L3 Global 0.05 Deg](https://lpdaac.usgs.gov/products/mcd12c1v006/).

- [precipitation_chirps.ipynb](https://nbviewer.jupyter.org/github/SandroAlex/phd/blob/master/notebooks/single_variables/precipitation_chirps.ipynb?flush_cache=true):
    - **Key ideas:**
        - Intensive operations that use a lot of RAM memory. Run this notebook inside aerossol server.
        - Chirps is produced at 0.05 x 0.05 degree spatial resolution.
        - Explore single global file.
        - Maps for long term means and standard deviations of South American rainfall (1981 - 2015).
        - Explore monotonic linear long term trends by means of ordinary least squares (OLS) of rainfall for South America in time range 1981 - 2015 without investigating statistical significance of these trends.
        - Regrid and export precipitation data in the same spatial and temporal grid of GIMMS NDVI 3g data set.
    - **References:**
        - [CHIRPS FAQ](https://wiki.chc.ucsb.edu/CHIRPS_FAQ).
        - [Paper: The climate hazards infrared precipitation with stations — a new environmental record for monitoring extremes](https://www.nature.com/articles/sdata201566).
        - [Website: CHIRPS: Rainfall Estimates from Rain Gauge and Satellite Observations](https://www.chc.ucsb.edu/data/chirps).

- [precipitation_mswep.ipynb](https://nbviewer.jupyter.org/github/SandroAlex/phd/blob/master/notebooks/single_variables/precipitation_mswep.ipynb?flush_cache=true):
    - **Key ideas:**
        - Intensive operations that use a lot of RAM memory. Run this notebook inside `aerossol` server.
        - Multi-Source Weighted-Ensemble Precipitation (MSWEP) is a fully global historical precipitation dataset (`1979–2017` with `daily` temporal and `0.1°` spatial resolutions).
        - Explore single `global` file.
        - Explore all data available for `South America` resampled from `daily` to `annual`, `semi-monthly`, and `monthly` sums: (1), time series, (2) mean and standard deviation for all time range, (3) monthly climatology, and (4) long term ordinary least square `OLS` trends of observed data.
        - No evaluation of statistical significances for OLS trends.
        - Regrid and export precipitation data in the same spatial and temporal grid of GIMMS NDVI 3g data set. 
    - **References**
        - [gloh2o: Toward Locally Relevant Global Hydrological Simulations](http://www.gloh2o.org/).

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

- [total_precipitation_era.ipynb](https://nbviewer.jupyter.org/github/SandroAlex/phd/blob/master/notebooks/single_variables/total_precipitation_era.ipynb?flush_cache=true):
    - **Key ideas:**
        - Intensive operations that use a lot of RAM memory. Run this notebook inside one of cluster nodes of `aerossol` server.
        - ERA_INTERIM total precipitation is a fully global historical precipitation dataset (`1979–2018` with `12-hour` temporal and `0.75°` spatial resolutions).
        - Explore single `global` file.
        - Explore all data available for `South America` resampled from `12-houy` to `daily`, `annual`, `semi-monthly`, and `monthly` sums: (1), time series, (2) monthly climatology, and (3) long term ordinary least square `OLS` trends of observed data.
        - No evaluation of statistical significances for OLS trends.