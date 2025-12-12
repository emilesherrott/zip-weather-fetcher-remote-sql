1. Clone the Repository
`git clone https://github.com/emilesherrott/zip-weather-fetcher.git`
`cd zip-weather-fetcher`

2. Create a Virtual Environment (Recommended)

It’s best to run the project in a virtual environment to manage dependencies.

`python3 -m venv venv`


Activate the virtual environment:

macOS / Linux:

`source venv/bin/activate`


Windows (PowerShell):

`.\venv\Scripts\Activate.ps1`

3. Install Dependencies

Install the required Python packages:

`pip install -r requirements.txt`


If you don’t have a requirements.txt, you can install manually:

`pip install requests`

4. Run the Application
`python main.py`


The script will:

Fetch your ZIP/postal code using ip-api.com.

Fetch the current weather conditions using wttr.in.

Save the results to data/location_weather.json.

Print the combined data to the console.

5. Check the JSON Output

The data will be saved in:

**data/location_weather.json**


Example content:

{
    "zip": "SW1A 1AA",
    "current_weather": {
        "temp_C": "14",
        "temp_F": "57",
        "weather_desc": "Partly cloudy",
        "humidity": "67"
    }
}


You can read this JSON file later or use it in other scripts.

6. Notes

No API keys are required — all APIs are free to use.

Make sure you have an active internet connection.

If the APIs fail, the JSON may include an error message instead of actual data.