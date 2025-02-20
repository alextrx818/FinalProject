"""
Tennis database models and table definitions.
"""

# SQL for creating tennis_matches table
CREATE_TENNIS_MATCHES_TABLE = """
CREATE TABLE IF NOT EXISTS tennis_matches (
    match_id    VARCHAR(50) PRIMARY KEY,
    raw_data    JSONB NOT NULL,
    inserted_at TIMESTAMP DEFAULT NOW()
);
"""

# Index for faster JSON queries
CREATE_TENNIS_MATCHES_INDEX = """
CREATE INDEX IF NOT EXISTS idx_tennis_matches_raw_data 
ON tennis_matches USING gin (raw_data);
"""
