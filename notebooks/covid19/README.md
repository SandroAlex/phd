# Description

## Overview

Covid-19 lockdown effects on air pollution in São Paulo State, Brazil.

## Better visualization

- [hcho_omi.ipynb](https://nbviewer.jupyter.org/github/SandroAlex/phd/blob/master/notebooks/covid19/hcho_omi.ipynb?flush_cache=true):
    - **Main ideas:**
        - Intensive operations that use a lot of RAM memory in the first run when we do not have a file for preprocessed data. After that, the operations are easier and do not require much RAM. Run this notebook in `aerossol` server.
        - Global data `(0.10 x 0.10º)` at `daily` time step from 2004-10-01 until now.
        - Use data for `Southestern Brazil` only.
        - Explore single `HDF5` data file for HCHO in the atmospheric column.
        - Compare data with its uncertainty for a single day.
        - Convert all data files from `HDF5` to `netcdf` if this was not done before.
        - Compare periods of different isolation rates for different years.

- [hcho_tropomi.ipynb](https://nbviewer.jupyter.org/github/SandroAlex/phd/blob/master/notebooks/covid19/hcho_tropomi.ipynb?flush_cache=true):
    - **Main ideas:**
        - Read files that were previously converted from L2 to L3 grid for all periods (P0, P1, P2, P3, P4, P5, and P6) both in 2019 and 2020.
        - Use shape files for municipalities in São Paulo State in order to plot Metropolitan Area of São Paulo (MASP).
        - Use data for São Paulo State only.
        - Compare all periods of different isolation rates for 2019 and 2020.
        - There are no clearly differences between those years for any of the periods in MASP region (see box plots).
    - **References:**
        - [TROPOMI DATA PRODUCTS: Formaldehyde](http://www.tropomi.eu/data-products/formaldehyde).

- [no2_omi.ipynb](https://nbviewer.jupyter.org/github/SandroAlex/phd/blob/master/notebooks/covid19/no2_omi.ipynb?flush_cache=true):
    - **Key ideas:**
        - Exploring global `monthly` gridded `0.10 x 0.10°` L3 NO2 concentration data in South America and Southeastern Brazil. 
        - Is it possible to see the effect of covid19 lockdown in data?

- [no2_omi2.ipynb](https://nbviewer.jupyter.org/github/SandroAlex/phd/blob/master/notebooks/covid19/no2_omi2.ipynb?flush_cache=true):
    - **Main ideas:**
        - Intensive operations that use a lot of RAM memory in the first run when we do not have a file for preprocessed data. After that, the operations are easier and do not require much RAM. Run this notebook in `aerossol` server.
        - Global data `(0.25x0.25º)` at `daily` time step from 2004-10-01 until now.
        - Use data for `Southeastern Brazil` only.
        - Explore single `HDF5` data file for NO2 in the tropospheric column.
        - Differences with and without mask for clouds.
        - Convert all data files from `HDF5` to `netcdf` if this was not done before.
        - Compare periods of different isolation rates for different years.

- [precipitation_chirps.ipynb](https://nbviewer.jupyter.org/github/SandroAlex/phd/blob/master/notebooks/covid19/precipitation_chirps.ipynb?flush_cache=true):
    - Could precipitation explain the differences in air pollution levels during COVID-19 lock down? (apparently it couldn't!)