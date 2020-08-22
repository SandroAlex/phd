# Description

## Overview

Spatial regrid are done inside these python jupyter notebooks for atmospheric and surface variables coming from different sources. The results are data with original time resolution and 0.75x0.75° resolution for spatial grid, where this grid is compatible with the `0.75° ERA-INTERIM` one.

## Better visualization

- [air_temperature_merra2.ipynb](https://nbviewer.jupyter.org/github/SandroAlex/phd/blob/master/notebooks/regrid_to_era_interim/air_temperature_merra2.ipynb?flush_cache=true):
    - **Main ideas:**
        - This notebook makes the `MERRA2` data for variable of `mean air temperature at 2 m` (daily resolution) spatially compatible with `ERA-INTERIM` data grid: 
            - MERRA2:
                - lat: 361, lon: 576; 0.5 x 0.625 degrees; global.
            - ERA-INTERIM: 
                - lat: 241, lon: 480; 0.75 x 0.75 degrees; global. 
    
- [evapotranspiration_gleam.ipynb](https://nbviewer.jupyter.org/github/SandroAlex/phd/blob/master/notebooks/regrid_to_era_interim/evapotranspiration_gleam.ipynb?flush_cache=true):
    - **Main ideas:**
        - This notebook makes the `GLEAM` actual evaporation or `evapotranspiration` (daily) spatially compatible with `ERA-INTERIM` data grid: 
            - GLEAM:
                - lat: 720, lon: 1440; 0.25 x 0.25 degrees; global.
            - ERA-INTERIM: 
                - lat: 241, lon: 480; 0.75 x 0.75 degrees; global. 

- [ndvi_gimms.ipynb](https://nbviewer.jupyter.org/github/SandroAlex/phd/blob/master/notebooks/regrid_to_era_interim/ndvi_gimms.ipynb?flush_cache=true):
    - **Main ideas:**
        - This notebook makes the GIMMS NDVI data **spatially** compatible with ERA-INTERIM data.
        - First we need to create a regrid file using xesmf packages. This file translates from original GIMMS NDVI grid (2610 x 4320) to ERA-INTERIM one (241 x 480).
        - Then we create the new files using the above regridder file. **Please note that we do not make any manipulations before regridding**. It is necessary to perform a linear transformation and a cutting into data in order to retrieve valid NDVI values. This step is done in the new regridded files.
        - With the regridded files, first we make the transformation to retrieve valid range of NDVI data, and then we calculate the monthly means creating a netcdf file for each year. These final files will be compatible with monthly means from ERA-INTERIM variables.  
        - Finally, we read these monthly means files in order to visualize some data.

- [precipitation_persiann_cdr.ipynb](https://nbviewer.jupyter.org/github/SandroAlex/phd/blob/master/notebooks/regrid_to_era_interim/precipitation_persiann_cdr.ipynb?flush_cache=true):
    - **Main ideas:**
        - This notebook makes the PERSIANN-CDR `daily` precipitation data spatially compatible with ERA-INTERIM data grid: 
            - PERSIANN-CDR:
                - lat: 480, lon: 1440; 0.25 x 0.25 degrees; not global because latitude is between 60S and 60N.
            - ERA-INTERIM: 
                - lat: 161, lon: 480; 0.75 x 0.75 degrees; latitude between 60S and 60N.     
        - [Regridding overview](https://climatedataguide.ucar.edu/climate-data-tools-and-analysis/regridding-overview).
        - [ESMP : ESMF Python interface](https://www.earthsystemcog.org/projects/esmp/).

- [precipitation_persiann_cdr_msum.ipynb](https://nbviewer.jupyter.org/github/SandroAlex/phd/blob/master/notebooks/regrid_to_era_interim/precipitation_persiann_cdr_msum.ipynb?flush_cache=true):
    - **Main ideas:**
        - This notebook makes the PERSIANN-CDR precipitation data (monthly sum) spatially compatible with ERA-INTERIM data grid: 
            - PERSIANN-CDR:
                - lat: 480, lon: 1440; 0.25 x 0.25 degrees; not global because latitude is between 60S and 60N.
            - ERA-INTERIM: 
                - lat: 161, lon: 480; 0.75 x 0.75 degrees; latitude between 60S and 60N. 
        - First we had calculated the monthly cumulative rainfall from the original daily data from PERSIANN-CDR. These calculations can be found on the following notebook: [precipitation_persiann_cdr_msum.ipynb](../single_variables/precipitation_persiann_cdr_msum.ipynb).
        - Compare original and regridded data in South America by means of monthly climatologies and time series.
        - [Regridding overview](https://climatedataguide.ucar.edu/climate-data-tools-and-analysis/regridding-overview).
        - [ESMP : ESMF Python interface](https://www.earthsystemcog.org/projects/esmp/).

- [surface_soil_moisture_gleam.ipynb](https://nbviewer.jupyter.org/github/SandroAlex/phd/blob/master/notebooks/regrid_to_era_interim/surface_soil_moisture_gleam.ipynb?flush_cache=true):
    - **Main ideas:**
        - This notebook makes the `GLEAM` surface soil moisture (daily) spatially compatible with `ERA-INTERIM` data grid: 
            - GLEAM:
                - lat: 720, lon: 1440; 0.25 x 0.25 degrees; global.
            - ERA-INTERIM: 
                - lat: 241, lon: 480; 0.75 x 0.75 degrees; global. 

- [total_solar_incident_radiation_cruncep7.ipynb](https://nbviewer.jupyter.org/github/SandroAlex/phd/blob/master/notebooks/regrid_to_era_interim/total_solar_incident_radiation_cruncep7.ipynb?flush_cache=true):
    - **Main ideas:**
        - This notebook makes the `CRUNCEP7` data for variable of `total incident solar radiation` (6-hour time resolution) spatially compatible with `ERA-INTERIM` data grid: 
            - CRUNCEP7:
                - lat: 360, lon: 720; 0.50 x 0.50 degrees; global.
            - ERA-INTERIM: 
                - lat: 241, lon: 480; 0.75 x 0.75 degrees; global. 