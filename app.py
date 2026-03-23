from fastapi import FastAPI
import joblib
import pandas as pd 

app = FastAPI()

model = joblib.load("pipeline_model.pkl")

@app.get("/")
def home():
    return {"message": "Welcome to the Loan Default Prediction API"}

import os

@app.post("/predict")
def predict(data : dict):
    # 1. Create DataFrame from input
    df = pd.DataFrame([data])
    
    # 2. Log data for Drift Detection (New!)
    log_file = "captured_data.csv"
    # If the file doesn't exist, we write the header. If it does, we append without the header.
    df.to_csv(log_file, mode='a', header=not os.path.exists(log_file), index=False)
    
    # 3. Handle data types for the model
    num_cols = [
        'person_age', 'person_income', 'person_emp_length', 
        'loan_amnt', 'loan_int_rate', 'loan_percent_income', 
        'cb_person_cred_hist_length'
    ]
    for col in num_cols:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors='coerce')
    
    print(f"Captured 1 row of data to {log_file}")
    
    # 4. Predict
    prediction = model.predict(df)[0]

    return {"prediction" : int(prediction)}


#run the app
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="[IP_ADDRESS]", port=8000)


#to run the app
#uvicorn app:app --reload