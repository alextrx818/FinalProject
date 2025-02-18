import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from flask import Flask
from aggregator.sports.tennis.rapid_tennis_fetcher import RapidInplayOddsFetcher
import json
from datetime import datetime
import threading

app = Flask(__name__)

# Global variables for tracking
last_successful_update = None
last_successful_data = None
update_lock = threading.Lock()

class TestStats:
    def __init__(self):
        self.total_attempts = 0
        self.successful_attempts = 0
        self.failed_attempts = 0
        self.error_log = []
        self.max_error_log = 10
    
    def log_attempt(self, success, error_msg=None):
        self.total_attempts += 1
        if success:
            self.successful_attempts += 1
        else:
            self.failed_attempts += 1
            if error_msg:
                self.error_log.append((datetime.now(), error_msg))
                self.error_log = self.error_log[-self.max_error_log:]
    
    @property
    def success_rate(self):
        if self.total_attempts == 0:
            return 0
        return (self.successful_attempts / self.total_attempts) * 100

test_stats = TestStats()

def get_time_since_last_success():
    if not last_successful_update:
        return "No successful updates yet"
    delta = datetime.now() - last_successful_update
    hours = delta.seconds // 3600
    minutes = (delta.seconds % 3600) // 60
    seconds = delta.seconds % 60
    if delta.days > 0:
        return f"{delta.days}d {hours}h {minutes}m {seconds}s"
    elif hours > 0:
        return f"{hours}h {minutes}m {seconds}s"
    elif minutes > 0:
        return f"{minutes}m {seconds}s"
    else:
        return f"{seconds}s"

def format_player_name(name):
    """Format player name to be more readable"""
    if not name:
        return "N/A"
    return name.replace("_", " ").title()

def format_score(score_data):
    """Format score data to be more readable"""
    if not score_data or score_data == "N/A":
        return "No Score"
    try:
        # Try to parse and format the score data
        return score_data.replace(";", " | ")
    except:
        return str(score_data)

def format_time(time_str):
    """Format time to be more readable"""
    if not time_str or time_str == "N/A":
        return "Time not available"
    try:
        # Assuming time is in a standard format, adjust as needed
        return time_str.replace("T", " ").replace("Z", " UTC")
    except:
        return str(time_str)

