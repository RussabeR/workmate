
import csv
from src.services.aggregator import aggregate_files
from collections import defaultdict

def test_aggregate_files(tmp_path):
    file = tmp_path / "data.csv"
    with open(file, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["student","date","coffee_spent","sleep_hours","study_hours","mood","exam"])
        writer.writerow(["Иванов Сергей","2024-06-01","100","7","5","отлично","Математика"])
        writer.writerow(["Тестова Анна","2024-06-02","150","6","6","устал","Физика"])
        writer.writerow(["Студентов Петр","2024-06-01","200","5","7","зомби","Математика"])
        writer.writerow(["Иванов Сергей", "2024-06-01", "150", "7", "7", "зомби", "Математика"])

    result = aggregate_files([str(file)])

    assert isinstance(result, defaultdict)
    assert result["Иванов Сергей"] == [100, 150]
    assert result["Тестова Анна"] == [150]