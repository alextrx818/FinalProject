"""
HTTP endpoints for accessing sports data.
"""

from flask import jsonify
from database.db_utils import DatabaseManager

db = DatabaseManager()

def register_routes(app):
    @app.route('/api/tennis/live', methods=['GET'])
    def get_live_tennis():
        """Get all live tennis matches"""
        matches = db.get_live_tennis_matches()
        return jsonify({'data': matches})

    @app.route('/api/tennis/match/<match_id>', methods=['GET'])
    def get_tennis_match(match_id):
        """Get specific tennis match details"""
        match = db.get_tennis_match(match_id)
        if not match:
            return jsonify({'error': 'Match not found'}), 404
        return jsonify({'data': match})

    # Add more routes for other sports here
