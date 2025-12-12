import sys
from services.fetch_service import FetchService
from services.data_store import JSONDataStore
from services.db import WeatherDB
from datetime import datetime



JSON_PATH = "data/location_weather.json"

def format_date(iso_string: str) -> str:
    """Convert ISO timestamp to YYYY/MM/DD format."""
    try:
        dt = datetime.fromisoformat(iso_string)
        return dt.strftime("%Y/%m/%d")
    except ValueError:
        return iso_string

def main():
    db = WeatherDB()
    
    # If argument provided
    if len(sys.argv) > 1:
        cmd = sys.argv[1].lower()
        
        if cmd == "hot":
            print("🔥 HOTTEST RECORDS:\n")
            rows = db.get_all_records(order="DESC")
            if not rows:
                print("No data yet. Fetching local weather first...\n")
                FetchService.run(JSON_PATH)
                rows = db.get_all_records(order="DESC")
            for postcode, temp_C, recorded_at in rows:
                print(f"{postcode} → {temp_C}°C on {format_date(recorded_at)}")
            return
        
        elif cmd == "cold":
            print("❄️ COLDEST RECORDS:\n")
            rows = db.get_all_records(order="ASC")
            if not rows:
                print("No data yet. Fetching local weather first...\n")
                FetchService.run(JSON_PATH)
                rows = db.get_all_records(order="ASC")
            for postcode, temp_C, recorded_at in rows:
                print(f"{postcode} → {temp_C}°C on {format_date(recorded_at)}")
            return

    # Default: fetch local weather and save JSON
    combined_data = FetchService.run(JSON_PATH)
    print("📍 Local postcode & current weather:")
    print(combined_data)

    store = JSONDataStore(JSON_PATH)
    print("\nReading back from JSON:")
    print(store.read())

if __name__ == "__main__":
    main()

