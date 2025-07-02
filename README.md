# 🌧️ Rain Tomorrow Prediction App

This project is a machine learning-powered web application built using **Streamlit** that predicts whether it will rain tomorrow based on various weather conditions.

## 📌 Project Overview

The goal of this project is to make an accurate **binary prediction** (`Yes` or `No`) on whether it will rain the next day, using a dataset of weather observations. The model was trained using **LightGBM**, with hyperparameters optimized using **Optuna** and **Bayesian Optimization**.

---

## 🚀 Features

- Interactive web interface for user inputs
- Handles all 21 relevant weather features
- Makes real-time predictions
- Custom background and dark UI theme
- Deployable and lightweight

---

## ⚙️ Technologies Used

| Tool/Library     | Purpose                            |
|------------------|-------------------------------------|
| Python           | Programming language                |
| Pandas           | Data preprocessing                  |
| LightGBM         | Gradient Boosting classifier        |
| Optuna           | Bayesian Hyperparameter Optimization|
| Streamlit        | Web UI framework                    |
| joblib           | Model serialization/deserialization |

---

## 📂 Dataset

- Source: [Rain in Australia – Kaggle](https://www.kaggle.com/datasets/jsphyg/weather-dataset-rattle-package)
- Features: 21 (weather measurements such as temperature, rainfall, wind, humidity, etc.)
- Target: `RainTomorrow` (`Yes` / `No`)

---

## 🧠 Model Training & Optimization

- Used LightGBM for classification
- Performed Bayesian Optimization with Optuna to tune:
  - `learning_rate`, `num_leaves`, `max_depth`, `scale_pos_weight`, etc.
- Achieved AUC score of ~0.89

---
