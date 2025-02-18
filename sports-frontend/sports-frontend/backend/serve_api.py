# API server to serve data to frontend

from flask import Flask, jsonify
from flask_cors import CORS
import psycopg2
from psycopg2.extras import RealDictCursor

app = Flask(__name__)
CORS(app)

def get_db_connection():
    return psycopg2.connect(
        host="localhost",
        database="sports_odds",
        user="amireslami",
        password="Lincoln95$",
        cursor_factory=RealDictCursor
    )

@app.route('/api/odds/live')
def get_live_odds():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM tennis_odds WHERE status = %s', ('Live',))
    odds = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify({'data': odds})

if __name__ == '__main__':
    app.run(port=5000)
