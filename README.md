# BlazeBuster - Fire Weather Index Forecaster
Introduction

BlazeBuster is a web application designed to predict the Fire Weather Index (FWI), a critical metric for assessing wildfire danger. It leverages machine learning models to analyze real-time meteorological data and provide valuable insights into potential fire risks.

# Key Features

- Accurate FWI Prediction:
- Utilizes Linear Regression and Ridge Regression models for robust predictions.
- User-Friendly Interface: Built with Flask, offering a simple and intuitive web interface for data input and FWI display.

#Comprehensive Data Preprocessing:

-Performs Exploratory Data Analysis (EDA) to understand data distribution.
-Cleans data to handle missing values and outliers.
-Employs standard scaling for data normalization.

# Real-time Integration:

Designed to integr-ate with real-time meteorological data sources (implementation not included).

# Informative Visualizations:

Presents predicted FWI values alongside relevant information in clear visualizations.


# Technical Stack

-Web Framework: Flask
-Programming Language: Python
-Machine Learning Library: Scikit-learn
-Data Visualization Libraries (Optional): Matplotlib, Seaborn


# Getting Started

### Clone the Repository:

```Bash

git clone https://github.com/krishnakamalbaishnab/BlazeBuster.git

```

### Set Up Environment:

- Create a virtual environment (recommended for managing dependencies).

Install required packages:

```Bash

pip install -r requirements.txt
```

### Run the Application:

Start the Flask development server:

```Bash

python app.py
```

### Access the application in your web browser at http://127.0.0.1:5000/.

Contributing

We welcome contributions from the open-source community! Feel free to:

Fork the repository
Experiment with the code
Submit pull requests with improvements
License

This project is licensed under the MIT License.

Acknowledgements

We would like to thank [contributors and organizations] for their contributions to this project. (Replace with the actual names if applicable)