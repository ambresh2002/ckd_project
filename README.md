# 🩺 Chronic Kidney Disease (CKD) Prediction and Stage Classification System

A Machine Learning-based solution for predicting Chronic Kidney Disease (CKD) and classifying its stages using clinical data. This project leverages feature selection techniques and classification models to assist healthcare professionals in early detection and personalized treatment planning for CKD patients.

---

## 🔍 Project Overview

This system performs:
- **CKD Detection**: Binary classification to determine whether a patient has CKD.
- **CKD Stage Classification**: Multi-class classification to identify CKD stages (1 to 5).
- **Feature Selection**: Identifies the most important clinical features contributing to predictions using the Random Forest algorithm.

---

## 💡 Key Features

- Clinical data-based prediction
- Feature importance ranking
- Dual classification (CKD Y/N and CKD Stage)
- Evaluation using Accuracy, Precision, Recall, and F1 Score
- (Optional) Web interface for real-time input and predictions

---

## 🧾 Dataset Details

The dataset includes anonymized patient information with the following features:

### 🧬 Features:
['Id', 'Age', 'Serum_Creatinine', 'BUN', 'Specific_Gravity', 'Albumin', 'Sodium', 'Potassium',
'Hemoglobin', 'WBC', 'RBC', 'CAD', 'Systolic_BP', 'Diastolic_BP', 'Anemia', 'GFR',
'CKD (Y/N)', 'CKD Stage']


- **Target 1**: `CKD (Y/N)` – Binary classification
- **Target 2**: `CKD Stage` – Multi-class classification (Stage 1 to 5)

---

## 🛠️ Tech Stack

- **Programming Language**: Python
- **ML Libraries**: Scikit-learn, Pandas, NumPy
- **Visualization**: Matplotlib, Seaborn
- **Model Deployment (Optional)**: Django / Flask
- **Model Serialization**: Joblib

---

## 🔢 Machine Learning Techniques Used

### 1. **Feature Selection**
- **Algorithm**: Random Forest
- **Purpose**: Selects top clinical features based on impurity-based feature importance (Gini Importance)

### 2. **Model Building**
- **CKD Detection**: Random Forest Classifier
- **Stage Classification**: Random Forest Classifier (Multi-class)

### 3. **Evaluation Metrics**
- **Accuracy**: Ratio of correct predictions
- **F1 Score**: Harmonic mean of Precision and Recall
- **Confusion Matrix**: Visual analysis of classification performance

---

## 📊 Example Results

| Task                     | Accuracy | F1 Score |
|--------------------------|----------|----------|
| CKD Prediction (Y/N)     | 96.2%    | 0.95     |
| CKD Stage Classification | 89.7%    | 0.88     |

---

## 🚀 Getting Started

### ✅ Prerequisites

Make sure you have Python 3.x installed. You may use a virtual environment.

### 🔧 Installation

```bash
git clone https://github.com/ambresh2002/ckd-prediction.git
cd ckd-prediction
pip install -r requirements.txt

#Running the below comment to run on bash
python ckd_model.py

# For Django
python manage.py runserver

# For Flask
python app.py
ckd_project/
│
├── ckd_app/                  # Django app with views, models, urls
├── templates/                # HTML templates (predict.html, result.html)
├── static/                   # CSS, JS, Images
├── rf_ckd_model.pkl          # CKD classifier model
├── rf_stage_model.pkl        # CKD stage classifier model
├── scaler.pkl                # Scaler used for normalization
├── manage.py
└── requirements.txt

📌 Future Enhancements
📱 Mobile App version

🔗 Integration with EHR systems

🧠 Deep Learning models for advanced predictions

👨‍⚕️ Real-world clinical testing
<img width="1366" height="664" alt="screencapture-127-0-0-1-8000-l<img width="1366" height="1118" alt="screencapture-127-0-0-1-8000-predict-2025-02-26-10_46_24" src="https://github.com/user-attachments/assets/bff5eabc-e158-4278-a9d8-9d3bae991df0" />
<img width="1366" height="1147" alt="screencapture-127-0-0-1-8000-predict-2025-02-26-10_44_40" src="https://github.com/user-attachments/assets/7e3faaaf-aba8-421d-a60d-2e40fb6da9cb" />
<img width="1366" height="1060" alt="screencapture-127-0-0-1-8000-predict-2025-02-26-10_39_02" src="https://github.com/user-attachments/assets/bf1276e3-266b-45aa-b740-cef2a62fcc71" />
<img width="1366" height="698" alt="screencapture-127-0-0-1-8000-signup-2025-07-29-10_29_07" src="https://github.com/user-attachments/assets/42268395-9b27-40d9-accc-edc52028420e" />
<img width="1366" height="664" alt="screencapture-127-0-0-1-8000-login-2025-07-29-10_28_33" src="https://github.com/user-attachments/assets/d67076fa-787d-4f9b-a223-9fbb95e0cc04" />
<img width="1366" height="1300" alt="screencapture-127-0-0-1-8000-2025-07-29-10_27_57" src="https://github.com/user-attachments/assets/09dfd4a9-09a7-4b65-a185-8efb4be5e944" />
ogin-2025-07-29-10_28_33" src="https://github.com/user-attachments/assets/783c09c7-466d-4396-bbd6-41cbbdb665e7" />


