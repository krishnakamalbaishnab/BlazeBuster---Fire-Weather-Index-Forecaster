from flask import Flask, jsonify, render_template, request, url_for, flash, redirect
import pickle
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
import os

# Initialize Flask application
application = Flask(__name__)
app = application
app.secret_key = 'your-secret-key-here'  # Change this in production

# Load the trained models
try:
    ridge_model = pickle.load(open("models/ridge.pkl", 'rb'))
    standard_scaler = pickle.load(open("models/scaler.pkl", 'rb'))
    print("Models loaded successfully!")
except Exception as e:
    print(f"Error loading models: {e}")
    ridge_model = None
    standard_scaler = None

@app.route("/")
def index():
    """Render the main landing page"""
    return render_template('index.html')

@app.route("/home")
def home():
    """Render the prediction form page"""
    return render_template('home.html')

@app.route("/predictdata", methods=["GET", "POST"])
def predict_datapoint():
    """
    Handle Fire Weather Index prediction
    
    GET: Display the prediction form
    POST: Process form data and return prediction
    """
    if request.method == "POST":
        try:
            # Validate that models are loaded
            if ridge_model is None or standard_scaler is None:
                flash("Prediction models are not available. Please contact administrator.", "error")
                return render_template('home.html')
            
            # Extract and validate input data
            required_fields = ['Temperature', 'RH', 'Ws', 'Rain', 'FFMC', 'DMC', 'ISI', 'Classes', 'Region']
            input_data = {}
            
            for field in required_fields:
                try:
                    value = request.form.get(field)
                    if value is None or value.strip() == '':
                        flash(f"Please provide a value for {field}", "error")
                        return render_template('home.html')
                    
                    input_data[field] = float(value)
                except ValueError:
                    flash(f"Invalid value for {field}. Please enter a valid number.", "error")
                    return render_template('home.html')
            
            # Additional validation for specific fields
            if not (0 <= input_data['RH'] <= 100):
                flash("Relative Humidity must be between 0 and 100", "error")
                return render_template('home.html')
            
            if input_data['Classes'] not in [0, 1]:
                flash("Classes must be 0 (no fire) or 1 (fire)", "error")
                return render_template('home.html')
            
            if input_data['Region'] not in [1, 2, 3]:
                flash("Region must be 1, 2, or 3", "error")
                return render_template('home.html')
            
            if input_data['Rain'] < 0:
                flash("Rainfall cannot be negative", "error")
                return render_template('home.html')
            
            if input_data['Ws'] < 0:
                flash("Wind Speed cannot be negative", "error")
                return render_template('home.html')
            
            # Prepare data for prediction
            prediction_data = [[
                input_data['Temperature'],
                input_data['RH'],
                input_data['Ws'],
                input_data['Rain'],
                input_data['FFMC'],
                input_data['DMC'],
                input_data['ISI'],
                input_data['Classes'],
                input_data['Region']
            ]]
            
            # Scale the input data
            new_data_scaled = standard_scaler.transform(prediction_data)
            
            # Make prediction
            result = ridge_model.predict(new_data_scaled)
            
            # Format the result to 2 decimal places
            formatted_result = round(float(result[0]), 2)
            
            flash(f"Prediction successful! Fire Weather Index: {formatted_result}", "success")
            return render_template('home.html', result=formatted_result)
            
        except Exception as e:
            flash(f"An error occurred during prediction: {str(e)}", "error")
            return render_template('home.html')
    
    else:
        return render_template('home.html')

@app.errorhandler(404)
def page_not_found(e):
    """Handle 404 errors"""
    return render_template('404.html'), 404 if os.path.exists('templates/404.html') else "Page not found", 404

@app.errorhandler(500)
def internal_server_error(e):
    """Handle 500 errors"""
    return "Internal server error. Please try again later.", 500

if __name__ == "__main__":
    # Run the application
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)


