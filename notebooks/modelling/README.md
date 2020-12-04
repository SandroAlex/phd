# Description

## Overview

Using machine learning to better understand biosphere-atmosphere interactions in South America.

## Better visualization

- [ndvi_trends_gbrt_xgboost.ipynb](https://nbviewer.jupyter.org/github/SandroAlex/phd/blob/master/notebooks/modelling/ndvi_trends_gbrt_xgboost.ipynb?flush_cache=true):
    - **Key ideas:**
        - Learning some cool things. Just a test!
        - Intensive time consuming operations that use a lot of RAM memory when doing hyper parameter grid search with Bayesian optimization. Run this notebook in aerossol server.
        - The target is given by the decadal variations of NDVI (trends). The initial features obtained here are the following: 
            - (01) `LAT` Latitude; 
            - (02) `LON` Longitude; 
            - (03) `ELEV` Elevation; 
            - (04) `LC` Land class for 2015;
            - (05) `LC` Counts of annual land class changes from 2001 until 2015;
            - (06) `P` Mean precipitation;
            - (07) `P` Standard deviation of precipitation;
            - (08) `P` Long term trends of precipitation;
            - (09) `TMAX` Mean maximum 2-m temperature;
            - (10) `TMAX`Standard deviation of maximum 2-m temperature;
            - (11) `TMAX`Long term trends of maximum 2-m temperature;
            - (12) `TMIN` Mean minimum 2-m temperature;
            - (13) `TMIN` Standard deviation of minimum 2-m temperature;
            - (14) `TMIN` Long term trends of minimum 2-m temperature;
            - (15) `SRAD` Mean downward shortwave radiation flux at the surface;
            - (16) `SRAD` Standard deviation of downward shortwave radiation flux at the surface;
            - (17) `SRAD` Long term trends of downward shortwave radiation flux at the surface;
            - (18) `PDSI` Mean Palmer drought severity index;
            - (19) `PDSI` Standard deviation of Palmer drought severity index;
            - (20) `PDSI` Long term trends of Palmer drought severity index;
            - (21) `NDVI` Mean NDVI;
            - (22) `NDVI` Standard deviation of NDVI.
        - Use Ridge Regression (RR) as a simple benchmark, optimized with exhaustive grid search over hyper parameters.
        - Use Gradient Boosted Regression Trees (XGBRT) from [XGBoost](https://xgboost.readthedocs.io/en/latest/python/python_api.html) ([Scikit-Learn API](https://xgboost.readthedocs.io/en/latest/python/python_api.html#module-xgboost.sklearn)) with Bayesian optimization over hyper parameters. 
        - Here we analyze a reduced version of the data set: only instances with statistical significance in NDVI trends, which gives us approximately 5 % of rows in the original matrix.
        - All performance metrics are based on R2 score. 
        - Permutation feature importances for XGBRT model.
        - Partial dependence plots for XGBRT model.
    - **Notes:** 
        - Note that partial dependence plots assume that the target features are independent from the complement features, and this assumption is often violated in practice.
    - **References:**
        - Natekin, A. and Knoll, A. (2013). [Gradient boosting machines, a tutorial](https://www.frontiersin.org/articles/10.3389/fnbot.2013.00021/full). Frontiers in neurorobotics, 7:21.
        - [Sckit-Learn: Exhaustive search over specified parameter values for an estimator](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html).
        - [Sckit-Learn: Column Transformer with Mixed Types](https://scikit-learn.org/stable/auto_examples/compose/plot_column_transformer_mixed_types.html).
        - [XGBoost Parameters](https://github.com/dmlc/xgboost/blob/master/doc/parameter.rst).
        - [Scikit-Optimize: Scikit-learn hyperparameter search wrapper](https://scikit-optimize.github.io/stable/auto_examples/sklearn-gridsearchcv-replacement.html#sphx-glr-auto-examples-sklearn-gridsearchcv-replacement-py).
