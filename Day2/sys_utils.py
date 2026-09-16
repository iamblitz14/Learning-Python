# sys_utils.py
import os
import json
from pathlib import Path

def get_config_path():
    """Reads a target directory path from the OS environment variables."""
    # os.environ.get checks Windows for a variable named 'APP_CONFIG_DIR'
    # If it doesn't exist, it defaults to the current directory '.'
    return os.environ.get("APP_CONFIG_DIR", ".")

def load_system_config(filename):
    """Safely loads a JSON configuration file if it exists."""
    # Combine the environment directory with the filename
    base_dir = Path(get_config_path())
    path = base_dir / filename
    
    if not path.exists():
        return {"error": f"File '{path.resolve()}' not found.", "systems": []}
        
    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)
