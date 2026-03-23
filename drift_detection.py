import pandas as pd
from evidently.report import Report
from evidently.metric_preset import DataDriftPreset, DataQualityPreset
import os

def detect_drift(reference_data: pd.DataFrame, current_data: pd.DataFrame, report_path: str = "drift_report.html"):
    """
    Compares two datasets to detect statistical drift and data quality issues.
    
    Returns:
        bool: True if dataset-level drift is detected, False otherwise.
    """
    print(f"Analyzing drift between {len(reference_data)} reference rows and {len(current_data)} current rows...")
    
    # 1. Create a Report object
    report = Report(metrics=[
        DataDriftPreset(),
        DataQualityPreset()
    ])

    # 2. Run the analysis
    report.run(reference_data=reference_data, current_data=current_data)

    # 3. Save the interactive HTML report
    report.save_html(report_path)
    
    # 4. Extract the result (New!)
    # We turn the report into a dictionary to grab the "dataset_drift" status
    result = report.as_dict()
    drift_detected = result["metrics"][0]["result"]["dataset_drift"]
    
    if drift_detected:
        print("🚨 DRIFT DETECTED: The data distribution has changed significantly.")
    else:
        print("✅ NO DRIFT: The data remains statistically stable.")

    print(f"Detailed report saved to: {os.path.abspath(report_path)}")
    
    return drift_detected

if __name__ == "__main__":
    # --- EXAMPLE USAGE FOR LEARNING ---
    # This block only runs if you execute this file directly: python drift_detection.py
    
    data_path = "data/credit_risk_dataset.csv"
    
    if os.path.exists(data_path):
        # Load the original data
        df = pd.read_csv(data_path)
        
        # Split the data to simulate "Reference" vs "Current"
        # In a real app, 'current_data' would be the new data you've collected from users.
        reference = df.sample(n=5000, random_state=42)
        current = df.sample(n=5000, random_state=10) # Using a different seed to simulate slight changes
        
        detect_drift(reference, current)
    else:
        print(f"Error: Could not find {data_path}. Please make sure you are in the project root.")
