import pytest

from src.reports.base import BaseReport


@pytest.fixture
def tmp_csv_files(tmp_path):
    files = []
    data = {
        "math.csv": "student,coffee_spent\nИванов Сергей,100\nТестова Анна,200\nСтудентов Петр,300\n",
        "physics.csv": "student,coffee_spent\nИванов Сергей,150\nТестова Анна,200\nСтудентов Петр,300\n",
    }

    for filename, content in data.items():
        f = tmp_path / filename
        f.write_text(content, encoding="utf-8")
        files.append(f)
    return files



