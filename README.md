# 🔥 BlazeBuster - Fire Weather Index Forecaster

<div align="center">

![Fire Weather Index](https://img.shields.io/badge/Fire%20Weather-Index%20Forecaster-orange)
![Python](https://img.shields.io/badge/Python-3.7+-blue)
![Flask](https://img.shields.io/badge/Flask-2.0+-green)
![License](https://img.shields.io/badge/License-MIT-yellow)

**An intelligent web application for predicting Fire Weather Index (FWI) in Algerian forests using machine learning**

[Live Demo](#demo) • [Features](#features) • [Installation](#installation) • [Usage](#usage) • [API](#api)

</div>

## 📋 Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Technology Stack](#technology-stack)
- [Installation](#installation)
- [Usage](#usage)
- [Model Information](#model-information)
- [Input Parameters](#input-parameters)
- [API Documentation](#api-documentation)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## 🌟 Overview

BlazeBuster is a sophisticated Fire Weather Index (FWI) prediction system designed specifically for Algerian forest fire risk assessment. The application leverages machine learning algorithms to analyze meteorological data and provide accurate fire danger forecasts, helping authorities and researchers make informed decisions about fire prevention and management.

The Fire Weather Index is a crucial metric used by meteorologists and fire management agencies to assess the potential for wildfire occurrence and behavior based on weather conditions.

## ✨ Features

- **🎯 Accurate Predictions**: Uses Ridge Regression model trained on Algerian forest fire data
- **🌐 Web Interface**: Clean, responsive Flask web application
- **📊 Real-time Analysis**: Process meteorological parameters instantly
- **📱 Mobile Friendly**: Responsive design works on all devices
- **🔧 Easy Integration**: RESTful API for integration with other systems
- **📈 Data Visualization**: Clear presentation of prediction results
- **🛡️ Input Validation**: Robust error handling and data validation

## 🛠️ Technology Stack

| Component | Technology |
|-----------|------------|
| **Backend** | Python 3.7+, Flask |
| **Machine Learning** | Scikit-learn, Ridge Regression |
| **Data Processing** | Pandas, NumPy |
| **Frontend** | HTML5, CSS3, JavaScript |
| **Styling** | Custom CSS with Poppins Font |
| **Deployment** | Docker-ready, Cloud-compatible |

## 🚀 Installation

### Prerequisites
- Python 3.7 or higher
- pip (Python package installer)
- Git

### Clone the Repository
```bash
git clone https://github.com/krishnakamalbaishnab/BlazeBuster---Fire-Weather-Index-Forecaster.git
cd BlazeBuster---Fire-Weather-Index-Forecaster
```

### Set Up Virtual Environment (Recommended)
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### Install Dependencies
```bash
pip install -r requirements.txt
```

### Run the Application
```bash
python application.py
```

The application will be available at `http://127.0.0.1:5000/`

## 📖 Usage

### Web Interface
1. Navigate to the home page
2. Click "Try The Prediction Model"
3. Fill in the meteorological parameters:
   - Temperature (°C)
   - Relative Humidity (%)
   - Wind Speed (km/h)
   - Rainfall (mm)
   - FFMC (Fine Fuel Moisture Code)
   - DMC (Duff Moisture Code)
   - ISI (Initial Spread Index)
   - Classes (0 for no fire, 1 for fire)
   - Region (1, 2, or 3)
4. Click "Predict FWI" to get your fire weather index prediction

### API Usage
Send a POST request to `/predcitdata` with form data:

```bash
curl -X POST http://127.0.0.1:5000/predcitdata \
  -d "Temperature=25&RH=60&Ws=15&Rain=0.5&FFMC=85&DMC=45&ISI=10&Classes=1&Region=2"
```

## 🧠 Model Information

### Algorithm
- **Primary Model**: Ridge Regression
- **Preprocessing**: StandardScaler for feature normalization
- **Training Data**: Algerian forest fires dataset
- **Features**: 9 meteorological and environmental parameters

### Model Performance
The model was trained using cross-validation and compared against multiple algorithms:
- Linear Regression
- Lasso Regression
- Ridge Regression (Selected)
- Elastic Net Regression

Ridge Regression was selected based on optimal performance metrics including R² score and Mean Absolute Error.

### Data Preprocessing
- Correlation analysis to remove multicollinear features
- Standard scaling for feature normalization
- Encoding of categorical variables
- Handling of missing values and outliers

## 📊 Input Parameters

| Parameter | Description | Range/Format | Example |
|-----------|-------------|--------------|---------|
| **Temperature** | Air temperature in Celsius | Numeric (°C) | 25.5 |
| **RH** | Relative Humidity | 0-100 (%) | 65 |
| **Ws** | Wind Speed | Positive number (km/h) | 15.2 |
| **Rain** | Rainfall amount | Positive number (mm) | 0.5 |
| **FFMC** | Fine Fuel Moisture Code | 0-100 | 85.2 |
| **DMC** | Duff Moisture Code | Positive number | 45.3 |
| **ISI** | Initial Spread Index | Positive number | 8.7 |
| **Classes** | Fire occurrence indicator | 0 (no fire) or 1 (fire) | 1 |
| **Region** | Geographic region | 1, 2, or 3 | 2 |

## 🔌 API Documentation

### Endpoints

#### `GET /`
Returns the main landing page.

#### `GET /home`
Returns the prediction form page.

#### `POST /predcitdata`
Predicts Fire Weather Index based on input parameters.

**Request Format:**
```
Content-Type: application/x-www-form-urlencoded

Temperature=25&RH=60&Ws=15&Rain=0.5&FFMC=85&DMC=45&ISI=10&Classes=1&Region=2
```

**Response:**
Returns HTML page with prediction result displayed.

## 📁 Project Structure

```
BlazeBuster---Fire-Weather-Index-Forecaster/
├── application.py              # Main Flask application
├── requirements.txt           # Python dependencies
├── LICENSE                   # MIT License
├── README.md                # Project documentation
├── models/                  # Trained ML models
│   ├── ridge.pkl           # Ridge regression model
│   └── scaler.pkl          # StandardScaler for preprocessing
├── notebooks/              # Jupyter notebooks and analysis
│   ├── eda.py             # Exploratory Data Analysis
│   └── model.py           # Model training and evaluation
├── static/                # Static web assets
│   ├── fireLogo.png      # Application logo
│   ├── graphImage.png    # Dashboard visualization
│   ├── phoneImage.png    # Mobile app mockup
│   ├── script.js         # JavaScript functionality
│   └── styles.css        # CSS styling
└── templates/            # HTML templates
    ├── index.html       # Landing page
    └── home.html        # Prediction form page
```

## 🤝 Contributing

We welcome contributions from the community! Here's how you can help:

1. **Fork the repository**
2. **Create a feature branch**: `git checkout -b feature/your-feature-name`
3. **Make your changes**
4. **Add tests if applicable**
5. **Commit your changes**: `git commit -m 'Add some feature'`
6. **Push to the branch**: `git push origin feature/your-feature-name`
7. **Submit a pull request**

### Development Guidelines
- Follow PEP 8 style guidelines for Python code
- Add comments for complex logic
- Update documentation for new features
- Test your changes thoroughly

## 🐛 Issues and Support

If you encounter any issues or have questions:
1. Check the [Issues](https://github.com/krishnakamalbaishnab/BlazeBuster---Fire-Weather-Index-Forecaster/issues) page
2. Create a new issue with detailed description
3. Include steps to reproduce the problem

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Dataset**: Algerian Forest Fires Dataset
- **Libraries**: Scikit-learn, Flask, Pandas, NumPy
- **Inspiration**: Forest fire prevention and management research
- **Contributors**: Open source community

## 📧 Contact

For questions or collaboration opportunities:
- **GitHub**: [krishnakamalbaishnab](https://github.com/krishnakamalbaishnab)
- **Project Link**: [BlazeBuster Repository](https://github.com/krishnakamalbaishnab/BlazeBuster---Fire-Weather-Index-Forecaster)

---

<div align="center">

**⭐ Star this repository if you found it helpful!**

Made with ❤️ for forest fire prevention

</div>
