from services.db import WeatherDB

def test_insert_and_query(tmp_path):
    db_path = tmp_path / "test.db"
    db = WeatherDB(str(db_path))

    sample = {
        "postcode": "AB12",
        "current_weather": {"temp_C": 20, "temp_F": 68, "humidity": 50, "weather_desc": "Sunny"}
    }

    db.insert_weather(sample)
    rows = db.get_hottest_postcodes()

    assert len(rows) == 1
    assert rows[0][0] == "AB12"  # postcode
    assert rows[0][1] == 20      # average temp

