import csv
from typing import Tuple


def read_file(file_path: str) -> list[Tuple[str, int]]:
    result = []
    with open(file_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            result.append((row["student"], int(row["coffee_spent"])))
    return result
