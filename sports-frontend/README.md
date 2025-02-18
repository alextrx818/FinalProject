# Sports Odds Dashboard

A real-time sports odds dashboard integrating multiple betting APIs.

## Project Structure

```
/sports-frontend/
├── backend/
│   ├── aggregator/
│   │   └── tennis/
│   │       ├── rapid_tennis.py    # RapidAPI integration
│   │       ├── bets_tennis.py     # BetsAPI integration
│   │       ├── tennis_parser.py   # Data parsing
│   │       └── tennis_merger.py   # Data merging
│   └── serve_api.py              # Backend API server
├── frontend/
│   ├── src/
│   │   └── App.vue              # Main dashboard
│   └── public/
└── docs/
    ├── project_blueprint.md
    └── tools_and_apis.md
```

## Features

- Real-time tennis odds from multiple sources
- Data merging based on player names
- Live match status and scores
- Modern Vue.js dashboard

## API Integrations

- RapidAPI (Bet365)
- BetsAPI

## Tags

- `stable-tennis-v1.0`: Stable tennis API integration
- `v1.0.0-tennis`: Initial tennis API integration