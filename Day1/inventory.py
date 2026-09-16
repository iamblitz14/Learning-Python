import json
from pathlib import Path

servers = [
    {"name": "web-prod-01", "ip": "10.0.0.1", "status": "active"},
    {"name": "db-prod-01",  "ip": "10.0.0.2", "status": "active"},
    {"name": "web-stage-01", "ip": "192.168.1.1", "status": "active"},
    {"name": "lb-prod-01",   "ip": "10.0.0.3", "status": "active"}
]

# 1. Define the file target using pathlib
output_file = Path("servers_config.json")

# 2. Use a context manager to safely open and write the file
# 'w' means open the file in Write mode (overwrites existing files)
with open(output_file, "w", encoding="utf-8") as file:
    # json.dump(data, target_file, indent) converts list to formatted text
    json.dump(servers, file, indent=4)

print(f"?? Inventory successfully saved to {output_file.resolve()}")
