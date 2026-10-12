"""
Warehouse Efficiency Insight — supplementary ML analysis.
Synthetic demonstration dataset generated because source CSVs were not included in CH22.pdf.
"""
import math
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

df = pd.read_csv("../outputs/cleaned_warehouse_picks.csv")
features = ['quantity', 'item_count', 'priority', 'zone', 'zone_type', 'distance_band', 'category', 'size', 'storage_class', 'shift', 'experience_band', 'order_size_band', 'start_hour']
target = "pick_duration_min"
X, y = df[features], df[target]
numeric = ["quantity", "item_count", "start_hour"]
categorical = [c for c in features if c not in numeric]
prep = ColumnTransformer([
    ("num", Pipeline([("imputer", SimpleImputer(strategy="median"))]), numeric),
    ("cat", Pipeline([("imputer", SimpleImputer(strategy="most_frequent")), ("onehot", OneHotEncoder(handle_unknown="ignore"))]), categorical)
])
model = Pipeline([("prep", prep), ("model", RandomForestRegressor(n_estimators=180, min_samples_leaf=3, random_state=22, n_jobs=-1))])
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=22)
model.fit(X_train, y_train)
pred = model.predict(X_test)
print("MAE (minutes):", round(mean_absolute_error(y_test, pred), 2))
print("RMSE (minutes):", round(math.sqrt(mean_squared_error(y_test, pred)), 2))
print("R2:", round(r2_score(y_test, pred), 3))
