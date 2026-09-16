import csv
from pathlib import Path

csv_path = Path("servers_matrix.csv")

# 1. Store our parsed data back into a clean list
imported_servers = []

# 2. Open the CSV file in read mode ('r')
with open(csv_path, "r", encoding="utf-8") as csv_file:
    # Initialize the automated dictionary reader
    reader = csv.DictReader(csv_file)
    
    # 3. Loop through rows - each 'row' is automatically a Python dictionary!
    for row in reader:
        imported_servers.append(row)

# 4. Prove it is a native Python data structure now
print("?? Successfully imported CSV back into Python!")
print(f"Total rows parsed: {len(imported_servers)}")

# ? BUG FIX: Change imported_servers['ip'] to imported_servers[0]['ip']
print(f"First system IP: {imported_servers[0]['ip']}")
