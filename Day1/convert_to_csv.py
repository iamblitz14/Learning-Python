import json
import csv
from pathlib import Path

# 1. Paths for our input and output files
json_path = Path("servers_config.json")
csv_path = Path("servers_matrix.csv")

# 2. Read the existing JSON data
with open(json_path, "r", encoding="utf-8") as json_file:
    servers = json.load(json_file)

# 3. Extract columns headers directly from the dictionary keys
# We want: ['name', 'ip', 'status']
headers = list(servers[0].keys())

# 4. Open the CSV file and write the data matrix
with open(csv_path, "w", newline="", encoding="utf-8") as csv_file:
    # Initialize the structural dictionary writer
    writer = csv.DictWriter(csv_file, fieldnames=headers)
    
    # Write the very top header row
    writer.writeheader()
    
    # Write all rows instantly! 
    writer.writerows(servers)

print(f"?? Matrix generated! CSV saved to: {csv_path.resolve()}")
