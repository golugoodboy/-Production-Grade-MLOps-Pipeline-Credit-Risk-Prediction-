# 🚀 Production-Grade MLOps Pipeline (Credit Risk Prediction)

## 📌 Overview

This project implements an end-to-end MLOps pipeline for predicting loan default risk, including training, experiment tracking, deployment, monitoring, and automated retraining.

---

## 🧠 Key Features

* 🔹 End-to-End ML Pipeline (Data → Training → Deployment)
* 🔹 Experiment Tracking using MLflow
* 🔹 Production API using FastAPI
* 🔹 Dockerized for portability
* 🔹 Data Drift Detection using Evidently AI
* 🔹 Automated Retraining Pipeline
* 🔹 Training-Serving Consistency using sklearn Pipeline

---

## 🏗️ Tech Stack

* Python
* Scikit-learn
* MLflow
* FastAPI
* Docker
* Evidently AI
* Pandas

---

## ⚙️ Project Workflow

1. Data Preprocessing
2. Model Training & Evaluation
3. Experiment Tracking (MLflow)
4. Model Deployment (FastAPI)
5. Containerization (Docker)
6. Drift Detection
7. Auto Retraining

---

## 🚀 How to Run

### 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/mlops-credit-risk.git
cd mlops-credit-risk
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Run API

```bash
uvicorn app:app --reload
```

### 4️⃣ Open API Docs

```
http://127.0.0.1:8000/docs
```

---

## 🐳 Run with Docker

```bash
docker build -t mlops-project .
docker run -p 8000:8000 mlops-project
```

---

## 📊 Drift Detection

```bash
python src/drift_detection.py
```

---

## 🔄 Retraining Pipeline

```bash
python src/retrain.py
```

---

## 💼 Resume Highlights

* Built production-grade ML system with deployment, monitoring, and retraining
* Ensured training-serving consistency using sklearn pipelines
* Implemented experiment tracking and model versioning with MLflow

---

## 📌 Future Improvements

* CI/CD pipeline (GitHub Actions)
* Cloud deployment (AWS/GCP)
* Feature store integration

---

## 🤝 Contributing

Pull requests are welcome!

---

## ⭐ If you like this project, give it a star!

