import pandas as pd
from drift_detection import detect_drift
import os

# 1. Load your Golden Reference (Training Data)
reference_path = "data/credit_risk_dataset.csv"
if not os.path.exists(reference_path):
    print(f"Error: Could not find reference data at {reference_path}")
    exit()

reference_df = pd.read_csv(reference_path)

# 2. Load your Production Data (Captured Data)
current_path = "captured_data.csv"
if not os.path.exists(current_path):
    print(f"Info: No production data captured yet! Run some predictions through the API first.")
    exit()

current_df = pd.read_csv(current_path)

# 3. Run Drift Detection
# We compare the training data with our fresh production data.
detect_drift(reference_data=reference_df, current_data=current_df, report_path="production_drift_report.html")

print("\n--- Summary ---")
print(f"Reference Rows: {len(reference_df)}")
print(f"Captured Rows: {len(current_df)}")
print("Open production_drift_report.html to see the results!")
