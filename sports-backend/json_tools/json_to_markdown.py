import json
import sys
from tabulate import tabulate

def json_to_markdown():
    print("📌 Paste your raw JSON data below and press Enter, then Ctrl+D (Linux/macOS) or Ctrl+Z (Windows) to finish:")

    # Read JSON input from user
    raw_json = ""
    while True:
        try:
            line = input()
            raw_json += line + "\n"
        except EOFError:
            break

    try:
        data = json.loads(raw_json)
        
        if isinstance(data, dict):
            match_name = f"{data.get('team1', '')} vs {data.get('team2', '')}"
            score = data.get('score', '')
            sets = data.get('sets', '')
            game = data.get('game', '')
            serve = data.get('serve', '')
            
            # Create markdown table
            rows = []
            headers = ['Match', 'Market', 'Selection', 'Odds', 'Coef']
            
            for market in data.get('markets', []):
                market_group = market.get('group', '')
                selection_name = market.get('na', market.get('designation', ''))
                
                if market.get('ha'):
                    selection_name = f"{selection_name} ({market['ha']})"
                
                rows.append([
                    match_name,
                    market_group,
                    selection_name,
                    market.get('od', ''),
                    market.get('coef', '')
                ])
            
            # Generate markdown table
            markdown_table = tabulate(rows, headers=headers, tablefmt='pipe')
            
            # Add match details header
            match_details = f"""# Match Details
- **Match**: {match_name}
- **Score**: {score}
- **Sets**: {sets}
- **Current Game**: {game}
- **Serving**: {'Team 1' if serve == 'team1' else 'Team 2' if serve == 'team2' else 'N/A'}

## Betting Markets
"""
            
            output = match_details + "\n" + markdown_table
            
            # Print and save
            print("\n✨ Markdown Output:")
            print(output)
            
            with open('tennis_odds.md', 'w') as f:
                f.write(output)
            print("\n✅ Markdown also saved to 'tennis_odds.md'")
            
        else:
            print("❌ Error: Invalid data format. Expected a dictionary with match details.")
            
    except json.JSONDecodeError as e:
        print(f"❌ Error: Invalid JSON format. Details: {str(e)}")

if __name__ == '__main__':
    json_to_markdown()
