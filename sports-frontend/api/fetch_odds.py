from bet365_client import Bet365Client
from config import RAPIDAPI_KEY
import json
from datetime import datetime

def main():
    # Initialize the client
    client = Bet365Client(RAPIDAPI_KEY)
    
    # Fetch all tennis data
    tennis_data = client.get_all_tennis_data()
    
    # Save to a file with timestamp (for testing/backup)
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    with open(f'../public/tennis_data_{timestamp}.json', 'w') as f:
        json.dump(tennis_data, f, indent=2)
    
    # Update the main mock file for the frontend
    processed_data = []
    for item in tennis_data:
        event = item['event']
        markets = item['markets']
        
        # Extract relevant odds (you may want to adjust this based on the actual data structure)
        processed_data.append({
            'id': event.get('id'),
            'match': event.get('name', ''),
            'status': 'Live',
            'sport': 'Tennis',
            'pre_odds': markets.get('pre_odds', 0.0) if markets else 0.0,
            'live_odds': markets.get('live_odds', 0.0) if markets else 0.0,
            'trend': 0.0  # You'll need to calculate this based on historical data
        })
    
    # Update the mock_odds.json file
    with open('../public/mock_odds.json', 'w') as f:
        json.dump(processed_data, f, indent=2)

if __name__ == "__main__":
    main()
