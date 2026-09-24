"""Exercise the candidate CLI on a legal large Partition input."""
import subprocess
import sys
from pathlib import Path


CANDIDATE = Path(__file__).resolve().parents[2] / "work" / "algorithm.py"
weight = "1" + "0" * 4300
source = '{"numbers": [' + weight + ',' + weight + ']}\n'
result = subprocess.run(
    [sys.executable, str(CANDIDATE)], input=source, text=True, capture_output=True
)
print(f"exit={result.returncode}")
print(result.stderr.strip()[:500])
if result.returncode == 0:
    print(f"output_bytes={len(result.stdout)}")
