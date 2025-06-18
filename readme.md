# 🚀 Asteroid Hazard Prediction Using Machine Learning

## 📅 Project Overview
This project aims to predict whether a near-Earth object (NEO) is potentially hazardous based on its physical and orbital parameters. 
The focus was to build a deployable machine learning model that handles severe class imbalance and achieves high recall for hazardous predictions.

---

## 🔎 Problem Statement
**Objective:** Classify asteroids as `hazardous (1)` or `non-hazardous (0)`.

**Features Used:**
- Estimated Diameter (km)
- Velocity (km/h)
- Distance from Earth (km)

**Target Variable:**
- `is_hazardous` (binary classification)

**Challenge:**
- Highly imbalanced dataset (this is because hazardous objects are rare but crucial to detect)

---

## 🚀 Key Features

### ⚖️ Feature Engineering
- Derived a new metric called `risk_score`:  
  \[(diameter \u00d7 velocity\u00b2) / distance\]
- Normalized using `MinMaxScaler` for consistent input distribution.

### ⚖️ Handling Imbalanced Data
- Used **SMOTE (Synthetic Minority Oversampling Technique)** to balance classes in training data.
- Test data remains untouched to simulate real-world distributions.

### 📈 Model Building
- Used **Pipeline** with the following steps:
  - MinMaxScaler
  - SMOTE
  - Logistic Regression (`class_weight='balanced'`)
- Evaluated using:
  - Confusion Matrix
  - Classification Report
  - ROC-AUC
  - Precision-Recall Curves

### ⚖️ Threshold Tuning
- Analyzed precision-recall vs. threshold to optimize decision boundary.
- Applied a custom threshold to minimize false negatives.

---

## 🚀 Model Performance
- **ROC-AUC:** `0.96`
- **Accuracy:** `94.4%` (after threshold tuning)
- Strong recall for the hazardous class with low false negatives

---

## 🔧 Tools & Libraries
- Python 
- scikit-learn
- imbalanced-learn
- matplotlib
- joblib
-- Jules by Google, for the web application

---

## 📁 Main files: 
```bash
.
├── asteroid_model.ipynb        # Main training & evaluation notebook
├── logistic_pipeline.pkl       # Saved pipeline (scaler + SMOTE + model)
├── threshold.pkl               # Saved optimal threshold
├── predictor.py                # Deployment-ready script with prediction function
├── README.md                   # Project documentation
```

---

## 🚀 Usage (Deployment Script)

```python
cd into web app:
then python app.py
```

---

## 🎓 What I Learned
- End-to-end machine learning pipeline creation
- Handling real-world challenges like class imbalance
- Threshold tuning for maximizing model effectiveness
- Preparing ML models for deployment (joblib, clean API, feature handling)

---

## 🙌 Future Work
- Experiment with ensemble models (Random Forest, XGBoost)
- Connect to NASA API for real-time NEO prediction

---

## 📢 Contact
**Author:** Gautum Vaisiam Parambil  
**Email:** gautumsvp@gmail.com


---

## 💊 Acknowledgements
- Dataset sourced from Nasa (https://data.nasa.gov/dataset/asteroids-neows-api)
- Thanks to open-source libraries that made this project possible

---

