import os
from datetime import timedelta

class Config:
    """Base configuration class"""
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-key-change-in-production'
    
    # Model paths
    MODEL_PATH = os.path.join('models', 'ridge.pkl')
    SCALER_PATH = os.path.join('models', 'scaler.pkl')
    
    # Application settings
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB max file size
    
    # Security settings
    PERMANENT_SESSION_LIFETIME = timedelta(hours=1)
    
    # Input validation ranges
    VALIDATION_RANGES = {
        'Temperature': (-50, 60),  # Celsius
        'RH': (0, 100),           # Percentage
        'Ws': (0, 200),           # km/h
        'Rain': (0, 1000),        # mm
        'FFMC': (0, 100),         # Fire Weather Index scale
        'DMC': (0, 1000),         # Duff Moisture Code scale
        'ISI': (0, 100),          # Initial Spread Index scale
        'Classes': [0, 1],        # Binary classification
        'Region': [1, 2, 3]       # Specific regions
    }
    
    # Fire risk thresholds for FWI
    FIRE_RISK_THRESHOLDS = {
        'low': 5,
        'moderate': 15,
        'high': 25
    }

class DevelopmentConfig(Config):
    """Development configuration"""
    DEBUG = True
    TESTING = False

class ProductionConfig(Config):
    """Production configuration"""
    DEBUG = False
    TESTING = False
    SECRET_KEY = os.environ.get('SECRET_KEY')  # Must be set in production

class TestingConfig(Config):
    """Testing configuration"""
    DEBUG = True
    TESTING = True
    WTF_CSRF_ENABLED = False

# Configuration dictionary
config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig
} 