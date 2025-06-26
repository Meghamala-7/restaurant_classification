# 🍽️ Restaurant Recommendation Web App

This is a machine learning-based web application that helps users find restaurants based on selected **Country Code**, **City**, and **Cuisine**. It uses a **Random Forest Classifier** trained on real-world restaurant data.

---

## 🔍 Features

- 🔄 **Cascading dropdowns** for Country → City → Cuisine
  
- 🎯 **ML-powered filtering** using Random Forest
  
- 🖼️ Cuisine-based image display with fallback
  
- 📋 Stylish **card layout** for restaurant results

- 🎨 Clean and responsive UI with background images

---

## 📁 Folder Structure

restaurant-app/

├── app.py

├── dataset.csv

├── static/

│ ├── style.css

│ └── images/

│ ├── background.jpg

│ ├── background_results.jpg

│ ├── north_indian.jpg

│ ├── italian.jpg

│ ├── default.jpg

│ └── ... (other cuisines)

├── templates/

│ ├── index.html

│ └── results.html


## install dependencies

pip install flask pandas scikit-learn


## run app using

python app.py


##  Machine Learning Details

Model: RandomForestClassifier

Target: Predict Country Code based on City and Cuisine

Preprocessing:

Label Encoding for City and Cuisine

Missing value removal

Filtering Logic:

User selects Country → City → Cuisine

Model predicts likely country

Restaurants are filtered by actual match from dataset

## tech used

frontend: HTML, CSS, JavaScript

backend: Flask, python

