import psycopg2
from psycopg2.extras import DictCursor
from typing import Dict, List, Tuple
from datetime import datetime
from dotenv import load_dotenv
import os

load_dotenv()

DB_URL = os.getenv("SUPABASE_DB_URL")  # your Supabase connection string

class WeatherDB:
    """PostgreSQL wrapper for storing UK weather data on Supabase."""

    def __init__(self, db_url: str = None):
        self.db_url = db_url or DB_URL
        self.conn = psycopg2.connect(self.db_url, cursor_factory=DictCursor)
        self._create_table()

    def _create_table(self):
        """Create the weather table if it doesn't exist."""
        with self.conn:
            with self.conn.cursor() as cur:
                cur.execute("""
                    CREATE TABLE IF NOT EXISTS weather (
                        id SERIAL PRIMARY KEY,
                        postcode TEXT,
                        temp_C REAL,
                        temp_F REAL,
                        humidity REAL,
                        weather_desc TEXT,
                        recorded_at TIMESTAMP
                    )
                """)
            self.conn.commit()

    def insert_weather(self, data: Dict):
        """Insert a weather record into the DB."""
        current = data.get("current_weather", {})

        def safe_float(value):
            try:
                return float(value)
            except (TypeError, ValueError):
                return 0.0

        recorded_at = data.get("recorded_at") or datetime.utcnow()

        with self.conn:
            with self.conn.cursor() as cur:
                cur.execute("""
                    INSERT INTO weather (postcode, temp_C, temp_F, humidity, weather_desc, recorded_at)
                    VALUES (%s, %s, %s, %s, %s, %s)
                """, (
                    data.get("postcode"),
                    safe_float(current.get("temp_C")),
                    safe_float(current.get("temp_F")),
                    safe_float(current.get("humidity")),
                    current.get("weather_desc"),
                    recorded_at
                ))
            self.conn.commit()

    def get_all_records(self, order: str = "DESC") -> List[Tuple[str, float, str]]:
        """Return all weather records with postcode, temp_C, and timestamp."""
        with self.conn.cursor() as cur:
            cur.execute(f"""
                SELECT postcode, temp_C, recorded_at
                FROM weather
                ORDER BY temp_C {order}, recorded_at ASC
            """)
            return [(row["postcode"], row["temp_c"], row["recorded_at"].isoformat()) for row in cur.fetchall()]

