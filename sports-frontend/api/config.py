import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# API Configuration
RAPIDAPI_KEY = "750ad01770msh9716fc05e7ecc56p15565fjsn93e405806783"

# Database Configuration
DB_CONFIG = {
    'host': os.getenv('DB_HOST', 'localhost'),
    'database': os.getenv('DB_NAME', 'sportsdb'),
    'user': os.getenv('DB_USER', 'sportsuser'),
    'password': os.getenv('DB_PASSWORD', 'sportspass')
}
