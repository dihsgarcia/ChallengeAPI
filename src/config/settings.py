import json
from pathlib import Path

SETTINGS_FILE = Path(__file__).parent / "settings.json"

def load_settings():
    with open(SETTINGS_FILE, "r") as file:
        return json.load(file)

settings = load_settings()