@app.route('/')
def view_tennis_data():
    global last_successful_update, last_successful_data
    
    current_time = datetime.now()
    fetcher = RapidInplayOddsFetcher()
    debug_info = []
    
    try:
        print("Attempting to fetch tennis data...")
        new_data = fetcher.get_tennis_data()
        debug_info.append(f"Raw data type: {type(new_data)}")
        debug_info.append(f"Raw data: {new_data}")
        
        if new_data and isinstance(new_data, list):
            with update_lock:
                last_successful_update = current_time
                last_successful_data = new_data
            data = new_data
            test_stats.log_attempt(True)
            debug_info.append(f"Successfully fetched {len(data)} matches")
        else:
            debug_info.append(f"No valid data received: {new_data}")
            data = last_successful_data if last_successful_data else []
            test_stats.log_attempt(False, "Empty or invalid data received")
    except Exception as e:
        error_msg = str(e)
        debug_info.append(f"Error fetching data: {error_msg}")
        print(f"Error fetching data: {error_msg}")
        data = last_successful_data if last_successful_data else []
        test_stats.log_attempt(False, error_msg)
    
    current_time_str = current_time.strftime("%Y-%m-%d %H:%M:%S")
    last_success_str = last_successful_update.strftime("%Y-%m-%d %H:%M:%S") if last_successful_update else "Never"
    time_since_success = get_time_since_last_success()
    
    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Tennis Data Test Viewer</title>
        <meta http-equiv="refresh" content="60">
        <style>
            @media print {{
                body {{
                    font-size: 12pt;
                    line-height: 1.5;
                    background: white;
                }}
                .no-print {{
                    display: none !important;
                }}
                .match-card {{
                    page-break-inside: avoid;
                    border: 1px solid #000 !important;
                    margin: 20px 0 !important;
                }}
                .container {{
                    max-width: none !important;
                    margin: 0 !important;
                    padding: 0 !important;
                    box-shadow: none !important;
                }}
            }}
            body {{
                font-family: 'Courier New', monospace;
                margin: 20px;
                background-color: #f5f5f5;
                line-height: 1.6;
            }}
            .container {{
                max-width: 1400px;
                margin: 0 auto;
                background-color: white;
                padding: 20px;
                border-radius: 8px;
                box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            }}
            .match-card {{
                background: white;
                border: 2px solid #e0e0e0;
                border-radius: 8px;
                margin: 30px 0;
                padding: 20px;
                box-shadow: 0 2px 4px rgba(0,0,0,0.05);
                position: relative;
                overflow: hidden;
            }}
            .match-header {{
                background: #f8f9fa;
                margin: -20px -20px 20px -20px;
                padding: 15px 20px;
                border-bottom: 1px solid #e0e0e0;
                font-size: 1.2em;
                font-weight: bold;
            }}
            .match-number {{
                position: absolute;
                top: 15px;
                right: 20px;
                font-size: 1.2em;
                color: #9e9e9e;
            }}
            .match-data {{
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
                gap: 20px;
                margin-bottom: 20px;
            }}
            .match-info {{
                padding: 10px;
                background: #f8f9fa;
                border-radius: 4px;
            }}
            .info-label {{
                font-weight: bold;
                color: #666;
                margin-right: 10px;
            }}
            .info-value {{
                font-family: 'Courier New', monospace;
            }}
            .score {{
                font-size: 1.2em;
                font-weight: bold;
                color: #2196F3;
                padding: 10px;
                background: #e3f2fd;
                border-radius: 4px;
                text-align: center;
                margin: 10px 0;
            }}
            .serving {{
                display: inline-block;
                padding: 3px 8px;
                background: #4caf50;
                color: white;
                border-radius: 4px;
                font-size: 0.9em;
                margin-left: 10px;
            }}
            .test-stats {{
                background-color: #f3e5f5;
                padding: 15px;
                border-radius: 4px;
                margin: 15px 0;
            }}
            .stats-grid {{
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
                gap: 10px;
                margin-top: 10px;
            }}
            .stat-box {{
                background-color: #fff;
                padding: 10px;
                border-radius: 4px;
                box-shadow: 0 1px 3px rgba(0,0,0,0.1);
            }}
            .stat-value {{
                font-size: 1.2em;
                font-weight: bold;
                color: #673ab7;
            }}
            .error-log {{
                background-color: #ffebee;
                padding: 10px;
                border-radius: 4px;
                margin-top: 10px;
            }}
            .error-entry {{
                border-bottom: 1px solid #ffcdd2;
                padding: 5px 0;
            }}
            .error-time {{
                color: #d32f2f;
                font-size: 0.9em;
            }}
            .current-time {{
                position: fixed;
                top: 10px;
                left: 10px;
                background-color: #fff;
                padding: 10px;
                border-radius: 4px;
                box-shadow: 0 2px 4px rgba(0,0,0,0.1);
                z-index: 1000;
            }}
            .time-label {{
                color: #555;
                font-size: 0.9em;
            }}
            .time-value {{
                font-size: 1.1em;
                font-weight: bold;
                color: #1a237e;
            }}
            .debug-info {{
                background-color: #e3f2fd;
                padding: 15px;
                border-radius: 4px;
                margin: 15px 0;
                font-family: monospace;
                white-space: pre-wrap;
                word-break: break-all;
            }}
            .match-title {{
                font-size: 1.3em;
                color: #1a237e;
            }}
            .player-section {{
                text-align: center;
                margin: 15px 0;
                padding: 10px;
                background: #f5f5f5;
                border-radius: 8px;
            }}
            .player {{
                margin: 10px 0;
                font-size: 1.2em;
                font-weight: bold;
            }}
            .player-name {{
                color: #2196F3;
            }}
            .versus {{
                font-size: 0.9em;
                color: #9e9e9e;
                margin: 5px 0;
            }}
            .score-section {{
                margin: 15px 0;
                padding: 15px;
                background: #e3f2fd;
                border-radius: 8px;
            }}
            .score {{
                font-size: 1.4em;
                font-weight: bold;
                color: #1565c0;
                text-align: center;
                margin-bottom: 10px;
            }}
            .sets, .current-game {{
                font-size: 1.1em;
                margin: 5px 0;
            }}
            .serving {{
                display: inline-block;
                padding: 3px 8px;
                background: #4caf50;
                color: white;
                border-radius: 4px;
                font-size: 0.9em;
                margin-left: 10px;
                vertical-align: middle;
            }}
        </style>
        <script>
            function updateTime() {{
                const now = new Date();
                document.getElementById('browser-time').textContent = now.toLocaleTimeString();
                document.getElementById('browser-date').textContent = now.toLocaleDateString();
            }}
            
            setInterval(updateTime, 1000);
            window.onload = updateTime;
        </script>
    </head>
    <body>
        <div class="current-time">
            <div class="time-label">Browser Time</div>
            <div class="time-value" id="browser-time"></div>
            <div class="time-value" id="browser-date"></div>
        </div>

        <div class="container">
            <h1>Tennis Data Test View</h1>
            
            <div class="test-stats no-print">
                <h2>Test Statistics</h2>
                <div class="stats-grid">
                    <div class="stat-box">
                        <div>Server Time</div>
                        <div class="stat-value">{current_time_str}</div>
                    </div>
                    <div class="stat-box">
                        <div>Last Successful Update</div>
                        <div class="stat-value">{last_success_str}</div>
                    </div>
                    <div class="stat-box">
                        <div>Time Since Success</div>
                        <div class="stat-value">{time_since_success}</div>
                    </div>
                    <div class="stat-box">
                        <div>Success Rate</div>
                        <div class="stat-value">{test_stats.success_rate:.1f}%</div>
                    </div>
                    <div class="stat-box">
                        <div>Total Attempts</div>
                        <div class="stat-value">{test_stats.total_attempts}</div>
                    </div>
                    <div class="stat-box">
                        <div>Failed Attempts</div>
                        <div class="stat-value">{test_stats.failed_attempts}</div>
                    </div>
                </div>
                
                <div class="error-log">
                    <h3>Recent Errors</h3>
                    {''.join([
                        f'<div class="error-entry">'
                        f'<span class="error-time">{ts.strftime("%Y-%m-%d %H:%M:%S")}</span>: {err}'
                        f'</div>'
                        for ts, err in reversed(test_stats.error_log)
                    ]) if test_stats.error_log else 'No errors logged'}
                </div>
                
                <div class="debug-info">
                    <h3>Debug Information</h3>
                    {'<br>'.join(debug_info)}
                </div>
            </div>

            <div>
                <h2>Tennis Matches ({len(data)} total)</h2>
            </div>
    """
    
    if data:
        for idx, match in enumerate(data, 1):
            odds_data = match.get('odds_data', {})
            
            # Extract and format player names
            player1 = format_player_name(match.get('player1', 'N/A'))
            player2 = format_player_name(match.get('player2', 'N/A'))
            
            # Format score
            score = format_score(odds_data.get('score', 'N/A'))
            sets = odds_data.get('sets', 'N/A')
            current_game = odds_data.get('game', 'N/A')
            
            # Format serving status
            serving = odds_data.get('serve', '').strip()
            serving_player = ""
            serving_indicator = ""
            if serving:
                serving_player = format_player_name(serving)
                serving_indicator = f'<span class="serving">SERVING</span>'
            
            # Format league and event info
            league = match.get('liga', 'N/A').replace("_", " ").title()
            event_name = match.get('eventName', 'N/A').replace("_", " ").title()
            
            # Format status and time
            status = match.get('status', 'N/A').replace("_", " ").title()
            match_time = format_time(match.get('time', 'N/A'))
            
            html += f"""
                <div class="match-card">
                    <div class="match-header">
                        <span class="match-title">Match #{idx}: {player1} vs {player2}</span>
                        <div class="match-number">#{idx}</div>
                    </div>
                    
                    <div class="match-data">
                        <div class="match-info">
                            <div class="player-section">
                                <div class="player player1">
                                    <span class="player-name">{player1}</span>
                                    {serving_indicator if serving_player == player1 else ''}
                                </div>
                                <div class="versus">VS</div>
                                <div class="player player2">
                                    <span class="player-name">{player2}</span>
                                    {serving_indicator if serving_player == player2 else ''}
                                </div>
                            </div>
                            
                            <div class="score-section">
                                <div class="score">Current Score: {score}</div>
                                <div class="sets"><span class="info-label">Sets:</span> {sets}</div>
                                <div class="current-game"><span class="info-label">Current Game:</span> {current_game}</div>
                            </div>
                        </div>
                        
                        <div class="match-info">
                            <div><span class="info-label">Tournament:</span> <span class="info-value">{league}</span></div>
                            <div><span class="info-label">Event:</span> <span class="info-value">{event_name}</span></div>
                            <div><span class="info-label">Status:</span> <span class="info-value">{status}</span></div>
                            <div><span class="info-label">Match Time:</span> <span class="info-value">{match_time}</span></div>
                        </div>
                    </div>
                </div>
            """
    else:
        html += """
            <div style="padding: 20px; background-color: #fff3e0; border-radius: 4px; margin-top: 20px;">
                <h3 style="color: #e65100;">No Match Data Available</h3>
                <p>Check the debug information and error log above for details.</p>
            </div>
        """
    
    html += """
        </div>
    </body>
    </html>
    """
    return html

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
