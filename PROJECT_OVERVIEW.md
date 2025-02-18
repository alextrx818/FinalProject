# Sports Odds Dashboard - Project Overview

## Project Architecture

```
Frontend (Port 5173) ←→ Backend API (Port 5000) ←→ Database ←→ Sport Parsers ←→ Bet365 API
```

## Component Overview

### 1. Frontend (`/sports-frontend/sports-frontend/`)
- **Technology**: Vue.js + Quasar UI
- **Key Files**:
  - `src/App.vue`: Main dashboard with stats cards and odds table
  - `public/mock_odds.json`: Mock data (to be replaced with real API)
- **Features**:
  - Live sports odds display
  - Active matches counter
  - Total events tracking
  - Real-time updates

### 2. Backend API (`/sports-backend/`)
- **Technology**: Flask + PostgreSQL
- **Key Files**:
  - `serve_api.py`: Flask API server
  - `aggregator/*/`: Sport-specific parsers
- **Endpoints**:
  - `/api/odds/live`: Get live odds data
  - More endpoints planned (see backend_data_flow.md)

### 3. Data Flow
1. Sport Parsers fetch data from Bet365 API
2. Data is processed and validated
3. Processed data stored in PostgreSQL
4. Flask API serves data from database
5. Frontend fetches and displays data

### 4. Database
- **Type**: PostgreSQL
- **Key Tables**:
  - `tennis_odds`: Stores live tennis odds data
  - More tables to be added for other sports

## Current Status
- Backend API and database structure set up
- Frontend using mock data
- Need to complete:
  1. Bet365 API configuration
  2. Frontend-backend connection
  3. Real-time data implementation

## Development Notes
- Frontend dev server: `http://localhost:5173`
- Backend API server: `http://localhost:5000`
- Database connection in `serve_api.py`
- Sport-specific parsers handle different data structures

## File Structure
```
/root/
├── sports-frontend/
│   └── sports-frontend/
│       ├── src/
│       │   └── App.vue
│       └── public/
│           └── mock_odds.json
└── sports-backend/
    ├── serve_api.py
    └── aggregator/
        └── tennis/
            ├── rapid_inplay.py
            └── rapid_tennis.py
```
