import json
from pathlib import Path

config_path = Path("servers_config.json")

# 1. Open the file in read mode ('r')
with open(config_path, "r", encoding="utf-8") as file:
    # 2. Convert raw JSON text back into a native Python list
    servers = json.load(file)

# 3. Prove it's a real Python object by filtering it
print("?? Loaded Inventory from File:")
for server in servers:
    if server["status"] == "maintenance":
        print(f"?? ALERT: {server['name']} is currently down for maintenance!")
