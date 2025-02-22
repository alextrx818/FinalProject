import os
from pathlib import Path

# Base directory of the project
BASE_DIR = Path(__file__).resolve().parent

# Debug mode (should be False in production)
DEBUG = True

# Server settings
HOST = "0.0.0.0"
PORT = 8000

# Database settings
TENNIS_DB = {
    'name': 'tennis_db',
    'host': 'localhost',
    'port': 5432,
}

# API Rate limiting settings
API_RATE_LIMIT = {
    'rapid_api': {
        'requests_per_minute': 60,
        'burst_limit': 5
    },
    'bets_api': {
        'requests_per_minute': 30,
        'burst_limit': 3
    }
}

# Cache settings
CACHE_TIMEOUT = 300  # 5 minutes in seconds
CACHE_ENABLED = True

# Logging configuration
LOG_LEVEL = 'INFO'
LOG_FILE = os.path.join(BASE_DIR, 'logs', 'app.log')

# Tennis data specific settings
TENNIS_DATA_UPDATE_INTERVAL = 60  # seconds
TENNIS_MATCH_RETENTION_DAYS = 7  # days to keep historical match data

# Feature flags
FEATURES = {
    'live_odds_enabled': True,
    'historical_data_enabled': True,
    'api_monitoring_enabled': True
}
