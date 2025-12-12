## Setup and Run Instructions for Weather Fetcher

### **2️⃣ Create and activate a virtual environment**

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows PowerShell: venv\Scripts\Activate.ps1
```

* You should now see `(venv)` in your terminal prompt.

---

### **3️⃣ Update `requirements.txt` (if needed) and install dependencies**

Make sure `requirements.txt` contains:

```
requests>=2.31.0
pytest
pytest-mock
requests-mock
python-dotenv>=1.0
psycopg2-binary
```

Then install all dependencies:

```bash
pip install -r requirements.txt
```

---

### **4️⃣ Create a `.env` file**

In the project root:

```bash
touch .env
```

Inside `.env`, put your Supabase connection URL:

```
SUPABASE_DB_URL=postgresql://postgres.yivwkvtfimxdrmlywquh:[YOUR-PASSWORD]@aws-1-eu-north-1.pooler.supabase.com:6543/postgres
```

* Replace `<username>`, `<password>`, `<host>`, `<port>`, `<database>` with your Supabase credentials.
* **Do not commit `.env` to git.**

---

### **5️⃣ Run the application**

* Fetch your current weather and store it:

```bash
python3 main.py
```

* Show hottest postcodes (aggregated by latest entries):

```bash
python3 main.py hot
```

* Show coldest postcodes:

```bash
python3 main.py cold
```

---

### **6️⃣ Notes**

1. `.env` allows all users to point to the **same Supabase DB**.
2. Your `WeatherDB` now supports `recorded_at` timestamps.
3. The hot/cold commands print postcode, temperature, and timestamp.
4. Make sure your Supabase table exists — the code will auto-create it if not.

---

### **7️⃣ Optional: Running tests**

```bash
pytest
```

* Make sure your virtual environment is active before running tests.
* Tests will use mocks for APIs and can run without hitting Supabase.

