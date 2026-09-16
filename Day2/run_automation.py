# run_automation.py
from sys_utils import load_system_config

# 1. Load the raw inventory array using our helper module
config_data = load_system_config("servers_config.json")

# 2. Defensive check: Ensure we got a list back, not an error dictionary
if isinstance(config_data, list):
    # ?? Extract systems requiring maintenance using a list comprehension
    down_servers = [sys["name"] for sys in config_data if sys["status"] == "maintanance"]
    
    print("?? Automation Status Check Complete!")
    print(f"?? Action Required: The following systems are offline: {down_servers}")
else:
    print(f"? Automation Failure: {config_data.get('error')}")
