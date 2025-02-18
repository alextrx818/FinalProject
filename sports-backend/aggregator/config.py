"""
Shared configuration settings for APIs and database connections.
"""

import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# API Credentials
API_CREDENTIALS = {
    "bet365": {
        "api_key": os.getenv("BET365_API_KEY", "750ad01770msh9716fc05e7ecc56p15565fjsn93e405806783"),
        "api_host": "bet365-api-inplay.p.rapidapi.com"
    },
    "betsapi": {
        "token": os.getenv("BETSAPI_TOKEN", "213380-bmgdFz8UeXJ4kL")
    }
}

# RapidAPI Configuration
RAPID_API_KEY = API_CREDENTIALS["bet365"]["api_key"]
RAPID_API_HOST = API_CREDENTIALS["bet365"]["api_host"]
RAPID_API_URL = "https://bet365-api-inplay.p.rapidapi.com"

# Database Configuration
DB_CONFIG = {
    "host": os.getenv("DB_HOST", "localhost"),
    "database": os.getenv("DB_NAME", "sports_odds"),
    "user": os.getenv("DB_USER", "amireslami"),
    "password": os.getenv("DB_PASSWORD", "Lincoln95$")
}

# API Base URLs
API_URLS = {
    "bet365": "https://bet365-api-inplay.p.rapidapi.com/bet365",
    "betsapi": "https://api.b365api.com/v3"
}

# API Endpoints
API_ENDPOINTS = {
    "tennis": {
        "inplay_events": "/get_sport_events/tennis"
    }
}

# API Request Settings
REQUEST_CONFIG = {
    "timeout": 30,
    "max_retries": 3,
    "retry_delay": 5,
    "max_workers": 10
}
