# 📄 Model Card: Rain Tomorrow Predictor

## 1. Model Details

* **Model Type**: Gradient Boosting Classifier
* **Algorithm**: LightGBM (Light Gradient Boosting Machine)
* **Optimization**: Bayesian Optimization using Optuna
* **Trained By**: Data Scope (ChatGPT-guided project)
* **License**: MIT License
* **Date Created**: June 2025

---

## 2. Intended Use

* **Primary Purpose**: Predict whether it will rain tomorrow based on weather data.
* **Intended Users**: Meteorological enthusiasts, data science learners, early-stage weather prediction systems.
* **Use Cases**:

  * Educational demo on model deployment
  * Probabilistic weather forecasting
  * ML operations (MLOps) tutorial on app building

---

## 3. Training Data

* **Dataset Source**: [Rain in Australia](https://www.kaggle.com/datasets/jsphyg/weather-dataset-rattle-package)
* **Number of Features**: 21
* **Target Variable**: `RainTomorrow` (Yes/No)
* **Preprocessing Steps**:

  * Missing value imputation
  * Label encoding for categorical features
  * Train/test split (80/20)
  * Feature scaling (if needed)

---

## 4. Performance

* **Metric Used**: AUC (Area Under ROC Curve)
* **Validation AUC**: \~0.89
* **Evaluation Tools**: `classification_report`, `confusion_matrix`, ROC Curve

---

## 5. Limitations

* Assumes similar weather pattern distributions as training data
* Sensitive to missing or incorrectly entered feature values
* Categorical encoding is simplistic (no target encoding or embeddings)

---

## 6. Ethical Considerations

* This model should not be used for high-stakes decision-making
* Does not factor in regional weather anomalies or real-time satellite input

---

## 7. Caveats and Recommendations

* Users must ensure that input values are within realistic weather ranges.
* Recommended for demonstration or prototyping use only.
* Retrain periodically if applying to live weather feeds.

---

## 8. Model Versioning

* **Version**: v1.0
* **Last Updated**: June 2025
* **Framework Version**: LightGBM 4.3+, Streamlit 1.35+, Optuna 3.6+
