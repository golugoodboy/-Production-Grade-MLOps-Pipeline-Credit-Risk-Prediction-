import mlflow
import joblib

runs = mlflow.search_runs(order_by = ["metrics.accuracy DESC"])

best_run = runs.iloc[0]
print(best_run)

run_id = best_run.run_id
print("Best run id : ", run_id)

print("making a model now")

model = mlflow.sklearn.load_model(f"runs:/{run_id}/model")

joblib.dump(model, "best_model.pkl")
print("Model saved to best_model.pkl")



