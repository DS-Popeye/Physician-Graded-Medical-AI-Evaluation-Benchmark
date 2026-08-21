import json
from pathlib import Path

def load_cases(directory):
    return [json.loads(p.read_text(encoding="utf-8")) for p in sorted(Path(directory).glob("case_*.json"))]
