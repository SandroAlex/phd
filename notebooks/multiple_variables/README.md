# Description

## Overview

In these python jupyter notebooks we use more than one climatic and/or surface variable in order to create new ones or investigate relations among them.

## Better visualization of notebooks  

- [surface_relative_humidity.ipynb](https://nbviewer.jupyter.org/github/SandroAlex/phd/blob/master/notebooks/multiple_variables/surface_relative_humidity.ipynb?flush_cache=true):
    - **Main ideas:**
        - Notebook intended to calculate `daily` relative humidity at surface based on ERA-INTERIM datasets of temperature and dew point temperature both at surface (2 m above the ground). Based on Clausius-Clayperon equation:  

        $$ 
        e_s(T) = 6.1094 \exp{\left( \frac{17.625 T}{T + 243.04} \right)}
        $$
        where $T$ is temperature in degree Celsius, you can calculate relative humidity $RH$ as the following:
    
        $$
        RH = \frac{e_s(T_d)}{e_s(T)} 100 \%
        $$
        where $T_d$ is the dew point temperature.
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
        - First we create a variable called water balance ($WB$) which is based on the difference between total precipitation ($TP$) and evaporation ($E$):
        $$
        WB = TP - E
        $$
        - Please note the fliped sign in evaporation on the above cell.This is so because of ERA interim definition of evaporation, as you can see in [evaporation parameter details](https://apps.ecmwf.int/codes/grib/param-db?id=182). Also, remember that evaporation is the accumulated amount of water that has evaporated from the Earth's surface, **including a simplified representation of transpiration (from vegetation)**, into vapour in the air above.  