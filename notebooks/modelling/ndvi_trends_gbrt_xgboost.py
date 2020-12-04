#!/usr/bin/env python

"""
Faz praticamente a mesma coisa que o notebook de nome correspondente. Leva 
muitas horas para rodar esse script. Aqui é encontrado o melhor modelo possível.
"""

# =========================== Initial setup ===================================
print("\n>>> Initial setup ...")
# Load packages.
import sys
import warnings 
import joblib 

import pandas as pd
import xgboost as xgb

from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
from skopt import BayesSearchCV
from skopt.space import Real, Categorical, Integer

warnings.filterwarnings("ignore")

# Significance global threshold (decadal variation).
u = 0.0192

# =========================== Load data matrix ================================
print("\n>>> Load data matrix ...")
# Data file path.
ppdatafp = "/work/sandroal/data_sets/FEATURES/ndvi_trends.csv"

# Load data in a pandas DataFrame object.
df_matrix = pd.read_csv(ppdatafp)

# =========================== Preprocess and split data =======================
print("\n>>> Preprocess and split data ...")
# Numeric data (float and int). 
numeric_features = [
    "lclass_2001_2015_dcount",
    "lat", "lon", "elev", 
    "p_mean", "p_std", "p_slope",
    "tmax_mean", "tmax_std", "tmax_slope",
    "tmin_mean", "tmin_std", "tmin_slope", 
    "srad_mean", "srad_std", "srad_slope", 
    "pdsi_mean", "pdsi_std", "pdsi_slope", 
    "ndvi_mean", "ndvi_std"
]

# Categorical data.
categorical_features = ["lclass_2015"]

# Target.
target = ["ndvi_slope"]

# Inputs.
features = categorical_features + numeric_features

# For tree-based models it is not necessary to scale data. 
# We do it here just for learning purposes.
numeric_transformer = Pipeline(
    steps=[("scaler", StandardScaler())] 
)

# One hot encoding.
categorical_transformer = Pipeline(
    steps=[("onehot", OneHotEncoder())]
)

# Column-wise transformations by feature type.
preprocessor = ColumnTransformer(
    transformers=[("numeric", numeric_transformer, numeric_features),
                  ("categorical", categorical_transformer, categorical_features)]
)

# Reduce number of instances: only trends with statistical significance
mask_stat_sig = df_matrix.ndvi_slope.abs() >= u
df_matrix = df_matrix[mask_stat_sig]

# Simple train-test split as pandas DataFrame objects.
df_x_train, df_x_test, df_y_train, df_y_test = train_test_split(
    df_matrix[features], 
    df_matrix[target], 
    test_size=0.3, 
    stratify=df_matrix.lclass_2015
)

# =========================== Train XGBRT model ===============================
print("\n>>> Train XGBRT model ...")
# Append model to preprocessing pipeline. Now we have a full prediction pipeline.
model_xgbrt = Pipeline(
    steps=[("preprocessor", preprocessor),
           ("model", xgb.XGBRegressor())]
)

# Bayesian optimization over hyperparameters. Search for the best model.
search_xgbrt = BayesSearchCV(
    estimator=model_xgbrt,
    search_spaces={
        "model__n_estimators": Integer(low=500, high=3000, prior="uniform"),
        "model__max_depth": Integer(low=1, high=30, prior="uniform"),
        "model__learning_rate": Real(low=0.001, high=1.000, prior="log-uniform"),
        "model__objective": Categorical(["reg:pseudohubererror", "reg:squarederror"]),
        "model__subsample": Real(low=0.05, high=0.95, prior="log-uniform"),
        "model__lambda": Real(low=1, high=1000, prior="log-uniform"),
        "model__alpha": Real(low=1, high=1000, prior="log-uniform"),
    },
    n_iter=2800, #2800
    scoring="r2",
    n_jobs=-1,
    n_points=7,
    cv=5,
    verbose=1,
    return_train_score=True
)

print("\n>>> Total iterations (it will take to explore all subspaces):", 
      search_xgbrt.total_iterations)

# Run fit with all sets of parameters.
_ = search_xgbrt.fit(df_x_train, df_y_train)

# Now we have the following results.
print("\n>>> Results for best hyper parameters:")
df = pd.DataFrame(search_xgbrt.cv_results_)
print(df.iloc[search_xgbrt.best_index_])

# Optimum hyper parameter set.
print("\n>>> Best hyper parameters:")
print("*", search_xgbrt.best_params_)

# =========================== Export XGBRT model ==============================
print("\n>>> Export XGBRT model ...	")

# Where to find it.
file_path = "/work/sandroal/trained_models/xgbrt_ndvi_trends.joblib"

# Export model.
joblib.dump(
    value=search_xgbrt.best_estimator_,
    filename=file_path
)

print("\n>>> Exported model to:", file_path)

# Load it again.
final_model = joblib.load(file_path)

# Show it.
print("\n>>> Final model:")
print(final_model)
