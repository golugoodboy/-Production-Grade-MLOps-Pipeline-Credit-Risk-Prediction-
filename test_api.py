import requests

url = "http://localhost:8000/predict"

data = {
  "person_age": 25,
  "person_income": 50000,
  "person_home_ownership": "RENT",
  "person_emp_length": 2,
  "loan_intent": "EDUCATION",
  "loan_grade": "A",
  "loan_amnt": 10000,
  "loan_int_rate": 12.5,
  "loan_percent_income": 0.2,
  "cb_person_default_on_file": "N",
  "cb_person_cred_hist_length": 5
}

response = requests.post(url, json = data)

print(response.json())