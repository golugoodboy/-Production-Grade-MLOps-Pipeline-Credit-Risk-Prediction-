from src.data_preprocessing import load_data, preprocess_data
from src.train import train_model, save_model
from src.evaluate import evaluate_model
import mlflow

url = r"C:\Users\Goludev\Desktop\langchain\ml_ops_project\data\credit_risk_dataset.csv"

df = load_data(url)

df = preprocess_data(df)

with mlflow.start_run():    
    model, x_test, y_test = train_model(df)

    evaluate_model(model, x_test, y_test)

save_model(model)

