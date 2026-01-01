import json
f = open('C:\\Users\\GudiboinaSaiKishore\\OneDrive - KPI PARTNERS INC\\Desktop\\DE projects\\AWS\\AWS serverless ETL Pipeline\\orders_etl.json', "r")
data = json.loads(f) 
data

import json
from pathlib import Path

# Get the directory of the current Python file
BASE_DIR = Path(__file__).resolve().parent

# Path to JSON file
json_file = BASE_DIR / 'C:\\Users\\GudiboinaSaiKishore\\OneDrive - KPI PARTNERS INC\\Desktop\\DE projects\\AWS\\AWS serverless ETL Pipeline\\orders_etl.json'

# Read JSON
with json_file.open("r", encoding="utf-8") as f:
    data = json.load(f)

print(data)



