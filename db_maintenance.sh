#!/bin/bash

# Vacuum and analyze all databases
echo "Running VACUUM ANALYZE on all databases..."
sudo -u postgres psql -c "VACUUM ANALYZE;"

# Reindex the tennis_db
echo "Reindexing tennis_db..."
sudo -u postgres psql -d tennis_db -c "REINDEX DATABASE tennis_db;"

# Update table statistics
echo "Updating table statistics..."
sudo -u postgres psql -d tennis_db -c "ANALYZE VERBOSE;"

# Check for bloat in tables
echo "Checking for table bloat..."
sudo -u postgres psql -d tennis_db -c "
SELECT schemaname, tablename, pg_size_pretty(size) as size, pg_size_pretty(bloat_size) as bloat_size, round(bloat_ratio::numeric, 2) as bloat_ratio 
FROM (
  SELECT *, (bloat_size::float / size::float * 100) as bloat_ratio
  FROM (
    SELECT 
      n.nspname as schemaname,
      c.relname as tablename,
      pg_table_size(c.oid) as size,
      CASE WHEN c.reltoastrelid = 0 THEN 0
           ELSE pg_total_relation_size(c.reltoastrelid)
      END as bloat_size
    FROM pg_class c
    LEFT JOIN pg_namespace n ON n.oid = c.relnamespace
    WHERE c.relkind = 'r'
  ) as a
) as a
WHERE bloat_ratio > 10
ORDER BY bloat_ratio DESC;"

# Log database sizes
echo "Current database sizes:"
sudo -u postgres psql -c "SELECT datname, pg_size_pretty(pg_database_size(datname)) FROM pg_database;"
