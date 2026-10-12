# Use Case 22 — Warehouse Efficiency Insight

## Scope
Round 2 (EDA & feature engineering) and Round 3 (Excel analysis), with supplementary ML and pitch materials. Quiz excluded.

## Critical data note
The uploaded CH22.pdf describes `orders.csv`, `picks.csv`, `items.csv`, `workers.csv`, and `zones.csv` but did not include the actual CSV files. The `data/` CSVs in this bundle are **synthetic demonstration data**, created to exercise the required workflow. If your instructor supplied official CSVs separately, replace these files and rerun the notebook before submitting numerical findings.

## Files
- `data/`: five raw demonstration CSVs
- `outputs/cleaned_warehouse_picks.csv`: combined cleaned analysis table
- `outputs/Warehouse_Efficiency_Analysis.xlsx`: executive summary, analysis sheets, charts, cleaned data
- `outputs/Ready_to_Submit_Report.docx`: structured write-up with metrics and caveat
- `outputs/Warehouse_Insights_Pitch.pptx`: optional short presentation
- `notebooks/warehouse_efficiency_eda_ml.ipynb`: EDA, preprocessing, feature engineering, regression
- `src/train_model.py`: standalone supplementary ML training script
- `outputs/*.png`: selected visualizations
- `outputs/*summary.csv`: analysis summaries
- `outputs/feature_importance.csv`: model feature importance

## Model
Random Forest Regressor predicts `pick_duration_min`; report MAE, RMSE and R² on a held-out 20% test split. Metrics are synthetic-data demonstration results only.

## How to run
Install dependencies from `requirements.txt`, then open the notebook from the `notebooks/` folder. Paths are relative to the notebook. Use a Python environment with pandas, numpy, scikit-learn, matplotlib, openpyxl, nbformat, python-docx, and python-pptx.
