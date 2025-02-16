# Backend Data Flow

## Dependencies
```
requests==2.28.2
python-dotenv==0.21.0
psycopg2-binary==2.9.5
Flask==2.2.3
schedule==1.1.0
```

## Data Flow Overview

1. **Data Collection Layer**
   - Fetch data from Bet365 API
   - Schedule regular updates
   - Handle API rate limits and errors

2. **Data Processing Layer**
   - Parse and validate incoming data
   - Transform data into required format
   - Filter relevant information

3. **Database Layer**
   - Store processed data in PostgreSQL
   - Maintain historical records
   - Handle data updates and conflicts

4. **API Layer**
   - Flask REST API endpoints
   - Real-time data access
   - Error handling and logging

5. **Frontend Integration**
   - API response format
   - WebSocket updates (future enhancement)
   - Data caching strategy

## API Endpoints Structure

```
/api/v1
├── /odds
│   ├── GET /live      # Get current live odds
│   ├── GET /upcoming  # Get upcoming events
│   └── GET /history   # Get historical odds
├── /events
│   ├── GET /active    # Get active events
│   └── GET /summary   # Get events summary
└── /status
    └── GET /health    # API health check
```

## Data Models

1. **Event**
   - Event ID
   - Sport Type
   - Teams/Participants
   - Start Time
   - Status

2. **Odds**
   - Event ID
   - Odds Type
   - Values
   - Last Updated
   - Source

3. **Market**
   - Market ID
   - Event ID
   - Market Type
   - Status

## Scheduled Tasks

- Data fetching (every 1 minute)
- Database cleanup (daily)
- Performance metrics collection (hourly)
- Error rate monitoring (continuous)

## Error Handling

1. **API Errors**
   - Rate limiting
   - Authentication failures
   - Network timeouts

2. **Database Errors**
   - Connection issues
   - Query failures
   - Data integrity

3. **Processing Errors**
   - Data validation
   - Format conversion
   - Missing fields

## Monitoring & Logging

- Request/Response logging
- Error tracking
- Performance metrics
- API usage statistics
