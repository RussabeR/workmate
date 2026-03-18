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



@pytest.fixture
def sample_report_registry():
    class FakeReport(BaseReport):
        def calculate(self, data):
            return [(student, sum(grades)) for student, grades in data.items()]
        def name(self):
            return "median_coffee"

    BaseReport.registry.clear()
    BaseReport.registry["median_coffee"] = FakeReport
    return BaseReport.registry