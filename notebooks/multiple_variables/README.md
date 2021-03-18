# Description

## Overview

In these python jupyter notebooks we use more than one climatic and/or surface variable in order to create new ones or investigate relations among them.

## Better visualization of notebooks  

- [notable_regions_amazonia.ipynb](https://nbviewer.jupyter.org/github/SandroAlex/phd/blob/master/notebooks/multiple_variables/notable_regions_amazonia.ipynb?flush_cache=true).
    - **Key ideas:**
        - Vegetation indexes for Amazonia coming from AVHRR (NDVI) and MODIS (NDVI, EVI).
        - Precipitation data from CHIRPS.
        - AVHRR (NDVI): 15-day time step, from 07-1981 to 12-2015; 1/12° x 1/12° (8 km x 8 km) spatial resolution. 
        - MODIS (NDVI, EVI): monthly time step, from 02-2000 to 01-2021; 0.05° x 0.05° (5 km x 5 km) spatial resolution.
        - CHIRPS (Precipitation): Same spatiotemporal grid as the AVHRR's one.
        - Can precipitation explain the differences in vegetation trends between human perturbed and pristine regions? Answer: No, apparently. 
    - **References:**
        - [Climate Data Guide: NDVI: NORMALIZED-DIFFERENCE-VEGETATION-INDEX: NOAA AVHRR](https://climatedataguide.ucar.edu/climate-data/ndvi-normalized-difference-vegetation-index-noaa-avhrr).
        - [Website: MOD13C2 v006 MODIS/Terra Vegetation Indices Monthly L3 Global 0.05 Deg CMG](https://lpdaac.usgs.gov/products/mod13c2v006/).
        - [CHIRPS: Rainfall Estimates from Rain Gauge and Satellite Observations](https://www.chc.ucsb.edu/data/chirps).
        - Atkinson, P., Dash, J., and Jeganathan, C. (2011). [Amazon vegetation greenness as measured by satellite sensors over the last decade](https://agupubs.onlinelibrary.wiley.com/doi/full/10.1029/2011GL049118). Geophysical Research Letters, 38(19).

- [notable_regions_argentina.ipynb](https://nbviewer.jupyter.org/github/SandroAlex/phd/blob/master/notebooks/multiple_variables/notable_regions_argentina.ipynb?flush_cache=true).
    - **Key ideas:**
        - Vegetation indexes for Argentina coming from AVHRR (NDVI) and MODIS (NDVI, EVI).
        - Precipitation data from CHIRPS.
        - AVHRR (NDVI): 15-day time step, from 07-1981 to 12-2015; 1/12° x 1/12° (8 km x 8 km) spatial resolution. 
        - MODIS (NDVI, EVI): monthly time step, from 02-2000 to 01-2021; 0.05° x 0.05° (5 km x 5 km) spatial resolution.
        - CHIRPS (Precipitation): Same spatiotemporal grid as the AVHRR's one.
        - Can precipitation explain the differences in vegetation trends between human perturbed and pristine regions? Answer: No, apparently. 
    - **References:**
        - Volante, J. N., Alcaraz-Segura, D., Mosciaro, M., Viglizzo, E. F., and Paruelo, J. (2012). [Ecosystem functional changes associated with land clearing in nw argentina](https://www.sciencedirect.com/science/article/pii/S016788091100291X?casa_token=fsAnBYzgx-gAAAAA:YJxp8BFtU-Oh9rudwZxGDh73GSzzyt6UOBWPbF4pozOvCFRaKyt3GOf9T7xxJHFxDAguYMTsDg). Agriculture, Ecosystems & Environment, 154:12–22.

- [notable_regions_nordeste.ipynb](https://nbviewer.jupyter.org/github/SandroAlex/phd/blob/master/notebooks/multiple_variables/notable_regions_nordeste.ipynb?flush_cache=true).
    - **Key ideas:**
        - Vegetation indexes for Brazilian Northeast region (Nordeste) coming from AVHRR (NDVI) and MODIS (NDVI, EVI).
        - Precipitation data from CHIRPS.
        - AVHRR (NDVI): 15-day time step, from 07-1981 to 12-2015; 1/12° x 1/12° (8 km x 8 km) spatial resolution. 
        - MODIS (NDVI, EVI): monthly time step, from 02-2000 to 01-2021; 0.05° x 0.05° (5 km x 5 km) spatial resolution.
        - CHIRPS (Precipitation): Same spatiotemporal grid as the AVHRR's one.
        - Can precipitation explain the differences in vegetation trends between human perturbed and pristine regions? Answer: Yes, apparently.

- [surface_relative_humidity.ipynb](https://nbviewer.jupyter.org/github/SandroAlex/phd/blob/master/notebooks/multiple_variables/surface_relative_humidity.ipynb?flush_cache=true):
    - **Main ideas:**
        - Notebook intended to calculate `daily` relative humidity at surface based on ERA-INTERIM datasets of temperature and dew point temperature both at surface (2 m above the ground). Based on Clausius-Clayperon equation: es(T) = 6.1094 exp((17.625 * T)/(T + 243.04)), where T is temperature in degree Celsius, you can calculate relative humidity RH as the following: RH =(es(Td))/(es(T)) * 100\%, where Td is the dew point temperature.
        - Surface temperature and dew point temperature are both at 6-hour resolution, from 1979-01-01 to 2018-12-31. The spatial coverage is global with 0.75x0.75 degrees resolution. We export resulting relative humidity files in the same spatio-temporal grid.
    
    - **Comments:**
        - The package cfgrib creates index files which makes reading much faster.
    
    - **References:**
        - [ERA datasets: near-surface humidity](https://confluence.ecmwf.int/display/CKB/ERA+datasets%3A+near-surface+humidity).
        - [Calculate Temperature, Dewpoint, or Relative Humidity](http://andrew.rsmas.miami.edu/bmcnoldy/Humidity.html).

- [water_balance.ipynb](https://nbviewer.jupyter.org/github/SandroAlex/phd/blob/master/notebooks/multiple_variables/water_balance.ipynb?flush_cache=true):
    - **Main ideas:**
        - This notebook is intended for constructing `daily` water balance variable, which is defined as the difference between daily precipitation and evapotranspiration. 
        - Total precipitation and evaporation are both at `12-hour` resolution, from 1979-01-01 to 2018-12-31. The spatial coverage is global with 0.75x0.75 degrees resolution. We export resulting water balance files in the same spatial grid with `daily` time resolution.    
        - First we create a variable called water balance (WB) which is based on the difference between total precipitation (TP) and evaporation (E).
        - Please note the flipped sign in evaporation on the due cell.This is so because of ERA interim definition of evaporation, as you can see in [evaporation parameter details](https://apps.ecmwf.int/codes/grib/param-db?id=182). Also, remember that evaporation is the accumulated amount of water that has evaporated from the Earth's surface, **including a simplified representation of transpiration (from vegetation)**, into vapour in the air above.  