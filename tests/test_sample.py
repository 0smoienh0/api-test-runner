import json, requests
from pathlib import Path

CONFIG_PATH = Path("/tests/config/apis.json")

def test_apis():
    targets = json.loads(CONFIG_PATH.read_text())
    for name, url in targets.items():
        res = requests.get(url, timeout=5)
        assert res.status_code == 200, f"{name} failed with {res.status_code}"
